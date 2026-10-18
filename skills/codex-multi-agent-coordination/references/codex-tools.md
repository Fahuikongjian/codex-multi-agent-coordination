# Codex Runtime Adaptation

Read for a new client or changed subagent tools. This skill does not install runtimes, edit `config.toml`, or require a particular model, platform, or external scheduler.

## Follow actual tool contracts

Identify capabilities among exposed tools. These examples do not establish availability:

| Capability | Possible names | Boundary |
| --- | --- | --- |
| Start a subagent | `spawn_agent`, `collaboration.spawn_agent` | Include a contract and record the returned real ID |
| Update a running agent | `send_input`, `send_message` | Delivery does not establish adoption |
| Assign a follow-up | `followup_task` or equivalent | Distinguish messaging from starting a new turn |
| Wait or inspect | `wait`, `wait_agent`, `list_agents` | Respect limits; avoid frequent polling |
| Interrupt or end | `interrupt_agent`, `close_agent`, or equivalent | Semantics differ; verify tools and processes separately |

Names and parameters vary. Call only exposed capabilities; this table is neither a portable SDK nor executable sample code. If a capability is missing, simplify according to actual state instead of inventing success.

Whether inheriting full history or sending minimal context, supply a clear contract and necessary inputs. Inherit model and reasoning settings unless the user or applicable configuration specifies otherwise. Do not hard-code models, worker counts, or ways around concurrency limits.

## Subagents versus user chats

Some clients expose `create_thread`, `send_message_to_thread`, or similar user-chat tools. They can create sidebar chats or message other user tasks, with different authorization requirements.

Use genuine subagent tools for ordinary delegation. Use user-chat operations only when explicitly requested and permitted by their contracts. An agent message is not human authorization to expand scope or send externally.

## Workspace and integration

Inspect real filesystem layout. Agents using one directory share edits immediately; multiple agents do not imply multiple checkouts. For worktrees, record absolute paths/baselines and explicitly provide required uncommitted input. Branches, commits, PRs, and external mutations follow user authorization and project requirements.

Allocate global-state operations such as installs, builds, migrations, service restarts, and browser actions by resource. Worktrees do not isolate a shared browser, server database, or build cache.

## Sources and boundaries

- [OpenAI: Subagents](https://developers.openai.com/codex/multi-agent)
- [OpenAI: Build skills](https://developers.openai.com/codex/skills)

Checked on 2026-10-18. Current official documentation lists `.agents/skills` for repository and user skills. Some existing clients and installers use `.codex/skills`; follow your actual client and installer.

Ownership, task epochs, ledgers, and dispute handling are cooperation conventions, not built-in OpenAI locks or mandatory access controls. They reduce risk without guaranteeing obedience or agreement. Use actual permissions and isolated resources when stronger separation is required.
