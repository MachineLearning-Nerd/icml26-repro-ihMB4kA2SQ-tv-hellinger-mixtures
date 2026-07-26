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

# Claim-by-claim reproduction: TV and Hellinger for Gaussian mixtures

Current candidate result: **five VERIFIED claims, each at MEDIUM confidence**. This is a reproduction verdict, not a live-judge score. The original judged revision `1c98799a89d8c1d3c45136c8b912e74371e975b3` scored **0/10**. A later evaluator assessed published revision `7c0bf4dc84363ff022c388d366397e3b295010a6` as `toy, toy, toy, inconclusive, inconclusive`; its dataset exposes no numeric total, so none is invented here.

The remediation adds an exact symbolic certificate for the universal/asymptotic reductions and an actual proper finite-cover Yatracos estimator under Huber contamination. The estimator covers all `171` pairwise comparison sets; its independent set/TV identity error is at most `4.219e-15`. Finite results are labeled corroboration, and C5’s practical exponent test is explicitly nonvacuous=false because the displayed asymptotic term exceeds one on the tested epsilon grid.

## Start here

- [Current claim-by-claim overview](pages/current-overview/page.md)
- [C1 — chi-square/TV theorem](pages/current-claim-c1/page.md)
- [C2 — Hellinger/TV corollary](pages/current-claim-c2/page.md)
- [C3 — sharp Chebyshev construction](pages/current-claim-c3/page.md)
- [C4 — minimax TV characterization](pages/current-claim-c4/page.md)
- [C5 — robust Hellinger upper/lower rates](pages/current-claim-c5/page.md)
- [Exact methods, command, environment, and compute](pages/current-methods/page.md)
- [Evaluator visibility matrix](pages/current-visibility/page.md)
- [Release and red-team audit](pages/current-release-audit/page.md)

Direct evidence:

- [Exact universal verifier](evidence/src/repro/src/verify_universal_reductions.py) and [output](evidence/raw/universal_reductions/result.json)
- [Proper Yatracos estimator](evidence/src/repro/src/run_yatracos_experiment.py), [aggregate CSV](evidence/raw/yatracos_experiment/aggregate_results.csv), and [raw replicates](evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Independent checker](evidence/raw/yatracos_experiment/independent_checker.json) and [negative controls](evidence/raw/yatracos_experiment/negative_control.json)

## Reproduce

Repository fixed command, inherited unchanged by every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`; exact dependencies are in [`pyproject.toml`](evidence/src/pyproject.toml) and [`uv.lock`](evidence/src/uv.lock). The executable verifiers and tests are under [`evidence/src/repro`](evidence/src/repro). Pinned source archives, including the paper SHA-256 `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`, are maintained in the linked GitHub repository; their retrieval URLs, dates, User-Agent, and hashes are mirrored in the source audits.

## Historical rejected baseline

The exact judged revision is immutable historical evidence. Its pages remain reachable and unchanged, but its token-presence and formula-positivity checks are **not** the current verifier. See the [historical judged entrypoint](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/README.md) and [protected manifest](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256).
