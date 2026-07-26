# Current claim-by-claim reproduction

Original live judged score: **0/10**. A later verdict assessed the previous candidate `toy, toy, toy, inconclusive, inconclusive` without a numeric total. Candidate forecast after remediation: **4–8/10 conservatively; 10/10 best-supported possible**, pending the live evaluator.

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

The current verifier is `evidence/src/repro/src/run_publication_gate.py`, with `verify_universal_reductions.py` and `run_yatracos_experiment.py` as the new exact/estimator routes. It supersedes the historical verifier at judged revision `1c98799a89d8c1d3c45136c8b912e74371e975b3`.
