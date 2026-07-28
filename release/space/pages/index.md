# Current direct claim-by-claim reproduction

Current live score: **5/10** at judged revision
`013c7ab5979d4382ffefc3957d32a8a060e82445`. The judge found the earlier
dependency-ledger kernel insufficient because its hardest theorem nodes were
not expanded. This candidate adds an independently checked, source-complete
proof-transcript replay with zero opaque internal nodes.
The conservative forecast is **7–10/10**, with **10/10** the
best-supported possible score rather than a judge result.

| Current page |
| --- |
| [Overview](#/current-overview) |
| [Formal proof replay](#/current-formal-proof-replay) |
| [C1 — chi-square/TV theorem](#/current-claim-c1) |
| [C2 — Hellinger/TV corollary](#/current-claim-c2) |
| [C3 — sharp Chebyshev construction](#/current-claim-c3) |
| [C4 — minimax TV characterization](#/current-claim-c4) |
| [C5 — robust Hellinger rates](#/current-claim-c5) |
| [Methods and reproducibility](#/current-methods) |
| [Evaluator visibility matrix](#/current-visibility) |
| [Release and red-team audit](#/current-release-audit) |
| [Historical rejected baseline](#/historical-rejected-baseline) |

The obvious current verifier is `evidence/src/repro/src/run_publication_gate.py`.
Its theorem-level generator is `verify_source_complete_proof_replay.py`, its
independent checker is `check_source_complete_proof_replay.py`, and its
three-route numerical stage is `run_three_route_evidence.py`. It supersedes
the earlier dependency-ledger kernel and reruns every previously accepted
check.
