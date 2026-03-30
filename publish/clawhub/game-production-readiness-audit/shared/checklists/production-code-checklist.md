# Production Code Checklist

Use this checklist unless the user explicitly asks for a disposable spike.

## Code quality
- Clear ownership of state and side effects
- Strong typing or equivalent guardrails where the stack supports it
- No core-path placeholder TODOs or fake implementations
- No silent global mutation without an explicit state owner
- No duplicated logic when a shared abstraction is clearly warranted

## Runtime quality
- Deterministic enough to debug
- Errors surfaced clearly
- No obvious crash paths in normal play
- No obvious resource leaks in the main loop

## Architecture quality
- Game-native abstractions are explicit
- Managers / controllers / state machines have clear boundaries
- UI state and simulation state are separated cleanly enough
- Data flow is understandable to another developer

## Delivery quality
- Build and run instructions still work
- Verification or sanity checks exist where practical
- If refactoring, compatibility and rollback concerns are documented
