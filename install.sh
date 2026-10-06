#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
target="$HOME/.claude/skills"
mkdir -p "$target"
for dir in "$here"/skills/*/; do
  name="$(basename "$dir")"
  dest="$target/$name"
  if [ -L "$dest" ]; then
    rm "$dest"
  elif [ -e "$dest" ] && [ ! -f "$dest/.wow" ]; then
    echo "skip $name: $dest exists and was not installed by this script"
    continue
  fi
  mkdir -p "$dest"
  sed "s|\${CLAUDE_SKILL_DIR}/\.\./\.\.|$here|g" "$dir/SKILL.md" > "$dest/SKILL.md"
  touch "$dest/.wow"
  echo "installed $name"
done
config="$HOME/.claude/wow-config.md"
if [ ! -e "$config" ]; then
  cp "$here/config.example.md" "$config"
  echo "created $config: fill it in"
fi
