# AGENTS.md

This repository is the **skills-first** source of truth for Game Superpowers.

## Repo conventions

- `skills/` contains the reusable Game Superpowers skills
- `schemas/` contains structured output schemas used across the collection
- `shared/` contains checklists, templates, and reference material
- `.claude/skills/` and `.agents/skills/` exist for host-native skill discovery

## Editing policy

When changing a skill:
1. Keep the skill focused on one job
2. Keep `name` aligned with the folder name
3. Keep `description` specific enough for implicit invocation
4. Prefer routing improvements over bloating a single skill
5. Preserve the build track / audit track split

## Collection entrypoint

If you need a top-level collection skill, use `gsp-orchestrator`.
