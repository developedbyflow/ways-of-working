#!/usr/bin/env python3
"""Keeps only the number on each arrow of a view whose properties say "labels" "numbers": a drawing with many
arrows (the map of the modules) where the arrows' texts would cross each other; the text of each number is
in the table under the drawing, which check-tables.py compares with the model. In workspace.dsl:

    component product.api "modules" {
        include *
        properties {
            "labels" "numbers"
        }
    }

Every other view is left as it is. Reads the view's properties from the Structurizr JSON; rewrites the
PlantUML file given. Standard library only.

  numbers-only.py <workspace.json> <view key> <view.puml>
"""
import json
import re
import sys

workspace_json, key, path = sys.argv[1:]
views = json.load(open(workspace_json, encoding="utf-8"))["views"]
view = next((v for kind in views.values() if isinstance(kind, list) for v in kind if v.get("key") == key), {})
if (view.get("properties") or {}).get("labels") == "numbers":
    text = open(path, encoding="utf-8").read()
    text = re.sub(r'^(.* : )"([0-9]+)\. [^"]*"$', r'\1"\2."', text, flags=re.M)
    open(path, "w", encoding="utf-8").write(text)
