# First-Playable Rubric

A first playable is a **specific quality target**, not the universal end state for every game request.
Use this rubric only when the chosen target is `first-playable`.

## Hard gates
- Boots without blocking errors
- Reaches an actionable screen quickly
- Main input works
- Primary verb is executable
- One fail or end condition exists
- Retry / restart path exists
- HUD or affordances are readable enough to play

## UX gates
- The first 30 seconds are understandable
- The camera / framing supports the main action
- Critical information is visible without hunting
- Menus and overlays do not block the playfield unnecessarily
- Feedback exists for success, failure, and invalid actions

## Feel gates
- The game does not feel dead
- Input has visible or audible response
- Motion or timing communicates impact
- Effects are legible, not noisy

## Engineering gates
- No obvious console spam
- No crash loop
- No unbounded state growth during short playtests
- The architecture is minimal but not chaotic

## Verdict
- **PASS** — playable and worth further development
- **NEEDS REPAIR** — close, but one or more hard gates fail
- **REPLAN** — current scope or backend choice is fighting the target
