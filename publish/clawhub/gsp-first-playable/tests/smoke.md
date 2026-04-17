# Smoke Test

Bundle: `gsp-first-playable`
Version: `1.1.0`

## Prompt

Use `gsp-first-playable` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: gsp-backend-selector, gsp-hud-feedback-polish, gsp-loop-bootstrap, gsp-playability-verifier, gsp-scope-guard, gsp-screenshot-critic, gsp-ux-flow-designer, gsp-orchestrator
