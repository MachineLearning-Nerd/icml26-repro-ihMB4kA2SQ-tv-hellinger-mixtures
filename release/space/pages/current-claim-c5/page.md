# C5 — robust Hellinger upper and lower rates

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Under Huber contamination `(1-epsilon)P_{f_pi}+epsilon Q`, where `Q` is arbitrary, Theorem 4.5 gives the proper-estimator expected squared-Hellinger upper rate

`epsilon^(2(1-(2+delta)/log(max(log(1/epsilon),e)))) + n^(-1+o_d(1))`.

Theorem 4.6 lower-bounds every estimator by the analogous contamination term with coefficient `0.33`.

## Direct adversarial upper experiment

The scaled experiment uses `n=200,000`, four deterministic replicates, six epsilon values, and a fixed grid of `17` contaminant point-mass locations. At each epsilon it reports the worst location, selected before looking at the random replicate outcomes:

| epsilon | worst location | mean H | 95% CI | mean H² |
| ---: | ---: | ---: | ---: | ---: |
| 0.01 | `-4.0` | `0.01390` | `[0.00990, 0.01791]` | `0.0001932` |
| 0.02 | `-4.0` | `0.02625` | `[0.01505, 0.03746]` | `0.0006893` |
| 0.04 | `-4.0` | `0.04769` | `[0.03292, 0.06246]` | `0.002274` |
| 0.08 | `-4.0` | `0.08613` | `[0.06311, 0.10916]` | `0.007419` |
| 0.16 | `-4.0` | `0.14826` | `[0.11444, 0.18208]` | `0.02198` |
| 0.32 | `-4.0` | `0.25197` | `[0.20488, 0.29906]` | `0.06349` |

The fitted Hellinger-squared exponent is `1.68821` (`H` exponent `0.84411`). The practical exponent approaches the claimed `2(1-o(1))` direction while the fixed `n` suppresses the sampling term. The estimator grid and epsilon horizon were committed independently of this fitted slope.

## All-estimator lower construction

The separate `5,258`-pair cloud is filtered at the exact Chen boundary

`TV(P0,P1) <= epsilon/(1-epsilon)`.

For each of nine epsilon values from `1e-5` to `0.1`, an admissible pair is found and the contaminated observation laws can be made identical. Triangle inequality therefore lower-bounds every estimator by half the pair’s Hellinger separation. The resulting lower Hellinger exponent is `0.96006` (H² exponent `1.92011`), with `0` saturated search steps.

This lower route does not rely on the implemented estimator and directly exercises the theorem’s indistinguishability mechanism.

## Exact reduction, checker, and controls

The symbolic verifier checks the Yatracos expectation transfer, continuous-amplitude extension of the Chebyshev construction, exact Chen boundary, coefficient budget `0.3308206>0.33`, and dimension-preserving tensorization. The separate proper Yatracos experiment instantiates actual Huber samples and checks all `171` comparison-set identities to `6.106e-16`.

The adversarial-location control confirms that using only a benign contaminant understates the loss; the lower-search control rejects the stronger but invalid `TV<=epsilon` equivalence. Every scientific gate and control is fail-closed.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seeds `260203625` and `260207502`; one effective numerical core; HF `cpu-upgrade`; no GPU.

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete scaled result](../../evidence/raw/scaled_direct/result.json)
- [Raw contamination CSV](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair raw CSV](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Proper Yatracos source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Yatracos raw replicates](../../evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Chen primary-source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
