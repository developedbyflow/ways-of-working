#!/usr/bin/env python3
"""Draws the model's groups in every C4 view where the exporter leaves them out.

The Structurizr CLI draws a group ("Outside systems") in the context view, but not in the container and
component views, where the same systems sit outside the box being opened. This wraps their boxes in the
group, with the style the exporter gives it in the context view (a dashed grey frame). Only boxes at the top
level of the drawing are wrapped, so a deployment view (boxes inside nodes) is left as it is.
Standard library only. Reads the model as Structurizr JSON and rewrites the PlantUML file given.

  add-groups.py <workspace.json> <view.puml>
"""
import base64
import json
import re
import sys

STYLE = """  // {name}
  .Group-{key} {{
    BackgroundColor: #ffffff;
    LineColor: #444444;
    LineStyle: 2-2;
    LineThickness: 2;
    FontColor: #444444;
    FontSize: 24;
    HorizontalAlignment: center;
    Shadowing: 0;
  }}
"""


def groups(workspace):
    """{group name: [element names]} for the people and software systems that sit in a group."""
    found = {}
    model = workspace["model"]
    for element in (model.get("people") or []) + (model.get("softwareSystems") or []):
        if element.get("group"):
            found.setdefault(element["group"], []).append(element["name"])
    return found


workspace_path, puml_path = sys.argv[1], sys.argv[2]
workspace = json.load(open(workspace_path, encoding="utf-8"))
lines = open(puml_path, encoding="utf-8").read().split("\n")

for group, names in groups(workspace).items():
    key = base64.b64encode(group.encode()).decode().rstrip("=")
    if any(f"<<Group-{key}>>" in line for line in lines):
        continue  # the exporter drew it already
    boxes = [i for i, line in enumerate(lines)
             if re.match(r'^(rectangle|person|database|queue) "==([^\\"]*)', line)
             and re.match(r'^\S+ "==([^\\"]*)', line).group(1) in names]
    if not boxes:
        continue
    moved = [lines[i] for i in boxes]
    lines = [line for i, line in enumerate(lines) if i not in boxes]
    at = next(i for i, line in enumerate(lines) if line == "</style>")
    lines[at:at] = STYLE.format(name=group, key=key).rstrip("\n").split("\n")
    at = lines.index("</style>") + 1
    lines[at:at] = ["", f'rectangle "{group}" <<Group-{key}>> as group{key} {{'] + ["  " + m for m in moved] + ["}"]

open(puml_path, "w", encoding="utf-8").write("\n".join(lines))
