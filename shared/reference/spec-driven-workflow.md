# Spec-Driven Workflow

This repository supports a lightweight, repo-native planning flow inspired by OpenSpec without requiring the external CLI.

## Why this exists

Game Superpowers already has strong planning, design, and implementation skills. This workflow adds a durable file structure for teams that want requirements, specs, design, and tasks to live in the target repo instead of only in chat history.

## Core split

Keep stable capability knowledge separate from a single change package.

- `specs/`
  - long-lived capability behavior
  - readable by future humans and agents
- `changes/`
  - one change package per meaningful user-facing change
  - contains the proposal, design, task list, and spec delta for that change

Recommended shape:

```text
specs/
  combat-loop/
    spec.md
  hud-feedback/
    spec.md

changes/
  add-perfect-dodge-window/
    proposal.md
    design.md
    tasks.md
    specs/
      combat-loop/
        spec.md
```

## When to use it

Use this workflow when:
- the user explicitly asks for `requirements`, `spec`, `design`, and `tasks`
- the user references OpenSpec or spec-driven development
- the work needs durable review artifacts across sessions or teammates

Stay with normal inline Game Superpowers output when:
- the request is small and disposable
- the user wants speed over durable planning artifacts
- the repo does not need a living spec library yet

## Artifact roles

### `proposal.md`
- frame the user-facing change
- say why now, what is in scope, what is out of scope
- name affected capabilities and acceptance signals

### `specs/<capability>/spec.md`
- describe stable expected behavior
- use requirement titles plus concrete scenarios
- avoid one-off implementation notes

### `design.md`
- explain the technical and gameplay decisions for this change
- capture brownfield constraints, system flow, state model, UX, feedback, and verification strategy

### `tasks.md`
- turn the design into verifiable implementation chunks
- keep task sizing aligned with the chosen development mode
- preserve requirement and design traceability

## Naming guidance

- `change-id`: short, kebab-case, action-oriented
  - `add-perfect-dodge-window`
  - `rework-run-fail-loop`
- `capability`: stable, system-oriented
  - `combat-loop`
  - `hud-feedback`
  - `player-progression`

## Archive policy

After a change lands, keep the living specs current.

- If the project updates living specs during planning, sync the approved behavior into `specs/` before implementation or merge.
- If the project prefers change-first review, keep the delta under `changes/` until the change is accepted, then promote the final behavior into `specs/`.

Do not let `changes/` become the only place where final behavior is documented.
