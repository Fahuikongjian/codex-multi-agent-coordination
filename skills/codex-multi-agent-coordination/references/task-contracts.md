# Task, Result, and Decision Templates

Trim fields to fit the assignment. These are cooperation conventions, not a built-in Codex schema or tool arguments.

## Delegation message

```text
Task: T2; assignment_epoch: 1
Role: implementer; recipient: main coordinator
Goal: implement request timeouts against agreed interface D1.
Exclusions: no new HTTP library, return-schema change, or unrelated refactor.
Input baseline: current client.ts snapshot and D1.
Writable: src/network/client.ts and tests/network/client.test.ts.
Read-only: src/network/types.ts, package.json, and all other files.
Exclusive resources: work/T2/; no shared Git-index operations.
Dependencies: D1 is settled; propose shared-type changes to the coordinator.
Acceptance: use existing TimeoutError; preserve cancellation; run relevant checks.
Stop: submit and stop writing when done. Pause only affected work if a
contract change or another owner's resource is needed.
Authority: no nested agents, peer reassignment, or external publication.
Return: T2/epoch=1, changed files, behavior, actual checks/results, limits.
```

Include essential constraints directly, not just "follow the global plan." A linked ledger must be accessible in the child's workspace. For separate worktrees, copy necessary input or supply relevant content. Full-history inheritance does not replace a clear contract.

The example does not require a particular module layout, extra tests, or new approval gates. Replace example paths and checks with actual task needs.

## Minimal coordinator ledger

```markdown
# Current coordination
User outcome: add request timeouts while preserving the existing API.
Baseline: actual commit plus relevant uncommitted files or snapshot.
Coordinator/integration owner: main agent.

| task | epoch | owner | writable scope | dependency | acceptance | state |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | 1 | main | types.ts | none | preserve API; settle timeout contract | accepted |
| T2 | 1 | worker-a | client.ts and its tests | D1 | timeout/cancellation checks | running |
| T3 | 1 | worker-b | usage documentation | D1 | examples follow agreed API | running |
| R1 | 1 | reviewer | none; read-only | T2/T3 submitted | review stable snapshot | planned |

Shared resources: main owns Git index, dependency lockfiles, and final build.
D1: retain TimeoutError; reopen for compatibility failures or changed requirements.
```

Replace abbreviated filenames with unambiguous paths. Add workspace roots, resource instances, and actual agent IDs as needed. Identical relative paths in separate checkouts are different files; aliases of the same real directory are not isolation.

Useful states: `planned -> running -> submitted -> accepted`, with `blocked` or `cancelled` when applicable. `submitted` means writing has stopped; `accepted` means the coordinator checked and accepted the result. Increment only the affected task's epoch, not every unrelated ledger update.

## Dependency or disagreement report

```text
T2/epoch=1 - decision needed
Fact: TimeoutError has no cause parameter; verified in types.ts.
Impact: timeout implementation can proceed, but tracing would be limited.
Evidence: file location or minimal reproduction.
Proposal: keep the structure; ask the T1 owner to extend it if tracing is required.
Current action: continue independent work; do not modify types.ts.
Requested action: coordinator decides whether scope should change.
```

If direct agent messaging is unavailable or unauthorized, use the allowed parent-reporting mechanism. Coordination does not authorize bypassing communication boundaries or creating user chats.

## Completion report

```text
T2/epoch=1 - submitted; writing stopped
Baseline: actual input version; disclose relevant changes during execution.
Result: timeouts use TimeoutError; caller cancellation keeps its behavior.
Artifacts: actual paths; add branch/commit only for a separate worktree.
Changes: this task's files, not every uncommitted shared-checkout file.
Verification: actual commands, exit status, and key results; identify checks not run.
Limits: none, or specific incomplete work and its reason.
```

## Decision and reopening conditions

```text
D2 - affects T2 and T3
Issue: whether the error structure gains a field.
Evidence: user requires API compatibility; caller checks cover the schema.
Decision: preserve the structure; tracing fields are outside this task.
Next: T2 continues; T3 uses the same interface.
Reopen: reproducible evidence of failure against an explicit requirement,
or a user requirement change.
```

A decision record preserves its basis; coordinator preference cannot outrank user requirements or failure evidence.
