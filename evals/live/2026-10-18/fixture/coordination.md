# Live evaluation coordination ledger
Coordinator and integration owner: root.
D1 revision 1: exact money in cents; fixed JSON schema; positive quantities only.
T1 epoch 1: implement ledger.py only; owner implementation agent; baseline fixture commit.
T2 epoch 1: implement tests/test_cli.py only; CLI IO, files/stdin, BOM, validation and exit behavior; no refund policy assertions.
Root owns cli.py, SPEC.md, acceptance/, coordination.md, .git/, evidence/ and final reporting.
T2 additionally owns tmp/T2/ and agent-work/T2/; T1 owns agent-work/T1/.
Subagents must read the installed skill, stop writing after submitted, and report active tools/processes.
No peer can expand another task's write ownership. Test caches are contained inside this run root.

D2 revision 2 (controlled requirement-change event): support refunds using negative nonzero quantity; retain JSON schema and exact cents.
T1 epoch 1: submitted and accepted against revision 1; hash recorded, no active tools/processes reported; no further writes authorized.
T1 epoch 2: planned reassignment to live_cli_tests AFTER T2 submission and confirmed quiescence.
T2 epoch 1: CLI-only criteria unchanged; continues independently.
T2 epoch 1: submitted and accepted; tests hash verified; tools/processes completed; temporary test directory empty.
Runtime verification: both agents completed before transfer.
T1 epoch 1 write ownership: released. T1 epoch 2 owner: live_cli_tests; only ledger.py and agent-work/T1-epoch2/ may be written.
T1 epoch 2: submitted and accepted; only ledger.py changed; 17 acceptance and 8 CLI checks passed.
Archived epoch 1 candidate replay: rejected against D2; current implementation hash unchanged.
English-only skill package synchronized before final read-only review.
R1 epoch 1: submitted read-only review with a reproduced large-number CLI crash; no pending processes.
D3 revision 3: support at most 18 quantity digits and 30 price whole-part digits; oversized input is a field validation error, with no global conversion-limit changes.
T1 epoch 2: completed and stopped; new evidence reopens affected validation.
T1 epoch 3 owner: live_cli_tests; write ledger.py only plus agent-work/T1-epoch3/; test files stay root-owned.
T1 epoch 3: submitted and accepted against D3 after 21 root acceptance and 8 CLI tests; all tools stopped.
Root final manual checks: six cases passed, including three oversized-input regressions.
R1 epoch 2: bounded read-only re-review of numeric guards and D3 evidence requested after stable snapshot.
R1 epoch 2: original defect resolved; generic parser-size diagnostic recorded as a supported boundary under D4. No code change needed for this minor diagnostic concern.
Final acceptance: 22 library/CLI regression tests plus 8 integration tests, 8 manual CLI cases; all passed.
All subagents submitted and reported no running tools/processes before archival and cleanup.
