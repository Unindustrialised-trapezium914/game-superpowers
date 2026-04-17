# Browser 2D Specialist Reference

Use this reference when the chosen backend profile is `web-2d-ui-first` or `web-2d-world-first`.

## Suitable routes
Examples of good routes include:
- scene-driven 2D framework plus DOM overlay HUD
- lightweight render loop plus separate UI shell
- canvas-first action game with explicit game-state layer and thin presentation layer

Do not lock on a library just because it is popular. Choose the route that best fits the requested interaction style and quality target.

## Strong default patterns
- Keep simulation state separate from rendering state.
- Treat HUD and overlays as their own layer with explicit visibility, priority, and pause behavior.
- Prefer DOM or an equivalent dedicated UI layer when text-heavy menus, settings, inventory, or accessibility matter.
- Prefer world-first rendering patterns when the brief is action-heavy, arcade-heavy, puzzle-heavy, or relies on moment-to-moment spatial play.

## Input guidance
- Define keyboard, gamepad, mouse, and touch behavior explicitly.
- Lock the primary verb and restart flow early.
- On mobile, define safe-area and thumb-zone constraints before polishing secondary controls.

## Asset and feedback guidance
- Use lightweight assets and clear feedback before overinvesting in polish.
- If procedural art is requested, define which pieces are SVG, shader-driven, particle-driven, or conventional.
- Separate “world feedback” from “HUD confirmation” so the player gets both readability and feel.

## Acceptance checks
- The first actionable state is fast and obvious.
- HUD does not choke the playfield.
- Restart / fail / success loops are easy to understand.
- The chosen route still looks maintainable after expansion.
