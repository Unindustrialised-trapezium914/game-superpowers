# Smoke Test

Bundle: `game-subagent-build-loop`
Version: `1.1.0`

## Prompt

Use `game-subagent-build-loop` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: game-build-review, game-playability-verifier, using-game-superpowers
