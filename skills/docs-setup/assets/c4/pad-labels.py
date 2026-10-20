#!/usr/bin/env python3
"""Adds a little room inside every C4 box: PlantUML draws a box exactly as wide as its widest line,
so a description touches the edges. Pads each description line with non-breaking spaces (never the name,
which starts with "==", nor the [type] line). Reads and writes the PlantUML file given."""
import re
import sys

PAD = " " * 3


def pad(match):
    lines = match.group(2).split("\\n")
    lines = [PAD + line + PAD if line and not line.startswith(("==", "<size")) else line for line in lines]
    return match.group(1) + '"' + "\\n".join(lines) + '"'


path = sys.argv[1]
text = open(path, encoding="utf-8").read()
text = re.sub(r'^(\s*(?:person|rectangle|database|queue) )"(==[^"]*)"', pad, text, flags=re.M)
open(path, "w", encoding="utf-8").write(text)
