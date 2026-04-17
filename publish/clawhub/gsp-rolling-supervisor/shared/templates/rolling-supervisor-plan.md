# Rolling Supervisor Plan

## Objective
- target quality:
- definition of done:

## Worker graph
- brainstorm -> scope -> planner -> builder -> verifier -> feedback -> verifier

## Worker contracts
- each worker writes a handoff summary
- each worker returns a structured result
- supervisor destroys the worker process after each turn

## Context policy
- max handoff size:
- summarize when over budget:
- always reload project rules from docs/game-studio and CLAUDE.md or AGENTS.md

## Safety policy
- never run infinite stop-hook loops
- prefer short-lived processes over persistent uncontrolled sessions
- isolate parallel branches with git worktrees when available
