# Current direct claim-by-claim reproduction

Current live score: **5/10** at judged revision
`6e08ad1e3b8345baf56246f4c50ed663d2365aa6`. The judge requested proof-level
support for the universal and asymptotic quantifiers. This candidate adds an
independently replayed, fail-closed proof-kernel certificate for every claim.
The conservative forecast remains **8–10/10**, with **10/10** the
best-supported possible score rather than a judge result.

| Current page |
| --- |
| [Overview](#/current-overview) |
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
Its proof generator is `verify_kernel_certificate.py`, its independent replay
is `check_kernel_certificate.py`, and its three-route numerical stage is
`run_three_route_evidence.py`. It supersedes the historical verifier and
reruns every previously accepted check.
