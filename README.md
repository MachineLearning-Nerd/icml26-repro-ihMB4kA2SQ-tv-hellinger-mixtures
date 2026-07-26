# Reproducing sharp TV–Hellinger inequalities for Gaussian mixtures

![The exact sharpness ratio exceeds one at every tested order.](reports/tv-hellinger-reproduction/images/headline-sharpness.png)

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/blob/main/notebooks/tv_hellinger_reproduction.py)

This CPU-only campaign reproduces the five theorem-level claims in *Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures* ([arXiv:2602.03202](https://arxiv.org/abs/2602.03202)). The original judged artifact scored `0/10`; a later evaluator rated the first remediation `toy, toy, toy, inconclusive, inconclusive` because finite construction checks did not prove universal statements and no estimator experiment instantiated C4–C5.

The strongest direct result is the paper's explicit Chebyshev sharpness construction. The claimed ratio must be at least `1`; at `n=11,15,19,23,27,31`, the observed ratios are `1.217, 2.502, 5.171, 10.733, 22.400, 46.636`. Adaptive Gauss–Kronrod and independent high-precision Gauss–Hermite integration agree to `3.33e-5` relatively for nonsmooth TV and `9.62e-15` for smooth Hellinger/chi-square integrals.

The judge-remediation branch adds an exact symbolic universal-reduction certificate and an actual proper finite-cover Yatracos estimator under point-mass Huber contamination. It checks all 171 pairwise comparison sets, reports 95% confidence intervals and exhaustive finite-cover lower bounds, and marks the practical asymptotic exponent test nonvacuous=false. All five contracts remain **VERIFIED with MEDIUM confidence** as reproduction verdicts, not live-judge points.

The existing [Hugging Face Space](https://huggingface.co/spaces/DineshAI/ihMB4kA2SQ) remains at evaluated revision `7c0bf4dc84363ff022c388d366397e3b295010a6` while this candidate passes release gates. No new score or publication is claimed yet.

## What was tested

| Claim | Paper result | Reproduction result | Assessment |
| --- | --- | --- | --- |
| C1 | `sqrt(chi²) <= max(C0,TV^-alpha) TV` | Universal dependency ledger plus six direct exponent-branch ratios, maximum `2.35e-7` | VERIFIED, MEDIUM |
| C2 | `H <= TV^(1-o(1))` with exact `1/log log` exponent | Pointwise derivation plus six direct ratios, maximum `4.43e-8` | VERIFIED, MEDIUM |
| C3 | Explicit `0.33/log log` sharpness sequence | Six valid mixtures; ratio `1.217`–`46.636`; analytic coefficient and subsequence repair | VERIFIED, MEDIUM |
| C4 | Local-entropy characterization of TV minimax risk | Exact minimax reduction plus implemented proper estimator and exhaustive 19-cover pair lower | VERIFIED, MEDIUM |
| C5 | Robust Hellinger upper and matching contamination lower rate | Exact Yatracos/Chen reductions plus actual contamination/risk experiment and continuous-amplitude repair | VERIFIED, MEDIUM |

The finite sweep is corroboration, not a proxy proof of universal or minimax statements. Those conclusions come from the reconstructed analytic chains. The certificates are not proof-assistant formalizations, and their pinned internal/external lemma dependencies are the main remaining validation risk.

## Read and explore

- [Illustrated technical report](reports/tv-hellinger-reproduction/report.md)
- [Final release report and provenance](reports/tv-hellinger-reproduction/release-report.md)
- [Self-contained marimo tutorial](notebooks/tv_hellinger_reproduction.py)
- [Exact published Hugging Face text tree](release/space/README.md)
- [Raw C1–C3 evidence](release/space/evidence/raw/claim_1_3/raw_results.csv)
- [C4–C5 analytic output](release/space/evidence/raw/application_certificate/result.json)
- [Exact universal-reduction output](release/space/evidence/raw/universal_reductions/result.json)
- [Proper Yatracos aggregate data](release/space/evidence/raw/yatracos_experiment/aggregate_results.csv)
- [Raw estimator replicates](release/space/evidence/raw/yatracos_experiment/raw_replicates.csv)

Run the formal suite:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Python `3.12`, one repository-level `.venv`, and exact dependencies are pinned by `pyproject.toml` and `uv.lock`. Numerical seed: `260203202`. No GPU was used. Uncertain numerical jobs ran on Hugging Face `cpu-upgrade`; deterministic sub-five-minute checks ran locally with a one-effective-core estimate.

## Experiment log

The command below is copied verbatim from `orx exp status` and is identical on every formal node.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `main` | Public presentation surface | Not run as an experiment (publication surface) | Published Space text, report, notebook, and provenance mirrored after release | None |
| [`orx/historical-judged-baseline-0-10`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/historical-judged-baseline-0-10) | Freeze and reproduce judged baseline | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Historical rejected baseline reproduced | local CPU, `5s` |
| [`orx/c1-c3-exact-construction-gauss-hermite`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-exact-construction-gauss-hermite) | Independent fixed-node construction route | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C1–C3 direct route passed | HF `cpu-upgrade`, `13.104s` verifier |
| [`orx/c1-c3-exact-construction-adaptive-quadrature`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-exact-construction-adaptive-quadrature) | Adaptive integration and cross-engine comparison | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All direct inequalities and controls passed | HF `cpu-upgrade`, `29.722s` verifier |
| [`orx/c1-c3-analytic-asymptotic-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-analytic-asymptotic-certificate) | Reconstruct universal/asymptotic implications | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C1–C3 analytic chain passed; source relabel repaired | local CPU, `1m40s` cumulative |
| [`orx/c4-c5-application-theorem-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c4-c5-application-theorem-certificate) | Reconstruct minimax and robust application proofs | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | C4–C5 passed with two explicit proof repairs | local CPU, `1m35s` cumulative |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-visible-release-candidate) | Visibility, history subset, report, notebook, release gates | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All release gates passed at `108047a`; run `f09c11ab…` | local CPU, `1m05s`, 8 logical visible / 1 effective |
| [`orx/universal-proof-certificate-remediation`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/universal-proof-certificate-remediation) | Exact symbolic universal/asymptotic reductions and premise ledger | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Exact C1–C5 reductions and controls passed at `be9b161` | local CPU, `1m15s`, 1 effective core |
| [`orx/yatracos-lower-pair-and-rate-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/yatracos-lower-pair-and-rate-audit) | Actual proper estimator, Huber samples, lower bounds, and nonvacuity audit | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | 19-cover experiment passed at `f0d6a59`; 171-set checker error `7.216e-16` | HF `cpu-upgrade`, `58s`, 64 logical visible |
| [`orx/evaluator-visible-judge-remediation-release`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-visible-judge-remediation-release) | Preliminary cumulative candidate and artifact generation | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Preliminary run `7bc34e8e…` passed at `094d92e`; superseded by immutable gate run | local CPU, `1m35s`, estimator explicitly capped to 1 thread |
| [`orx/final-judge-remediation-release-gates`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/final-judge-remediation-release-gates) | Immutable cumulative science, figure, notebook, visibility, subset, and secret gates | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All gates passed at `959e052`; 171-set checker error `4.219e-15` | local CPU, `1m30s`, estimator capped to 1 thread |

Hugging Face billing cost was not exposed in the run logs, so no cost is inferred.
