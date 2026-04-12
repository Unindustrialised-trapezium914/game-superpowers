---
name: game-feedback-design
description: "Use when designing a game's visual, motion, audio, or UI feedback grammar."
---

# Game Feedback Design

## Goal
Make feedback part of the design, not something bolted on at the end.

## Outputs

Follow the `using-game-superpowers` output strategy:
- **inline** (default): present feedback design in conversation.
- **minimal** or **full**: write `docs/game-studio/feedback-design.md`.

Use:
- `./shared/templates/feedback-design.md`
- `./shared/checklists/feedback-design-checklist.md`
- `./shared/checklists/game-feel-pillars.md`
- `./shared/checklists/ui-ux-hard-rules.md`

## Cover
- input acknowledgment
- success / reward signals
- fail / deny signals
- danger telegraphing
- state transition feedback
- audio priorities
- micro-motion and juice that support clarity rather than noise
- which feedback belongs in the world layer vs the HUD layer

## Use when
- the build works but feels dead
- the target is `polished-prototype` or above
- combat, traversal, collection, menuing, or puzzle interactions need stronger feel

## Important
Feedback is part of the mechanic contract.
If the game does not communicate clearly or feel responsive, it is not “done enough.”
