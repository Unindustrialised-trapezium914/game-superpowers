---
name: game-super-build
description: "Use when orchestrating serious game work across concept, scope, build mode, quality target, and downstream routing."
---

# Game Super Build

Lead game-production workflow. Choose the right strategy for project state and quality target instead of just producing the smallest thing that runs.

## Outputs

Follow the `using-game-superpowers` output strategy:
- **inline** (default): keep all findings, plans, and decisions in conversation. Do not create `docs/` files.
- **minimal**: write only `plan.md` and `quality-target.md` for cross-session continuity.
- **full**: create or update the relevant `docs/game-studio/` records for project state, concept, requirements, scope, build strategy, backend, UX, feedback, architecture, plan, quality, and release safety.

## Phase map
1. **Classify**
   - Detect build, audit, or both.
   - Existing repo inspection routes to `game-project-audit` first.
   - Assess project state with `game-project-state-assessment`.
2. **Lock the brief**
   - Use `game-concept-brainstorm` when the request is vague, weakly differentiated, archetype-ambiguous, or a one-prompt showcase build.
   - Use `game-requirements-brainstorm`.
   - Use `game-scope-profile`.
   - Use `game-build-strategy`.
3. **Choose implementation route**
   - Use `game-backend-selector`.
   - Route explicit Douyin H5 delivery through `game-douyin-h5` before deeper browser specialization.
   - Route chosen web 2D or browser 3D profiles to the matching specialist skill.
4. **Design the product**
   - Use `game-ux-flow-designer`, `game-feedback-design`, and `game-mechanics-systems-design`.
   - Use `game-production-code` when the quality target needs product-grade implementation standards.
5. **Execute and verify**
   - Use `game-implementation-plan`.
   - If subagents are available and the target is above throwaway-spike quality, prefer `game-subagent-build-loop`.
   - Review and verify with `game-build-review`, `game-playability-verifier`, and `game-screenshot-critic`.
6. **Escalate only when justified**
   - Use compare or rolling-supervisor modes only when the task size or uncertainty warrants them.

## Important
For browser games, stack-neutral does not mean implementation-vague.
Do not confuse fewer questions with better workflow.
