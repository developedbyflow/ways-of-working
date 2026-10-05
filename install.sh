#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
target="$HOME/.claude/skills"
mkdir -p "$target"
for dir in "$here"/skills/*/; do
  name="$(basename "$dir")"
  link="$target/$name"
  if [ -e "$link" ] && [ ! -L "$link" ]; then
    echo "skip $name: $link exists and is not a link"
    continue
  fi
  ln -sfn "${dir%/}" "$link"
  echo "linked $name"
done
