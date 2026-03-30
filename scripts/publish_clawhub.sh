#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUBLISH_DIR="$REPO_DIR/publish"
CHANGELOG_TEXT="${1:-Initial Game Superpowers ClawHub publish.}"

python3 "$REPO_DIR/scripts/generate_clawhub_bundles.py"
clawhub --workdir "$PUBLISH_DIR" --dir clawhub sync --all --changelog "$CHANGELOG_TEXT"
