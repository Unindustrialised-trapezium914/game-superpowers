# Rolling Supervisor Architecture

Use a short-lived worker model instead of a single endlessly growing session.

## Why
- lower context rot
- simpler failure recovery
- cleaner handoffs
- easier parallelization

## Worker roles
- brainstormer
- scope planner
- architect
- builder
- verifier
- feedback designer
- repair worker

## Handoff contract
Each worker must output:
- status
- summary
- key changes
- unresolved issues
- next recommended worker
- compact handoff text

## Runtime preference
- Claude: use hooks for local automation and an external supervisor for orchestration
- Codex: use exec/SDK/MCP for machine-readable orchestration
- ACP: useful as an integration layer, but not the v1 lifecycle authority
