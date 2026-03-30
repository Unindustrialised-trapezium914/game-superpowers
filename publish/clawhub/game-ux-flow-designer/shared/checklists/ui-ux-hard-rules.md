# UI/UX Hard Rules

Use these rules whenever a game has meaningful UI, onboarding, HUD, or menu flow.

## Playfield protection
- Protect the playfield first. Overlay UI must not hide the primary action area without a strong reason.
- If the game relies on spatial reading, reserve clear central sightlines and avoid permanent clutter in the middle third.
- Use backing, contrast, or placement changes when text sits over a moving or noisy world.

## First actionable state
- The player should reach an actionable state quickly.
- The first meaningful verb should be visible and understandable before secondary systems expand.
- If onboarding exists, it should support the first verb rather than block it behind too much text.

## Persistent HUD budget
- Treat permanent HUD as a budget, not a wishlist.
- Persistent HUD should show only the information needed for the next few seconds of decision making.
- Nice-to-have stats belong in pause, drawer, map, inventory, or secondary screens.

## DOM vs canvas / scene UI
- For browser projects, use a separate UI layer when text density, accessibility, layout complexity, or responsive behavior matter.
- Keep game simulation state independent from whichever view layer renders the HUD.
- Do not make the game core depend on a specific HUD implementation.

## Input and control conflicts
- Menus, pause states, pointer lock, camera control, and gameplay input must have explicit ownership.
- A paused or menu-focused state should never accidentally keep combat or camera input active.
- Escape / pause / close interactions must return the player to a sane state.

## Mobile and safe-area rules
- Respect safe areas, notches, and gesture zones.
- Avoid placing critical primary actions outside comfortable thumb zones on portrait mobile unless the game specifically demands it.
- One-handed pressure should be considered when the product is portrait or casual-mobile oriented.

## Feedback clarity
- Every important action needs acknowledgment.
- Dangerous states need telegraphing before punishment.
- Success, failure, denial, and cooldown should look and sound distinct.

## Audit note
- If runtime evidence is unavailable, distinguish confirmed issues from inferred risks.
