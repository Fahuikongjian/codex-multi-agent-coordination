---
name: codex-multi-agent-coordination
description: "Coordinate Codex subagents working on one task with explicit ownership, bounded delegation, evidence-based decisions, and safe handoffs. Use for multi-agent implementation or review, overlapping edits, duplicate work, stale results, or agents repeatedly overturning one another. Do not activate for ordinary single-agent work or merely to create separate user chats."
---

# Codex Multi-Agent Coordination

Keep agents working toward one deliverable. The main agent owns the goal, boundaries, decisions, and integration. Subagents deliver bounded results with evidence, retaining independent judgment within their assignments.

This is a cooperation protocol, not a file lock or sandbox. Actual permissions, higher-priority instructions, and user requirements still apply. Delegation does not grant additional authority to send, publish, delete, or change configuration.

## Identify your role

- **Main agent:** Divide, delegate, resolve, integrate, and deliver. Spawn subagents only when independent work exists, tools are available, and current instructions permit delegation.
- **Subagent:** Follow your contract and write only within its scope. Do not re-plan the entire assignment, take over coordination, direct peers, or spawn further agents without an explicit delegation grant. Report missing contract details and continue unaffected work.
- **No subagent tools:** Complete work in dependency order and disclose sequential execution. Do not substitute user-chat creation, nested CLI sessions, or invented calls.

For an unfamiliar runtime, read [references/codex-tools.md](references/codex-tools.md) as needed. Use the tools and parameters actually exposed in the current session.

## 1. Delegate independently deliverable work

Establish the requested outcome, behavior to preserve, and acceptance evidence as the current baseline. Parallel work does not require a full repository survey.

Prefer independent files or modules, read-only investigation, and review against a fixed snapshot. If tasks depend heavily on the same interface, assign one owner to settle it before parallelizing downstream work. Serialize strong dependencies instead of commissioning competing complete implementations.

Use the fewest agents that provide a useful benefit, within runtime limits. The coordinator may advance its own independent work, but should not duplicate delegated tasks. Assign competing solutions only when comparison is part of the requested task.

## 2. Define a contract before delegation

Identify these fields for each task:

- `task_id`, `assignment_epoch`, owner, and recipient. Increment the task's epoch when reassigning it or materially changing its contract.
- Goal, exclusions, input baseline or snapshot, and settled interfaces or decisions.
- Writable files or directories and exclusive resources. Without write permission, the assignment is read-only. The coordinator also respects ownership.
- Dependencies, verifiable acceptance criteria, stopping condition, and return format.

For a simple task, put the contract in its delegation message. With multiple writers, changing interfaces, or repeated handoffs, keep a small coordinator-owned ledger in an allowed scratch location, such as `work/coordination.md`. Subagents propose ledger changes through messages. Do not introduce a framework or configuration for a small assignment.

Read [references/task-contracts.md](references/task-contracts.md) when preparing messages and use only relevant templates. Limit each role to its subtask unless further delegation is explicitly granted.

## 3. Assign write ownership before parallel execution

**At any moment, each file or shared mutable resource has one write owner.** Resolve actual paths and resource identities; directory ownership includes descendants. Aliases, symlinks, or case differences must not conceal overlapping access.

- **Shared checkout:** Partition files. If several agents need the same file, appoint one writer and have others submit proposals or patch text, or transfer ownership between verified quiet stages.
- **Separate worktrees:** Record baseline, branch, and integration owner. File isolation does not isolate shared databases, ports, caches, or external services, and does not resolve interface disagreements. Uncommitted input is not automatically copied.
- Assign owners for dependency lockfiles, shared types, export entrypoints, repository-wide formatting, generated output, the Git index, and branch operations. Commands must respect ownership. Tests that generate files or change shared state are also writers.

For takeover, revocation, or resource conflicts, read [references/conflict-recovery.md](references/conflict-recovery.md). **A stop message, interrupt request, or timeout does not establish that the old writer has stopped.** Verify the agent and its tools or processes are no longer writing, inspect current state, then release ownership and issue the new epoch. If stopping cannot be verified, freeze the affected resource and continue independent work.

## 4. Exchange facts and assign decisions

Prefix messages with `task_id + assignment_epoch`. State the fact, impact, evidence, and requested action. Completion reports include artifact locations, actual changes, executed checks, and unresolved limits, rather than an internal reasoning transcript.

Subagents decide implementation details within their contracts. Changes to an interface, another owner's files, acceptance criteria, or the overall approach require a coordinator proposal before writing. Allowed peer communication exchanges facts; it cannot reassign tasks or expand permission.

For a disagreement, the coordinator should:

1. Distinguish a **reproducible defect, requirement ambiguity, or implementation preference**. Observable failure and explicit requirements outrank preference.
2. Collect one useful round of necessary evidence. Run a small discriminating check when possible, instead of polling agents or extending debate indefinitely.
3. Decide within existing authorization; record reason, affected scope, and reopening conditions; notify only affected agents.

Keep a settled approach when no new evidence exists. A new reproduction, failed check, changed constraint, or user correction may reopen it; a previous decision cannot excuse a real defect. Ask the user only about material goals, permissions, or choices that cannot reasonably be inferred.

## 5. Integrate submitted results

Subagents stop writing when submitting a completed assignment and wait for an explicit new contract. Reviewers are read-only by default, use the agreed baseline and criteria, and report location, trigger, and impact. Label style preferences as optional rather than adding acceptance gates.

Before accepting a result, verify task, epoch, input version, and actual artifacts. Old-epoch results are evidence requiring revalidation, not permission to overwrite current work. Shared-checkout edits already exist in place; do not apply their patches twice. Integrate separate-worktree commits according to the project workflow. Arrival order does not select the winning version.

Perform final review after the affected scope is stable or has an explicit snapshot. Concurrent reviews are preliminary findings about their observed version. Assign bounded fixes to the existing owner, or complete a verified handoff before another writer takes over. Do not restart full review without a new change, failure, or unresolved concern.

## 6. Converge on the user's outcome

Wait with bounds and use available time for independent work. Avoid frequent polling; do not interpret silence as failure or completion. Resolve dependencies, narrow a contract, or serialize work before commissioning duplicate efforts.

Before delivery, confirm required tasks are accepted or explicitly blocked; relevant agents and tools have stopped affecting final artifacts; and the integrated version satisfies agreed acceptance. Report only executed checks.

The main agent returns one coherent outcome with completed work, verification, and real limits. Preserve unresolved evidence without replaying every settled debate. A division-of-work table, collection of reports, or unintegrated alternatives is not a finished deliverable.
