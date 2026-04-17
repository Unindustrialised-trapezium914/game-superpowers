# Smoke Test

Bundle: `gsp-scope-profile`
Version: `1.1.0`

## Prompt

Use `gsp-scope-profile` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: gsp-scope-guard, gsp-orchestrator
