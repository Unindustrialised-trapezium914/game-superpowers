---
name: game-requirements-brainstorm
description: Use when the request is vague, contradictory, or too under-specified to build a strong game result. Turn the request into a concise production-ready requirement brief without getting stuck in endless ideation.
license: MIT
compatibility: Claude Code and Codex. Best results with file read/write access.
metadata:
  author: game-superpowers
  version: "1.1.0"
  domain: game-development
---

# Game Requirements Brainstorm

## Goal
Help the user reach a requirement set that is specific enough to build a strong result.
This is not open-ended ideation for its own sake. It is requirement sharpening.

## Deliverables
- `docs/game-studio/requirements.md`
- `docs/game-studio/quality-target.md`

Use:
- `../../shared/templates/requirements-brief.md`
- `../../shared/templates/quality-target.md`

## Workflow
1. Extract what the user definitely wants.
2. Separate:
   - must-build features
   - must-not-cut qualities
   - optional features
   - explicit non-goals
3. Infer smart defaults when they are obvious.
4. Ask at most a few decisive questions only if they materially affect backend choice, scope completeness, or risk.
5. Write acceptance tests in user language.
6. Decide whether the quality target should be `first-playable`, `polished-prototype`, `production-feature`, or `live-patch`.

## Important
If the request is greenfield and the user wants a strong showcase result, do **not** automatically reduce the ask to a bare minimum.
Instead, protect the features and qualities that define the fantasy and the “wow.”
