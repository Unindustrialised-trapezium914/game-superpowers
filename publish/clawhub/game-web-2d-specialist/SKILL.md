---
name: game-web-2d-specialist
description: Apply concrete browser 2D implementation guidance after backend selection. Use this when the project is web-first and the chosen route is 2D UI-first or 2D world-first.
license: MIT
compatibility: Claude Code and Codex. Best results with file read/write access.
metadata:
  author: game-superpowers
  version: "1.1.1"
  domain: game-development
---

# Game Web 2D Specialist

## Goal
Turn a backend decision into concrete browser 2D implementation guidance without collapsing the whole system into library fandom.

## Deliverable
Write or update `docs/game-studio/backend-implementation.md`.

## Use when
- the chosen backend profile is `web-2d-ui-first` or `web-2d-world-first`
- the project is browser-first and needs sharper implementation guidance
- the team wants a concrete 2D route without losing stack-neutral top-level planning

## Use
- `./shared/reference/backend-profiles.md`
- `./shared/reference/browser-2d-specialist.md`
- `./shared/checklists/ui-ux-hard-rules.md`

## Cover
- recommended route archetype and why
- simulation state vs presentation state split
- HUD layer decision and whether a dedicated UI layer is needed
- action-state, fail-state, and restart-state handling
- mobile and desktop input expectations
- procedural-art constraints when relevant
- top implementation risks

## Important
Be concrete about architecture patterns, layering, and tradeoffs.
Do not pretend the backend is irrelevant once the route is chosen.
