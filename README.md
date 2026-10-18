# Codex Multi-Agent Coordination

A Codex skill for agents working toward one deliverable. It reduces duplicate work, overlapping edits, review ping-pong, and obsolete results overriding current requirements.

Use it for multi-agent implementation, review, or conflict recovery. Small tasks can stay single-agent. All instructions, display metadata, prompts, and documentation are in English. No particular model or operating system is required.

## Problems addressed

| Problem | Coordination mechanism |
| --- | --- |
| Several agents redo the whole task | One coordinator and bounded subtasks |
| Multiple writers edit one file | One owner, proposals from others, verified handoffs |
| Review keeps reversing decisions | Evidence and explicit reopening conditions |
| Old results conflict with changed requirements | Task epochs and baseline validation |
| Replacement starts before the old writer stops | Verify agent, tool, and process quiescence |
| Worktrees collide on ports or databases | Shared-resource ownership as well as file ownership |
| Reports never become a finished result | Integrate artifacts and check the final version |

This is a cooperation protocol. It does not enforce filesystem locks or guarantee obedience. Concurrent writes still need actual isolation and state checks.

## Install

Ask Codex's built-in installer:

```text
Use $skill-installer to install:
https://github.com/Fahuikongjian/codex-multi-agent-coordination/tree/main/skills/codex-multi-agent-coordination
```

Alternatively, copy `skills/codex-multi-agent-coordination/` into the project's `.agents/skills/` or your client's personal skill directory. Current official documentation lists `~/.agents/skills/`; some existing clients and installers use `~/.codex/skills/`. Follow your client and installer instead of installing duplicates.

Automatic discovery and explicit invocation are supported. Restart Codex if the client has not refreshed. This skill does not change global `AGENTS.md`, model settings, or concurrency limits.

## Use

```text
Use $codex-multi-agent-coordination to complete this feature.
Have the coordinator settle interfaces and acceptance, delegate independent
work, assign file and resource ownership, then integrate and verify.
```

For existing conflicts:

```text
Use $codex-multi-agent-coordination to coordinate the current task.
Two agents are editing one file and review keeps reversing decisions.
Inspect current writers and artifacts, stop overlap safely, resolve the
issue from evidence, and continue unaffected work.
```

For review:

```text
Use $codex-multi-agent-coordination to review this change.
Give read-only reviewers distinct concerns against one stable snapshot.
Have the coordinator verify and deduplicate findings before assigning fixes.
```

The runtime must expose actual subagent tools. Otherwise work proceeds sequentially; user chats are not used to simulate delegation. Existing authorization boundaries remain in force.

## Contents

```text
skills/codex-multi-agent-coordination/
  SKILL.md                         Core workflow
  agents/openai.yaml               English display metadata and prompt
  references/task-contracts.md     Assignment, result, and decision templates
  references/conflict-recovery.md  Conflict recovery and handoffs
  references/codex-tools.md        Runtime adaptation and sources
evals/scenarios.md                Reusable behavioral cases
evals/results.md                  Initial read-only evaluation
evals/live/2026-10-18/             Live development report and evidence
```

Read references only when relevant. Runtime use needs no additional Python packages, MCP service, or background process.

## Validation

The skill passed the bundled skill-creator validator and local YAML/link checks. Four initial read-only scenarios are recorded in [the forward-test report](evals/results.md). A subsequent real subagent run built an offline CSV ledger CLI; see [the live report](evals/live/2026-10-18/report.md) for checks, controlled challenges, ownership transfer, and limitations.

A successful task demonstrates executable coordination, not universal improvement or enforced ownership. This is not an A/B benchmark.

Sources: [OpenAI Skills](https://developers.openai.com/codex/skills) and [OpenAI Subagents](https://developers.openai.com/codex/multi-agent). Actual tool contracts take precedence over example names.

Licensed under the [MIT License](LICENSE).
