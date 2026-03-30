#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_BASE="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
TARGET="$DEST_BASE/game-superpowers"
MARKER=".game-superpowers-install"

mkdir -p "$DEST_BASE"

# Migrate the legacy install shape where the package root was a single symlink to repo/skills.
if [ -L "$TARGET" ] && [ "$(readlink "$TARGET")" = "$REPO_DIR/skills" ]; then
  rm "$TARGET"
fi

if [ -e "$TARGET" ] && [ ! -d "$TARGET" ]; then
  echo "skip: $TARGET exists and is not a directory"
  exit 1
fi

mkdir -p "$TARGET"
touch "$TARGET/$MARKER"

for skill in "$REPO_DIR/skills"/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  link="$TARGET/$name"
  if [ -e "$link" ] || [ -L "$link" ]; then
    rm -rf "$link"
  fi
  ln -s "$skill" "$link"
done

for shared_dir in shared schemas; do
  link="$TARGET/$shared_dir"
  if [ -e "$link" ] || [ -L "$link" ]; then
    rm -rf "$link"
  fi
  ln -s "$REPO_DIR/$shared_dir" "$link"
done

printf 'Installed Game Superpowers into %s\n' "$TARGET"
