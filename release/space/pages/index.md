# Current direct claim-by-claim reproduction

Current live score: **5/10** at judged revision
`ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58`; all five checks were classified
as `toy`. This evaluator-calibrated candidate remains a forecast of
**8–10/10 conservatively; 10/10 best-supported possible**, pending a new live
evaluation.

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

The obvious current verifier is `evidence/src/repro/src/run_publication_gate.py`. Its new direct numerical stage is `run_scaled_direct_evidence.py`; it supersedes the historical verifier and reruns every previously accepted check.
