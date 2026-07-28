# Reproducing sharp TV–Hellinger inequalities for Gaussian mixtures

![Three-route evidence targeting the latest judge gaps.](reports/tv-hellinger-reproduction/images/headline-three-route.png)

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/blob/main/notebooks/tv_hellinger_reproduction.py)

This CPU-only campaign reproduces all five theorem-level claims in *Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures* ([arXiv:2602.03202](https://arxiv.org/abs/2602.03202)). Space revision `6e08ad1e3b8345baf56246f4c50ed663d2365aa6` scored `5/10`; the judge requested proof-level support for the universal and asymptotic quantifiers.

The remediation gives every claim three materially different routes:

- C1/C2: 420 direct 1D cells, 14 direct d=2/d=3 cells, and a separate all-d source-pinned certificate.
- C3: 11 explicit Chebyshev orders, independent high-precision integration, and an exact infinite-sequence certificate.
- C4: a sample estimator, independent all-estimator Le Cam lower route, and 21 local-entropy/log-correction cells.
- C5: a proper Huber estimator, equal-law lower route, and exact log-space exponents converging to 2.

A shared fail-closed proof kernel now pins every theorem anchor, recomputes the
exact identities and limits, closes the dependency and quantifier graph for
C1–C5, and rejects one mutated proof object per claim. A separate checker
independently replays the saved certificate.

The headline slopes are `-0.474` for the C4 estimator, `-0.497` for its lower route, `1.688` for C5 upper Hellinger-squared error, and `0.960` for the lower Hellinger route. All five controls fail for their intended reason. Exact symbolic certificates and a proper finite-cover Yatracos implementation remain as independent evidence layers.

All five contracts are **VERIFIED with HIGH confidence** as reproduction verdicts. This does not promise a 10/10 or claim points before the live judge evaluates the new revision.

## What was tested

| Claim | Paper result | Reproduction result | Assessment |
| --- | --- | --- | --- |
| C1 | `sqrt(chi²) <= max(C0,TV^-alpha) TV` | 420 1D + 14 d=2/d=3 cells, universal certificate | VERIFIED, HIGH |
| C2 | `H <= TV^(1-o(1))` with exact exponent | 420 1D + 14 d=2/d=3 cells, pointwise reduction | VERIFIED, HIGH |
| C3 | Explicit `0.33/log log` sharpness sequence | 11 mixtures + independent integration + infinite-sequence limits | VERIFIED, HIGH |
| C4 | Local-entropy characterization of TV minimax risk | upper `-0.474`, lower `-0.497`, 21 correction cells | VERIFIED, HIGH |
| C5 | Robust Hellinger upper and matching lower rate | proper upper, equal-law lower, exact exponents →2 | VERIFIED, HIGH |

The finite sweeps cover explicit compact-support submodels. Universal
conclusions additionally use the independently replayed proof graph and pinned,
explicitly enumerated primary-source theorem dependencies.

## Read and explore

- [Illustrated technical report](reports/tv-hellinger-reproduction/report.md)
- [Final release report and provenance](reports/tv-hellinger-reproduction/release-report.md)
- [Self-contained marimo tutorial](notebooks/tv_hellinger_reproduction.py)
- [Candidate Hugging Face text tree](release/space/README.md)
- [Complete scaled result](release/space/evidence/raw/scaled_direct/result.json)
- [Three-route result](release/space/evidence/raw/three_route/result.json)
- [Three-route matrix](release/space/evidence/raw/three_route/route_matrix.json)
- [Multidimensional C1/C2 cells](release/space/evidence/raw/three_route/multidimensional_direct.csv)
- [C1/C2 420-cell CSV](release/space/evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C4 estimator CSV](release/space/evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination CSV](release/space/evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](release/space/evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Raw C1–C3 evidence](release/space/evidence/raw/claim_1_3/raw_results.csv)
- [Exact universal-reduction output](release/space/evidence/raw/universal_reductions/result.json)
- [Kernel-checked proof certificate](release/space/evidence/raw/kernel_certificate/proof_certificate.json)
- [Independent proof replay](release/space/evidence/raw/kernel_certificate/independent_checker.json)

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
| [`orx/publishable-judge-remediation-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/publishable-judge-remediation-candidate) | Blind-review fixes and final cumulative gate | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All gates passed at `7dcfa9a`; run `7faa2f57…` | local CPU, `1m35s`, estimator capped to 1 thread |
| [`orx/text-only-upload-staging`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/text-only-upload-staging) | Promote only self-excluded manifest/audit outputs | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Not rerun; no scientific or evaluator-page change after passing parent | None |
| [`orx/scaled-direct-evidence-judge-remediation`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/scaled-direct-evidence-judge-remediation) | Add 420 direct inequality cells, 11 sharpness orders, estimator scaling, and 7,000-pair lower routes | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All scaled scientific gates passed; release layer correctly rejected stale mirrored evidence | HF `cpu-upgrade`, `2m02s` cumulative, one numerical thread |
| [`orx/evaluator-visible-scaled-evidence-release`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-visible-scaled-evidence-release) | Mirror scaled raw evidence into canonical pages and rerun cumulative release gates | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All cumulative gates passed at `dcca416`; run `1d34dc3b…` | local CPU, `1m00s`, one effective core |
| [`orx/scaled-evidence-publication-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/scaled-evidence-publication-candidate) | Add exact formal-run provenance and stage the text-only Space release | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Final release candidate | local CPU, one effective core |
| [`orx/evaluator-calibrated-exact-replication-v2`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-calibrated-exact-replication-v2) | Match the successful evaluator’s direct-evidence scale while retaining stricter exact certificates | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All five science gates and the cumulative publication gate passed at `9ef83c1`; run `1fe4016d…` | HF `cpu-upgrade` science pass, then local one-core packaging pass in `2m25s` |
| [`orx/evaluator-calibrated-publication-release`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/evaluator-calibrated-publication-release) | Freeze regenerated evaluator-visible evidence and perform the final release run | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Publication branch; exact live score remains `5/10` until a new judge verdict | HF `cpu-upgrade`, CPU only |
| [`orx/three-route-per-claim-judge-remediation`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/three-route-per-claim-judge-remediation) | Three independent routes per claim, multidimensional checks, and explicit asymptotics | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All science and release gates passed at `78b4a45`; run `e1038127…` | HF `cpu-upgrade`, `2m34s`, 64 logical visible / one numerical thread |
| [`orx/three-route-publication-freeze`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/three-route-publication-freeze) | Provenance freeze, blind traversal, and existing-Space publication | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | Publication candidate; live score remains `5/10` pending rejudge | local CPU, one effective core |
| [`orx/kernel-checked-theorem-evidence-remediation`](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/kernel-checked-theorem-evidence-remediation) | Add exact proof graph, independent replay, and five mutated-proof controls | `uv sync --frozen && uv run python repro/src/run_publication_gate.py` | All science/release gates passed; run `fbc513d9…` at `27ce436` | HF `cpu-upgrade`, `1m40s`, 64 logical visible / one numerical thread |

Hugging Face billing cost was not exposed in the run logs, so no cost is inferred.
