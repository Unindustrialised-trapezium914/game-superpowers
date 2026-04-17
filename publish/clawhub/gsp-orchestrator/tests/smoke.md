# Smoke Test

Bundle: `gsp-orchestrator`
Version: `1.1.0`

## Prompt

Use `gsp-orchestrator` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: gsp-architecture-maintainability-audit, gsp-audio-feedback-audit, gsp-audit-scorecard, gsp-build-review, gsp-build-strategy, gsp-concept-brainstorm, gsp-douyin-h5, gsp-feedback-audit
