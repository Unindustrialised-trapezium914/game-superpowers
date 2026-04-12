# Smoke Test

Bundle: `game-first-playable`
Version: `1.1.0`

## Prompt

Use `game-first-playable` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: game-backend-selector, game-hud-feedback-polish, game-loop-bootstrap, game-playability-verifier, game-scope-guard, game-screenshot-critic, game-ux-flow-designer, using-game-superpowers
