# Smoke Test

Bundle: `gsp-spec-driven-planning`
Version: `1.0.0`

## Prompt

Use `gsp-spec-driven-planning` on a fitting game-development task.

## Expected checks

- The agent recognizes that the workflow is optional and only applies when durable artifacts are wanted.
- The agent preserves the split between `specs/` and `changes/`.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- Companion skills referenced in this bundle: gsp-orchestrator, gsp-requirements-brainstorm, gsp-implementation-plan
