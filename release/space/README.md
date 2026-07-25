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

Current candidate result: **five VERIFIED claims, each at MEDIUM confidence**. This is a forecast artifact; the live evaluator has not awarded new points. Previous live judged score: **0/10** at Space revision `1c98799a89d8c1d3c45136c8b912e74371e975b3`.

The strongest evidence is an independently reconstructed proof chain backed by two independent high-precision integrations of the paper's explicit Chebyshev Gaussian mixtures. The sharpness inequality passes at every tested odd order `n=11,15,19,23,27,31`; its ratio grows from `1.217` to `46.636`. The analytic audit also found and repaired two application-proof presentation gaps instead of silently accepting them.

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

## Reproduce

Repository fixed command, inherited unchanged by every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`; exact dependencies are in [`pyproject.toml`](evidence/src/pyproject.toml) and [`uv.lock`](evidence/src/uv.lock). The executable verifiers and tests are under [`evidence/src/repro`](evidence/src/repro). Pinned source archives, including the paper SHA-256 `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`, are maintained in the linked GitHub repository; their retrieval URLs, dates, User-Agent, and hashes are mirrored in the source audits.

## Historical rejected baseline

The exact judged revision is immutable historical evidence. Its pages remain reachable and unchanged, but its token-presence and formula-positivity checks are **not** the current verifier. See the [historical judged entrypoint](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/README.md) and [protected manifest](historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256).
