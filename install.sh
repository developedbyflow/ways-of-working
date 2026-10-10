#!/usr/bin/env bash
# Links every skill in skills/ into ~/.claude/skills, so an edit in this repo applies right away.
#   ./install.sh           link all skills, and remove links to skills that no longer exist
#   ./install.sh --remove  remove every link that points into this repo
# CLAUDE_SKILLS_DIR overrides the target folder.
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
target="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$target"

# Links into this repo, whatever their name.
for link in "$target"/*; do
  [ -L "$link" ] || continue
  dest="$(readlink "$link")"
  case "$dest" in "$repo"/skills/*) ;; *) continue ;; esac
  if [ "${1:-}" = "--remove" ] || [ ! -d "$dest" ]; then
    rm "$link"
    echo "removed $(basename "$link")"
  fi
done
[ "${1:-}" = "--remove" ] && exit 0

for dir in "$repo"/skills/*/; do
  name="$(basename "$dir")"
  link="$target/$name"
  if [ -e "$link" ] && [ ! -L "$link" ]; then
    echo "skipped $name: $link exists and is not a link" >&2
    continue
  fi
  ln -sfn "${dir%/}" "$link"
  echo "linked $name"
done
