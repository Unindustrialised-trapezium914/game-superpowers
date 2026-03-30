#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_BASE="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
mkdir -p "$DEST_BASE"
TARGET="$DEST_BASE/game-superpowers"
if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo "skip: $TARGET already exists"
  exit 0
fi
ln -s "$REPO_DIR/skills" "$TARGET"
printf 'Linked %s -> %s\n' "$TARGET" "$REPO_DIR/skills"
