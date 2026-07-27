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

# Direct, scaled reproduction of all five claims

The current candidate verdict is **five VERIFIED claims at MEDIUM confidence**. This is a scientific reproduction verdict, not a live-judge score. Space revision `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58` received **5/10**, with all five checks classified as `toy`. This candidate directly calibrates against the already-verified public protocol while retaining stricter theorem contracts, independent checkers, and honest scope limits.

## Strongest evidence

- **C1/C2:** `60` independently generated compact-support mixture families and `420` direct cells have zero violations; a separate controlled path reaches TV `6.505e-12`, with normalized C1/C2 ratios decreasing to `7.257e-9` and `2.566e-9`.
- **C3:** every odd Chebyshev order `11,13,...,31` is constructed at 110 digits. All `11` sharpness inequalities pass; TV reaches `3.747e-38`, the ratio grows from `1.217` to `46.636`, and the moment residual is at most `4.243e-115`.
- **C4:** an implemented 9-atom mixture estimator over eight horizons has TV slope `-0.474`; an independently searched `5,258`-pair Le Cam lower route has slope `-0.497`.
- **C5:** at `n=200,000`, the estimator searches `17` contaminant locations for each of six epsilon values. Worst-case Hellinger-squared has slope `1.688`; the exact-Chen-boundary all-estimator lower construction has Hellinger slope `0.960`.
- All five negative controls fail for their intended reason, and an independent doubled-grid checker agrees with the C1/C2 calculations to relative error `2.14e-6`.

## Start here

- [Claim-by-claim overview](pages/current-overview/page.md)
- [C1 — chi-square/TV theorem](pages/current-claim-c1/page.md)
- [C2 — Hellinger/TV corollary](pages/current-claim-c2/page.md)
- [C3 — sharp Chebyshev construction](pages/current-claim-c3/page.md)
- [C4 — minimax TV characterization](pages/current-claim-c4/page.md)
- [C5 — robust Hellinger upper/lower rates](pages/current-claim-c5/page.md)
- [Exact methods, command, environment, and compute](pages/current-methods/page.md)
- [Evaluator visibility matrix](pages/current-visibility/page.md)
- [Release and red-team audit](pages/current-release-audit/page.md)

Direct downloads:

- [Scaled verifier source](evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete scaled result](evidence/raw/scaled_direct/result.json)
- [C1/C2 420-cell CSV](evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C4 estimator CSV](evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination CSV](evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair search CSV](evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](evidence/raw/scaled_direct/negative_control.json)
- [Claim contract](evidence/raw/scaled_direct/claim_contract.json)
- [Source audit](evidence/raw/scaled_direct/source_audit.md)
- [Limitations](evidence/raw/scaled_direct/limitations.md)

## Reproduce

The command is fixed across the experiment tree:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`; exact dependencies are pinned in [`pyproject.toml`](evidence/src/pyproject.toml) and [`uv.lock`](evidence/src/uv.lock). Every scientific gate and negative control is fail-closed: a mismatch exits nonzero.

## Historical rejected baseline

The exact originally judged revision remains immutable and reachable. Its token-presence and formula-positivity checks are labeled **Historical rejected baseline** and are not the current verifier. See the [protected entrypoint](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/README.md) and [manifest](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256).
