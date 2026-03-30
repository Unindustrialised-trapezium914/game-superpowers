# Polished Prototype Rubric

Use this when the target is `polished-prototype`.
A polished prototype should feel intentionally built, not merely technically playable.

## Completeness gates
- All user-requested core features in scope are present
- Basic menu / start / pause / retry flow exists
- Win, loss, or session-resolution states are implemented where relevant
- The build is coherent enough for external demo or evaluation

## UX / feel gates
- First 30 seconds communicate the fantasy quickly
- HUD hierarchy is clear
- Controls feel deliberate rather than placeholder
- Failure and reward feedback are strong enough to shape play
- The build does not feel obviously unfinished in its critical path

## Visual gates
- Visual direction is coherent
- Procedural art, shader, particle, or UI recipe choices support the requested style
- Important objects and states are readable
- The game looks “good enough” for the promised prototype bar

## Engineering gates
- Core systems are organized and maintainable
- No core-path TODO stubs
- No fragile copy-pasted subsystems in critical logic
- Main flows can be rerun without manual cleanup

## Verdict
- **PASS** — strong prototype / demo quality
- **REPAIR** — feature or feel gaps remain
- **REPLAN** — target is mismatched with scope or strategy
