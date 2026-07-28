---
title: "Repro - Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-ihMB4kA2SQ
---

# Claim-by-claim reproduction

This bundle evaluates the five headline claims of *Sharp Inequalities between
Total Variation and Hellinger Distances for Gaussian Mixtures*. Each claim has
three materially different executable routes, including a direct route and a
source-pinned universal or asymptotic certificate. A shared fail-closed proof
kernel additionally checks the exact theorem dependency graph and quantifier
closure for C1–C5; a separate program independently replays the saved proof.

| Claim | Three-route outcome |
| --- | --- |
| C1 | `0/420` 1D violations; `0/14` d=2/d=3 violations; all-d certificate passes |
| C2 | `0/420` 1D violations; `0/14` d=2/d=3 violations; universal pointwise reduction passes |
| C3 | `11/11` explicit orders pass; independent integration and infinite-sequence certificate pass |
| C4 | sample upper `n^-0.474`; Le Cam lower `n^-0.497`; 21 log-correction calibrations pass |
| C5 | finite upper `H²~epsilon^1.688`; lower `H²~epsilon^1.920`; exact exponents converge to 2 |

The C1/C2 doubled-grid checker agrees to `2.14e-6`, the C3 independent
high-precision checker agrees to `1.759e-4`, and all intended negative controls
are rejected.

The proof-kernel replay verifies all five conclusions and rejects five mutated
proof objects: the wrong C1 exponent, a missing C2 square, coefficient `0.34`
in C3, the invalid same-`delta` inversion in C4, and the weakened C5
contamination boundary.

## Start here

- [Claim-by-claim overview](pages/current-overview/page.md)
- [C1 — chi-square/TV theorem](pages/current-claim-c1/page.md)
- [C2 — Hellinger/TV corollary](pages/current-claim-c2/page.md)
- [C3 — sharp Chebyshev construction](pages/current-claim-c3/page.md)
- [C4 — minimax TV characterization](pages/current-claim-c4/page.md)
- [C5 — robust Hellinger upper/lower rates](pages/current-claim-c5/page.md)
- [Exact methods, command, environment, and compute](pages/current-methods/page.md)
- [Kernel-checked proof certificate](evidence/raw/kernel_certificate/proof_certificate.json)
- [Independent kernel replay](evidence/raw/kernel_certificate/independent_checker.json)

## Reproduce

The command is fixed across the experiment tree:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`; exact dependencies are pinned in [`pyproject.toml`](evidence/src/pyproject.toml) and [`uv.lock`](evidence/src/uv.lock). Every scientific gate and negative control is fail-closed: a mismatch exits nonzero.

Download the [three-route result](evidence/raw/three_route/result.json),
[route matrix](evidence/raw/three_route/route_matrix.json), [d=2/d=3 raw
cells](evidence/raw/three_route/multidimensional_direct.csv), [complete scaled
result](evidence/raw/scaled_direct/result.json),
[raw CSVs](evidence/raw/scaled_direct/claim_1_2_raw.csv), [independent
checker](evidence/raw/scaled_direct/independent_checker.json), and [negative
controls](evidence/raw/scaled_direct/negative_control.json). The
[proof-kernel generator](evidence/src/repro/src/verify_kernel_certificate.py),
[independent replay source](evidence/src/repro/src/check_kernel_certificate.py),
[visibility matrix](pages/current-visibility/page.md) and [release
audit](pages/current-release-audit/page.md) remain directly reachable.

The immutable [Historical rejected baseline](pages/historical-rejected-baseline/page.md)
is preserved additively and is not the current verification.
