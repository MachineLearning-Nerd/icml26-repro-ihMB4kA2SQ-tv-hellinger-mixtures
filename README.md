# Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures

CPU-only, source-pinned reproduction certificate for ICML 2026 OpenReview paper
`ihMB4kA2SQ` (arXiv:2602.03202).

## Result

The publication gate verifies five anchored claims against the pinned primary
source and independent finite certificates: Gaussian-mixture divergence cells,
Chebyshev-root identities, and the stated logarithmic rate forms. Three
incorrect alternatives are deliberately rejected.

This is a finite, numerical and source-contract audit. It is not a new proof of
the paper's universal theorems, and the source contains no author experiment
release to rerun.

## Reproduce

```bash
.venv/bin/python repro/src/verify_tv_hellinger.py --output outputs/verification.json
.venv/bin/python repro/src/run_publication_gate.py
```

The source archive is `source/arxiv-2602.03202.tar`; its SHA-256 is
`dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`.

## Claims and evidence

| Claim | Primary-source anchor | Independent certificate |
|---|---|---|
| C1 | Theorem 2.1 chi-square / TV inequality | Five finite two-component Gaussian shifts |
| C2 | Corollary 2.4 Hellinger inequality | Hellinger/TV/chi-square relation on the same cells |
| C3 | Theorem 3.1 Chebyshev-node sharpness construction | Exact Chebyshev polynomial roots for 16 orders |
| C4 | Theorem 4.3 TV-learning characterization | Four positive logarithmic rate-form cells |
| C5 | Theorems 4.5–4.6 robust Hellinger rates | Four robust and lower-rate-form cells |

## Negative controls

The verifier rejects an incorrect Hellinger normalization on separated
mixtures, non-root Chebyshev nodes, and replacing `log log(1/epsilon)` with
`log(1/epsilon)` in the sharpness exponent.
