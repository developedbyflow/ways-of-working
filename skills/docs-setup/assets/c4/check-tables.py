#!/usr/bin/env python3
"""Checks that each C4 drawing and the table under it in the Markdown say the same thing.

For every view listed in c4/views.txt with a third field (the Markdown file that holds its table):
  - every number on an arrow of the view ("5. Starts checkout") is a row of the table, and every row is an arrow;
  - each arrow's two ends are named in its row's "From → to" cell (the name, or its first word).
Reads the model as Structurizr JSON (exported by diagrams.sh), the table as the first Markdown table whose
first column is "#". Standard library only. Exit code 1 and a list of differences when they disagree.

  check-tables.py <workspace.json> <docs/02-design folder>
"""
import json
import re
import sys
from pathlib import Path

NUMBER = re.compile(r"^\s*([0-9]+|[A-Z])\.\s")


def elements_by_id(workspace):
    found = {}

    def walk(items):
        for item in items or []:
            found[item["id"]] = item
            for key in ("containers", "components", "children", "containerInstances",
                        "softwareSystemInstances", "infrastructureNodes"):
                walk(item.get(key))

    model = workspace["model"]
    for key in ("people", "softwareSystems", "deploymentNodes"):
        walk(model.get(key))
    return found


def relationships_by_id(elements):
    found = {}
    for element in elements.values():
        for relationship in element.get("relationships") or []:
            found[relationship["id"]] = relationship
    return found


def name_of(element, elements):
    """An instance takes the name of what it's an instance of."""
    for key in ("containerId", "softwareSystemId"):
        if key in element:
            return elements[element[key]]["name"]
    return element["name"]


def view_arrows(view, elements, relationships):
    """(number, source name, destination name, label) for every numbered arrow in the view."""
    arrows = []
    for shown in view.get("relationships") or []:
        relationship = relationships[shown["id"]]
        description = relationship.get("description", "")
        if relationship.get("linkedRelationshipId") and not description:
            description = relationships[relationship["linkedRelationshipId"]].get("description", "")
        match = NUMBER.match(description)
        if not match:
            continue
        arrows.append((match.group(1), name_of(elements[relationship["sourceId"]], elements),
                       name_of(elements[relationship["destinationId"]], elements), description))
    return arrows


def table_rows(markdown):
    """{number: "From → to" cell} from the first table whose first header cell is "#"."""
    rows, in_table = {}, False
    for line in markdown.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not line.lstrip().startswith("|"):
            if in_table:
                break
            continue
        if cells[0] == "#":
            in_table = True
            continue
        if not in_table or set(cells[0]) <= set("-: "):
            continue
        number = cells[0]
        if any(cell.startswith("~~") for cell in cells[:2]):     # a struck-through row: removed
            continue
        span = re.match(r"^([0-9]+)[–-]([0-9]+)$", number)
        numbers = [str(n) for n in range(int(span.group(1)), int(span.group(2)) + 1)] if span else [number]
        for n in numbers:
            rows[n] = cells[1] if len(cells) > 1 else ""
    return rows


def named(name, cell):
    cell = cell.lower()
    short = name.split(" (")[0].lower()
    return short in cell or short.split()[0] in cell


def main():
    workspace_json, design = Path(sys.argv[1]), Path(sys.argv[2])
    workspace = json.loads(workspace_json.read_text())
    elements = elements_by_id(workspace)
    relationships = relationships_by_id(elements)
    views = {}
    for kind in ("systemLandscapeViews", "systemContextViews", "containerViews", "componentViews", "deploymentViews"):
        for view in workspace["views"].get(kind) or []:
            views[view["key"]] = view

    problems = []
    for line in (design / "c4" / "views.txt").read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.strip().split(":")
        if len(parts) < 3:
            continue
        key, markdown_file = parts[0], design / parts[2]
        arrows = view_arrows(views[key], elements, relationships)
        rows = table_rows(markdown_file.read_text())
        drawn = {arrow[0] for arrow in arrows}
        for number in sorted(drawn - rows.keys(), key=lambda n: (len(n), n)):
            problems.append(f"{key}: arrow {number} is drawn but has no row in {parts[2]}")
        for number in sorted(rows.keys() - drawn, key=lambda n: (len(n), n)):
            problems.append(f"{key}: row {number} of {parts[2]} has no arrow in the drawing")
        for number, source, destination, label in arrows:
            cell = rows.get(number)
            if cell is None:
                continue
            for end in (source, destination):
                if not named(end, cell):
                    problems.append(f"{key}: arrow \"{label}\" ({source} → {destination}): "
                                    f"\"{end}\" isn't named in row {number} (\"{cell}\")")
        if not problems or not any(p.startswith(key + ":") for p in problems):
            print(f"{key}: {len(arrows)} arrows match {parts[2]}")

    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
