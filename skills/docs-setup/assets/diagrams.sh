#!/usr/bin/env bash
# Draws every design diagram from its text source, in standard notations:
#   - C4 (context, containers, components, deployment): one model, c4/workspace.dsl (Structurizr DSL),
#     exported by the Structurizr CLI in Structurizr's own look (the type under every name: [Person], [Container: Java]),
#     then drawn by PlantUML; c4/views.txt says where each view's SVG goes;
#   - everything else (UML sequence, UML activity, ER, DFD): the .puml file next to its .svg.
#
#   ./diagrams.sh            draw everything
#   ./diagrams.sh foo.puml   draw one PlantUML file
#
# Needs Java 17+ and two free tools in $DIAGRAM_TOOLS (default ~/Desktop/TechProducts/tools):
#   plantuml-<version>.jar and structurizr-cli/ and, for the best layout, Graphviz (`brew install graphviz`); without it, PlantUML's built-in layouts.
set -euo pipefail

dir="$(cd "$(dirname "$0")" && pwd)"
tools="${DIAGRAM_TOOLS:-$HOME/Desktop/TechProducts/tools}"
plantuml="${PLANTUML_JAR:-$(ls "$tools"/plantuml-*.jar 2>/dev/null | sort | tail -1)}"
structurizr="${STRUCTURIZR_CLI:-$tools/structurizr-cli/structurizr.sh}"
[ -f "$plantuml" ] || { echo "PlantUML not found in $tools (set DIAGRAM_TOOLS or PLANTUML_JAR)" >&2; exit 1; }

# Graphviz (dot) gives the best layout, with its curved lines (straight segments and "ortho" were tried on 2026-10-20 and read worse);
# without it, PlantUML's built-in ones (ELK for C4, smetana for the rest).
if command -v dot >/dev/null 2>&1; then layout=""; c4layout=""; else layout="-Playout=smetana"; c4layout="!pragma layout elk"; fi
draw() { java -Djava.awt.headless=true -jar "$plantuml" -tsvg -charset UTF-8 $layout "$@"; }

if [ $# -gt 0 ]; then draw "$@"; exit; fi

# 1. The C4 model: c4/views.txt has one "view key:path of the SVG without .svg:the Markdown with its table" per line.
if [ -s "$dir/c4/views.txt" ]; then
  [ -x "$structurizr" ] || { echo "Structurizr CLI not found at $structurizr" >&2; exit 1; }
  tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
  "$structurizr" export -w "$dir/c4/workspace.dsl" -f plantuml/structurizr -o "$tmp" >/dev/null
  grep -v '^\s*\(#\|$\)' "$dir/c4/views.txt" | while IFS= read -r line; do
    key="${line%%:*}"; target="${line#*:}"; target="${target%%:*}"
    src="$tmp/structurizr-$key.puml"
    [ -f "$src" ] || { echo "missing view: $key" >&2; exit 1; }
    # the layout chosen above; the shared legend added at the bottom (the exporter's key is a separate file)
    { sed -n '1p' "$src"; echo "$c4layout"; sed -e '1d' -e '/^@enduml/d' "$src"
      cat "$dir/c4/legend.puml"; echo '@enduml'; } > "$tmp/$key.puml"
    python3 "$dir/c4/pad-labels.py" "$tmp/$key.puml"     # room inside every box
    draw -o "$tmp/out" "$tmp/$key.puml"
    mkdir -p "$(dirname "$dir/$target")"
    cp "$tmp/out/$key.svg" "$dir/$target.svg"
    echo "drew $target.svg (C4: $key)"
  done
  # Every arrow's number and ends match the table under its drawing (c4/check-tables.py).
  "$structurizr" export -w "$dir/c4/workspace.dsl" -f json -o "$tmp/json" >/dev/null
  python3 "$dir/c4/check-tables.py" "$tmp/json/workspace.json" "$dir"
fi

# 2. Every other diagram: a .puml file next to its .svg.
find "$dir" -name '*.puml' -not -path '*/node_modules/*' -not -path "$dir/c4/*" | sort | while read -r f; do
  draw "$f"
  echo "drew ${f#$dir/}"
done
