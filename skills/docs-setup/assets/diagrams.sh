#!/usr/bin/env bash
# Draws every design diagram from its text source, in standard notations:
#   - C4 (context, containers, components, deployment): one model, c4/workspace.dsl (Structurizr DSL),
#     exported by the Structurizr CLI to C4-PlantUML, then drawn by PlantUML; c4/views.txt says where each view's SVG goes;
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

# Graphviz (dot) gives the best layout, with straight segments for C4 (its curves are the default; "ortho" puts the labels over the boxes);
# without it, PlantUML's built-in ones (ELK for C4, smetana for the rest).
if command -v dot >/dev/null 2>&1; then layout=""; c4layout="skinparam linetype polyline"; else layout="-Playout=smetana"; c4layout="!pragma layout elk"; fi
draw() { java -Djava.awt.headless=true -jar "$plantuml" -tsvg -charset UTF-8 $layout "$@"; }

if [ $# -gt 0 ]; then draw "$@"; exit; fi

# 1. The C4 model: c4/views.txt has one "view key:path of the SVG without .svg" per line.
if [ -s "$dir/c4/views.txt" ]; then
  [ -x "$structurizr" ] || { echo "Structurizr CLI not found at $structurizr" >&2; exit 1; }
  tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
  "$structurizr" export -w "$dir/c4/workspace.dsl" -f plantuml/c4plantuml -o "$tmp" >/dev/null
  grep -v '^\s*\(#\|$\)' "$dir/c4/views.txt" | while IFS= read -r line; do
    key="${line%%:*}"; target="${line#*:}"
    src="$tmp/structurizr-$key.puml"
    [ -f "$src" ] || { echo "missing view: $key" >&2; exit 1; }
    # the layout chosen above; the shared legend instead of the exporter's
    { sed -n '1p' "$src"; echo "$c4layout"; echo 'skinparam ArrowThickness 1.6'; echo 'skinparam defaultTextAlignment center'; sed -e '1d' -e '/^SHOW_LEGEND/d' -e '/^@enduml/d' "$src"
      cat "$dir/c4/legend.puml"; echo '@enduml'; } > "$tmp/$key.puml"
    draw -o "$tmp/out" "$tmp/$key.puml"
    mkdir -p "$(dirname "$dir/$target")"
    cp "$tmp/out/$key.svg" "$dir/$target.svg"
    echo "drew $target.svg (C4: $key)"
  done
fi

# 2. Every other diagram: a .puml file next to its .svg.
find "$dir" -name '*.puml' -not -path '*/node_modules/*' -not -path "$dir/c4/*" | sort | while read -r f; do
  draw "$f"
  echo "drew ${f#$dir/}"
done
