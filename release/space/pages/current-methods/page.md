# Methods and reproducibility

## Fixed command and environment

The command was set once and inherited unchanged by the baseline and every child:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Environment: Python `3.12`, repository-level `.venv`, `uv` lockfile, NumPy `2.5.1`, SciPy `1.18.0`, mpmath `1.3.0`, SymPy `1.14.0`. See [`pyproject.toml`](../../evidence/src/pyproject.toml) and [`uv.lock`](../../evidence/src/uv.lock).

The paper archive was retrieved with User-Agent `OpenResearch-Reproduction/1.0 (contact: research-audit)` and has SHA-256 `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`. Jia and Chen–Gao–Ren retrieval URLs, date `2026-07-25`, and hashes are in the [source audit](../../evidence/raw/primary_dependencies/source_audit.md).

## Experiment lineage and compute

| Experiment | Backend | Estimate | Actual allocation | Runtime | Result |
| --- | --- | --- | --- | ---: | --- |
| Historical judged baseline | local | 1 effective core, <1m | local CPU | `5s` | Reproduced weak 0/10 baseline; rejected |
| Fixed-node Gauss–Hermite | HF `cpu-upgrade` | uncertain, so remote | 64 logical CPUs visible; one effective core | `13.104s` verifier | Independent C1–C3 route passed |
| Adaptive Gauss–Kronrod | HF `cpu-upgrade` | uncertain, so remote | 64 logical CPUs visible; one effective core | `29.722s` verifier | Independent C1–C3 route passed |
| Exact universal reductions | local | 1 effective core, <5m | 8 logical CPUs visible | `1m15s` cumulative | Exact symbolic C1–C5 reductions passed |
| Proper Yatracos precursor | HF `cpu-upgrade` | uncertain, so remote | 64 logical CPUs visible | `58s` cumulative; `2.9587s` estimator | 19-cover estimator, lower bounds, controls passed |
| One-thread artifact run | local | 1 effective core, <5m | thread cap committed; 8 logical visible | `1m35s` cumulative | Same estimator data regenerated and release regressions passed |

HF billing cost was not exposed in `orx` logs; no cost is invented. No GPU was used. Construction seed: `260203202`; estimator seed: `260203607`. Universal-certificate Git SHA: `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`; immutable cumulative evidence Git SHA: `959e052077f7edb0609e1d81b3e4b5f59c400a55`.

## Non-circular design

The six mixture orders were not selected by fitting the claimed slope. They instantiate the paper's explicit construction and are evaluated by two independent integration algorithms. The estimator sample sizes form a geometric horizon sweep committed independently of the theorem formula. Universal/minimax claims are concluded from exact symbolic implications and pinned primary-source theorems, not from either finite sweep.

The C5 nonvacuity audit is fail-open with respect to interpretation and fail-closed with respect to data: it records that the displayed asymptotic epsilon term is above one at every practical grid point, and therefore forbids treating the observed slope as verification of that exponent.

## Fail-closed suite

The cumulative entrypoint reruns the historical regression, unit tests, direct mixture construction, independent quadrature, proof obligations, primary dependencies, C1–C3 analytic certificate, C4–C5 application certificate, exact universal reductions, the proper Yatracos experiment, figures, marimo validation, and the release visibility gate. Any failed assertion exits nonzero.

- [Cumulative entrypoint](../../evidence/src/repro/src/run_publication_gate.py)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Proper estimator source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Unit tests](../../evidence/src/repro/tests/test_certificate.py)
- [Universal result](../../evidence/raw/universal_reductions/result.json)
- [Estimator result](../../evidence/raw/yatracos_experiment/result.json)
- [Raw gate output](../../evidence/raw/outputs/publication_gate.json)

Historical checkpoint states are preserved rather than rewritten. The current release checker and manifest identify the candidate state.
