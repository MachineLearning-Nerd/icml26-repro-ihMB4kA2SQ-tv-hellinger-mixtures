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
| C4/C5 lower | 6,000 seeded attempts yielding 5,257 random pairs plus one exact Chebyshev pair | Le Cam and equal-law certificates |
| C5 upper | fixed `n=200,000`; six epsilons; 17 contaminant locations; four seeds | worst-location H/H² confidence intervals |

No target slope, sample horizon, contaminant location, or pair was selected from the formula being tested. The C4 fixed-estimator control and C5 benign-contaminant control must fail.

## Compute record

The first uncertain scaled run used Hugging Face `cpu-upgrade`; numerical
libraries were pinned to one thread. Once runtime was bounded, the current
formal publication-freeze run used the authorized local backend: one effective
core, eight logical CPUs visible, `31.403s` for the scaled stage, `3m06s` total,
and `115,638,272` bytes maximum RSS. No GPU was used. The HF billing cost was
not exposed, so none is invented.

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
- [Evaluator visibility matrix](../current-visibility/page.md)
- [Release and red-team audit](../current-release-audit/page.md)
- [Historical rejected baseline](../historical-rejected-baseline/page.md)

Historical evidence remains reachable but is explicitly superseded by this current suite.
