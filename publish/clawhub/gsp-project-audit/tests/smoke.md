# Smoke Test

Bundle: `gsp-project-audit`
Version: `1.1.0`

## Prompt

Use `gsp-project-audit` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: gsp-architecture-maintainability-audit, gsp-audio-feedback-audit, gsp-audit-scorecard, gsp-feedback-audit, gsp-feel-audit, gsp-hud-readability-audit, gsp-live-risk-audit, gsp-mechanics-systems-audit
