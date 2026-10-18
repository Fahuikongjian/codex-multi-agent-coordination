# Conflict Recovery and Safe Handoffs

Read for overlapping writes, repeated reversals, requirement changes, or takeover. Local disagreements should not freeze unrelated work.

## Multiple agents touch one resource

1. Freeze overlapping writes and continue independent work. Preserve current edits and evidence rather than first reverting to a clean tree.
2. Inspect real paths, agent states, and unfinished commands. Distinguish user edits, other tasks, and current work; a Git diff does not establish authorship.
3. Appoint one writer. Others submit read-only proposals or wait for verified transfer.
4. Inspect necessary contributions, integrate minimally, and check a stable result.

In a shared checkout, do not let children run repository-wide staging, checkout, reset, stash, cleanup, or formatting. Assign these operations explicitly. Local commits in separate worktrees are acceptable when their contracts permit them. Never undo others' work merely to reclaim scope.

## Revocation, reassignment, or takeover

Use "stop -> verify -> inspect -> issue new contract":

```text
Coordinator -> old owner: revoke T2/epoch=1 writes; stop operations and
report last artifacts and unfinished processes.
Old owner -> coordinator: stopped; report artifacts, tools, and spawned processes.
Coordinator: verify runtime/process state, inspect files, retire the old epoch.
Coordinator -> new owner: T2/epoch=2 with current baseline, scope, acceptance,
and stopping condition.
```

An acknowledgement must account for builds, generators, services, and other writers it started. Interrupts may wait for tool completion. Timeouts do not release ownership. If neither acknowledgement nor runtime state establishes stopping, freeze the resource. Work on truly isolated candidates or read-only analysis if useful; integration still requires safe access to the original.

An epoch is a cooperation invalidation marker, not operating-system fencing. If an agent or process ignores the protocol, use actual isolation or stop it. Incrementing a number does not stop an old process.

## Requirement changes

Identify affected tasks and interfaces; stop only their scope. Keep valid independent tasks. Update affected decisions and contracts, increment materially changed task epochs, and verify old work has stopped before resuming writes. Preserve late old results as evidence requiring validation against current requirements before adoption.

## Implementer and reviewer disagree

Ask each side for one useful factual contribution: requirement, observed behavior, reproduction, or check result. Decide from evidence, preferably using a small discriminating test.

- **Correctness defect:** assign and verify a concrete repair, even after earlier acceptance.
- **Requirement ambiguity:** decide from the goal; ask the user only about material choices that cannot reasonably be inferred.
- **Preference:** retain the convention or implementation, label the suggestion optional, and close the issue.

The reviewer does not concurrently edit the implementer's file. Do not require unlimited rounds until all agents agree. Recheck affected behavior and necessary integration after a fix; expand checks only for a new change or risk.

## Dependency cycles and slow workers

Identify who waits for which observable artifact. If two tasks wait on each other, assign one owner to settle the minimal interface or serialize prerequisites, then resume useful parallelism. Adding another global planner does not resolve the original cycle.

Inspect real status before treating a slow worker as failed. Do not commission a duplicate race. Replacements require verified handoffs. Submitted tasks should not continue open-ended optimization.

## Resume a long or compacted session

Recover from the latest user request, concise ledger, actual files, and runtime state. Verify agent IDs, epochs, unfinished commands, baselines, and dependencies before spawning replacements. Cross-check ledgers and agent reports against artifacts.
