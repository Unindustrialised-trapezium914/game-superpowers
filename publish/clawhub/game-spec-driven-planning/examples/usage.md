# Usage Examples

## Example prompts

- Use `game-spec-driven-planning` and create `requirements/spec/design/tasks` artifacts for this combat feature.
- Apply `game-spec-driven-planning` to this brownfield game repo and produce a durable change package for the HUD overhaul.
- Use `game-spec-driven-planning` with Game Superpowers so this change leaves behind repo-native planning artifacts.

## Expected behavior

- Load the skill instructions from `SKILL.md`.
- Use the packaged `shared/` references and templates when the skill body points to them.
- Preserve the split between living `specs/` and per-change `changes/`.
- If the workflow calls for companion skills, tell the user which companion skills should be installed or invoked next.
