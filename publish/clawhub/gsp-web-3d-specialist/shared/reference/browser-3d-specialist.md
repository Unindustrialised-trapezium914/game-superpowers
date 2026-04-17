# Browser 3D Specialist Reference

Use this reference when the chosen backend profile is `web-3d-preview` or another browser-3D-oriented route.

## Suitable routes
Examples of good routes include:
- lightweight browser 3D scene graph with DOM HUD
- hybrid UI shell plus 3D playfield / preview scene
- stylized 3D route with strict scope control and explicit performance budgets

## Strong default patterns
- Keep camera state, simulation state, and menu state explicit and separate.
- Use DOM or an equivalent dedicated UI layer for text-heavy menus, overlays, settings, and accessibility.
- Treat pointer lock, free-look, drag camera, and menu focus as mutually coordinated states.
- Protect the playfield and readability before layering decorative HUD.

## Performance guidance
- Set a performance budget early.
- Avoid overcommitting to heavy assets, post effects, and visual density before the first strong loop is proven.
- Prefer predictable scene complexity and controlled feedback over uncontrolled spectacle.

## Interaction guidance
- Define how camera, movement, aim, pause, inventory, and modal states hand off control.
- Escape / menu open / menu close must never strand the player in a broken focus state.
- For hybrid games, keep 3D spectacle from drowning out actionable UI.

## Acceptance checks
- Camera and menu states do not fight.
- The first playable sequence is legible and controllable.
- HUD and overlays remain readable over 3D motion.
- The route is still realistic for the requested scope and quality target.
