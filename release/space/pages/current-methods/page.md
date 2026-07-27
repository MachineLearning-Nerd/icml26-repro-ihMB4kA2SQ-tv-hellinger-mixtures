# Methods and reproducibility

## Fixed command and pinned environment

The baseline command was set once and inherited unchanged:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Environment: Python `3.12`, one repository `.venv`, `uv`, NumPy `2.5.1`, SciPy `1.18.0`, mpmath `1.3.0`, and SymPy `1.14.0`. Exact inputs are [`pyproject.toml`](../../evidence/src/pyproject.toml), [`uv.lock`](../../evidence/src/uv.lock), and [`config.json`](../../evidence/src/repro/config.json).

The paper archive was retrieved with User-Agent `OpenResearch-Reproduction/1.0 (contact: research-audit)` and has SHA-256 `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`. The paper, Jia et al., and Chen–Gao–Ren source anchors, assumptions, quantifiers, dates, URLs, and hashes are in the [source audits](../../evidence/raw/scaled_direct/source_audit.md).

## Scaled design

| Route | Independently committed calibration | Output |
| --- | --- | --- |
| C1/C2 | 60 seeded mixture families; seven amplitude levels; 8,193-point primary grid | 420 exact-bound cells |
| C1/C2 checker | eight preselected sentinels; doubled 16,385-point grid | maximum relative error `2.135e-6` |
| C3 | every odd order 11–31; 100 digits | 11 explicit sharpness mixtures |
| C4 upper | eight geometric horizons 200–50,000; eight seeds; 121 candidate atoms | TV/H confidence intervals and slopes |
| C4/C5 lower | 7,000 seeded mixture pairs, searched independently at each target | Le Cam and equal-law certificates |
| C5 upper | fixed `n=200,000`; six epsilons; 17 contaminant locations; four seeds | worst-location H/H² confidence intervals |

No target slope, sample horizon, contaminant location, or pair was selected from the formula being tested. The C4 fixed-estimator control and C5 benign-contaminant control must fail.

## Compute record

Before the scaled run, runtime was uncertain, so it was routed to Hugging Face `cpu-upgrade`. The job exposed 64 logical CPUs; `OMP`, OpenBLAS, MKL, vecLib, and NumExpr were all pinned to one numerical thread. The scaled stage used `7.999s` and approximately `111 MiB` maximum RSS. A deterministic local artifact regeneration, performed only after that runtime was known, exposed eight logical CPUs, remained one-threaded, and used `6.507s`. No GPU was used. HF billing cost was not exposed, so none is invented.

The first HF attempt used the default image and stopped before science because `uv` was absent. The successful run used `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`. Both attempts remain recorded in the experiment tree.

The first complete evaluator-visible candidate passed the unchanged cumulative command at Git SHA `dcca416ce369663eb30bd325a1bdde9b8a008d56`, OpenResearch run `1d34dc3b-f424-4898-a653-25594cb9f51d`, in `1m00s` on the local backend after runtime was bounded. It regenerated the same deterministic scientific fields and passed all release checks.

## Fail-closed suite

The cumulative entrypoint reruns:

1. the historical regression and unit tests;
2. C1–C3 mixture construction with independent quadrature;
3. proof obligations and primary-source dependency audits;
4. exact analytic/application/universal certificates;
5. the proper finite-cover Yatracos experiment;
6. `run_scaled_direct_evidence.py`;
7. all figures, the marimo notebook check, and evaluator-visible release checks.

Every scientific gate and every intended negative-control rejection is asserted. A mismatch exits nonzero.

- [Cumulative entrypoint](../../evidence/src/repro/src/run_publication_gate.py)
- [Scaled verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Scaled result](../../evidence/raw/scaled_direct/result.json)
- [Claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
- [Raw publication gate](../../evidence/raw/outputs/publication_gate.json)

Historical evidence remains reachable but is explicitly superseded by this current suite.
