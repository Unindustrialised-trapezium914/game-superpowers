# Smoke Test

Bundle: `gsp-douyin-h5`
Version: `1.1.0`

## Prompt

Use `gsp-douyin-h5` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: gsp-feedback-design, gsp-requirements-brainstorm, gsp-ux-flow-designer, gsp-web-2d-specialist, gsp-orchestrator
