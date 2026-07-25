# Reproducing sharp TV–Hellinger inequalities for Gaussian mixtures

![The exact sharpness ratio exceeds one at every tested order.](reports/tv-hellinger-reproduction/images/headline-sharpness.png)

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/blob/main/notebooks/tv_hellinger_reproduction.py)

This CPU-only campaign reproduces the five theorem-level claims in *Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures* ([arXiv:2602.03202](https://arxiv.org/abs/2602.03202)). The previous judged artifact scored `0/10` because it checked nearby formulas rather than the claims.

The strongest direct result is the paper's explicit Chebyshev sharpness construction. The claimed ratio must be at least `1`; at `n=11,15,19,23,27,31`, the observed ratios are `1.217, 2.502, 5.171, 10.733, 22.400, 46.636`. Adaptive Gauss–Kronrod and independent high-precision Gauss–Hermite integration agree to `3.33e-5` relatively for nonsmooth TV and `9.62e-15` for smooth Hellinger/chi-square integrals.

All five exact claim contracts are assessed **VERIFIED with MEDIUM confidence** through reconstructed analytic proofs, primary-source audits, direct construction evidence, independent checkers, and controls. This is a forecast; the live evaluator has not awarded new points.

## What was tested

| Claim | Paper result | Reproduction result | Assessment |
| --- | --- | --- | --- |
| C1 | `sqrt(chi²) <= max(C0,TV^-alpha) TV` | Universal dependency ledger plus six direct exponent-branch ratios, maximum `2.35e-7` | VERIFIED, MEDIUM |
| C2 | `H <= TV^(1-o(1))` with exact `1/log log` exponent | Pointwise derivation plus six direct ratios, maximum `4.43e-8` | VERIFIED, MEDIUM |
| C3 | Explicit `0.33/log log` sharpness sequence | Six valid mixtures; ratio `1.217`–`46.636`; analytic coefficient and subsequence repair | VERIFIED, MEDIUM |
| C4 | Local-entropy characterization of TV minimax risk | Jia Fano contract plus upper/lower derivation and necessary `delta/2` inverse repair | VERIFIED, MEDIUM |
| C5 | Robust Hellinger upper and matching contamination lower rate | Proper Yatracos/Chen chains plus continuous-amplitude lower-bound repair | VERIFIED, MEDIUM |

The finite sweep is corroboration, not a proxy proof of universal or minimax statements. Those conclusions come from the reconstructed analytic chains. The certificates are not proof-assistant formalizations, and their pinned internal/external lemma dependencies are the main remaining validation risk.

## Read and explore

- [Illustrated technical report](reports/tv-hellinger-reproduction/report.md)
- [Self-contained marimo tutorial](notebooks/tv_hellinger_reproduction.py)
- [Evaluator-visible Hugging Face candidate tree](release/space/README.md)
- [Raw C1–C3 evidence](release/space/evidence/raw/claim_1_3/raw_results.csv)
- [C4–C5 analytic output](release/space/evidence/raw/application_certificate/result.json)

Run the formal suite:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`, one repository-level `.venv`, and exact dependencies are pinned by `pyproject.toml` and `uv.lock`. Numerical seed: `260203202`. No GPU was used. Uncertain numerical jobs ran on Hugging Face `cpu-upgrade`; deterministic sub-five-minute checks ran locally with a one-effective-core estimate.

## Experiment log

The command below is copied verbatim from `orx exp status` and is identical on every formal node.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `main` | Public presentation surface | Not run as an experiment (publication surface) | Baseline source branch; report/notebook mirrored after release | None |
| [`orx/historical-judged-baseline-0-10`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/historical-judged-baseline-0-10) | Freeze and reproduce judged baseline | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Historical rejected baseline reproduced | local CPU, `5s` |
| [`orx/c1-c3-exact-construction-gauss-hermite`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-exact-construction-gauss-hermite) | Independent fixed-node construction route | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C1–C3 direct route passed | HF `cpu-upgrade`, `13.104s` verifier |
| [`orx/c1-c3-exact-construction-adaptive-quadrature`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-exact-construction-adaptive-quadrature) | Adaptive integration and cross-engine comparison | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All direct inequalities and controls passed | HF `cpu-upgrade`, `29.722s` verifier |
| [`orx/c1-c3-analytic-asymptotic-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-analytic-asymptotic-certificate) | Reconstruct universal/asymptotic implications | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C1–C3 analytic chain passed; source relabel repaired | local CPU, `1m40s` cumulative |
| [`orx/c4-c5-application-theorem-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c4-c5-application-theorem-certificate) | Reconstruct minimax and robust application proofs | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C4–C5 passed with two explicit proof repairs | local CPU, `1m35s` cumulative |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-visible-release-candidate) | Visibility, history subset, report, notebook, release gates | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Pending final formal candidate run | local CPU, estimated `<3m` |

Hugging Face billing cost was not exposed in the run logs, so no cost is inferred.
