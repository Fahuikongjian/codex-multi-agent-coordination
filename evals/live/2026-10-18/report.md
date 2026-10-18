# Live Coordination Test - 2026-10-18

A real development task used a coordinator, two implementation/test subagents, and one separate read-only reviewer. Agents edited and executed an offline Python CSV ledger CLI in one shared checkout. This was not a role-play-only evaluation.

## Final outcome

| Check | Actual result |
| --- | --- |
| Final acceptance and regression suite | 22 tests passed |
| CLI integration suite | 8 tests passed |
| Additional end-to-end CLI cases | 8 passed |
| Controlled cross-scope proposal | Rejected; integer schema and ownership preserved |
| Implementation ownership transfer | Completed after old tasks submitted and tools stopped |
| Archived epoch-1 candidate replay | Rejected against current refund requirements; current source hash unchanged |
| Independent review | Found a real numeric-conversion/JSON crash; fix verified |

The final fixture commit was `d120277199da9556d92da1600990a1186ebb75c5` in the temporary local repository. That identifier is a test snapshot, not a commit in this GitHub repository. Retained source hashes and executed-check results are in [final-results.json](evidence/final-results.json).

## The development task

Build `summarize_orders(csv_text)` and use the supplied CLI to return exactly `order_count` and integer `total_cents`. Required behavior included exact decimal money, quoted CSV, BOM input, reordered headers, duplicate-ID detection, field validation, file/stdin input, JSON stdout, and controlled error exits.

The coordinator owned requirements, acceptance tests, the existing CLI, Git, and integration. The first worker owned only `ledger.py`. The second owned only `tests/test_cli.py` plus allocated temporary files. After both submitted and stopped, implementation ownership transferred to the second worker under a new task epoch. The previous test file remained unchanged during implementation repairs.

## Observed sequence

1. **Red baseline:** the unimplemented fixture failed the original 15 acceptance methods. The raw log contains 30 error entries because subtests also failed; these are not 30 distinct test methods.
2. **Parallel work:** the first worker implemented the library; the second wrote eight real subprocess CLI tests. The coordinator reran the original 15 acceptance tests successfully.
3. **Controlled conflict input:** the coordinator relayed a hypothetical peer proposal to change integer `total_cents` into floating-point `total` and directly edit another owner's file. The test agent rejected it and continued its actual work. This was an injected challenge, not a spontaneous peer incident.
4. **Controlled requirement change:** refunds were added using negative nonzero quantities while preserving the schema. Three new checks failed against the old implementation. After completion acknowledgements, runtime completed states, and matching artifact hashes were checked, `T1/epoch=2` was assigned to the former test worker. It changed the quantity guard and passed 17 acceptance plus eight CLI tests.
5. **Stale candidate check:** archived epoch-1 source was executed against a refund input. It failed and was not copied over current source. File hashes before and after matched. This is an offline archived-candidate replay, not a claim that a slow live agent delivered a late result.
6. **Real review finding:** the separate reviewer reproduced a CLI traceback for a 2,200-digit quantity multiplied by a 2,200-digit price. The coordinator reproduced exit 1, reopened the affected task, and recorded supported input bounds: at most 18 quantity digits and 30 price whole-part digits. The implementation owner added guards before integer conversion under `T1/epoch=3`. Python's global conversion security limit was not disabled.
7. **Bounded follow-up:** the reviewer confirmed the crash fix and identified a minor diagnostic boundary for fields beyond the standard CSV parser limit. Decision D4 explicitly retained that parser limit: parser-level failures may report the line and CSV condition; successfully parsed oversized numeric fields name their field. A regression check confirmed safe rejection rather than another parser implementation or unlimited review.
8. **Final integration:** the coordinator ran all 30 tests and eight manual CLI cases successfully, then confirmed subagents had completed before archival and cleanup.

The final numeric bounds, leading-zero handling, and parser diagnostic boundary are explicit in [SPEC.md](fixture/SPEC.md). Refund behavior, exact cents, and the JSON schema were preserved throughout.

## Evidence and reproduction

- [Final source](fixture/ledger.py), [CLI](fixture/cli.py), and [coordination ledger](fixture/coordination.md).
- [Acceptance and regression tests](fixture/acceptance/test_ledger.py), [large-input CLI regression](fixture/acceptance/test_cli_regression.py), and [CLI integration tests](fixture/tests/test_cli.py).
- [Final acceptance log](evidence/final-acceptance.log), [CLI log](evidence/final-cli.log), and [eight manual cases](evidence/manual-cli.json).
- [Initial numeric crash](evidence/large-number-before-fix.json), [first review](evidence/review-1.json), and [bounded follow-up](evidence/review-2.json).
- [Coordination event record](evidence/events.jsonl) and [stale candidate replay](evidence/stale-candidate-replay.json).

From the retained `fixture/` directory, using Python standard library only:

```sh
python -m unittest discover -s acceptance -v
python -m unittest discover -s tests -v
```

The recorded environment used Python 3.14.3 on Windows. No application dependencies were installed. No test task published externally or changed global configuration. Public evidence replaces temporary absolute paths with `<WORKSPACE>` and excludes local repository internals and bytecode.

## Skill version and limits of the finding

The first implementation and ownership transfer used the original pre-translation skill. The later implementation repair and reviewer used the final English-only installed skill. Before/after skill hashes are retained in the evidence. Translation preserved the coordination rules rather than adding numeric-domain rules to the skill.

This single controlled task demonstrates that the workflow can be executed, including scope refusal, actual ownership transfer, acceptance updates, real defect repair, and bounded convergence. It is not an A/B comparison, a throughput benchmark, operating-system write attribution, enforced file locking, or proof that conflicts can never occur. No active generator was interrupted during the live handoff; both original tasks had completed before transfer.

## Cleanup

Source and verification evidence are retained here for reproduction. The disposable test checkout, its three bytecode cache directories and four bytecode files, allocated test files, and related validation scratch were cleared from the working directory using Windows Recycle Bin. Two permanent-deletion attempts were blocked by the local policy; the recoverable cleanup succeeded, and all five scoped working paths were verified absent. This was not a secure wipe or an emptying of Recycle Bin. The exact status is recorded in [cleanup.json](evidence/cleanup.json). Global Python/pip/browser caches, unrelated work, the installed skill, and deliverables are outside the cleanup scope.
