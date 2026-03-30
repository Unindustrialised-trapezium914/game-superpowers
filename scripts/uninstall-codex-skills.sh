#!/usr/bin/env bash
set -euo pipefail
DEST_BASE="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
TARGET="$DEST_BASE/game-superpowers"
if [ -L "$TARGET" ]; then
  rm "$TARGET"
  printf 'Removed %s\n' "$TARGET"
else
  echo "nothing to remove: $TARGET"
fi
