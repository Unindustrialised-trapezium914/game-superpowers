# Game Superpowers v1.2.0 — Skills-Only Release

This release formalizes the project as a **skills-first** open-source system for Claude Code and Codex.

## What changed

- Reframed the repository around **skills** instead of plugins
- Added `using-game-superpowers` as the collection bootstrap skill
- Rewrote installation docs for native Claude and Codex skills flows
- Added scripts for Claude and Codex skills installation / uninstall
- Reorganized open-source documentation around build track + audit track

## Why this matters

The value of Game Superpowers lives in:
- game-specific workflow logic
- UI/UX and feedback-aware routing
- project-state-aware build and audit flows
- reusable skills that remain easy to fork and remix

Shipping the repository as a skills collection makes it easier to:
- use locally
- contribute to
- customize for a team or project
- keep cross-host compatible

## Highlights

- skills-first distribution
- build track and audit track
- collection bootstrap skill
- Claude-friendly `--add-dir` flow
- Codex-friendly symlink flow

## Notes

Downstream plugin packaging remains possible, but it is no longer the source of truth for this project.
