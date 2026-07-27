# C4 — minimax TV characterization

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

For every `delta>0` and every Hellinger-compact class `P` inside the bounded-support Gaussian-mixture class, Theorem 4.3 brackets the total-variation minimax squared risk between

`epsilon_n^(2(1+(2+delta)/log(max(log(1/epsilon_n),e))))`

and `epsilon_n²`, up to constants. Here `epsilon_n` is the local-Hellinger-entropy rate of Jia et al.; arbitrary and proper estimators agree up to constants.

## Direct upper scaling experiment

The scaled route samples a fixed 9-atom truth and fits nonnegative Gaussian-mixture weights on an independently committed 121-point support grid. Eight deterministic replicates are run at every horizon:

| n | mean TV | 95% CI |
| ---: | ---: | ---: |
| 200 | `0.05952` | `[0.04897, 0.07007]` |
| 500 | `0.04880` | `[0.03550, 0.06211]` |
| 1,000 | `0.03175` | `[0.02357, 0.03993]` |
| 2,000 | `0.02303` | `[0.01762, 0.02844]` |
| 5,000 | `0.01697` | `[0.01256, 0.02139]` |
| 10,000 | `0.009759` | `[0.008103, 0.01142]` |
| 20,000 | `0.007337` | `[0.006225, 0.008449]` |
| 50,000 | `0.004877` | `[0.003764, 0.005989]` |

The fitted TV exponent is `-0.47376`; Hellinger is `-0.43178`. A deliberately fixed estimator has mean TV `0.1173` and slope `0`, so the primary check cannot pass merely because sample size increases.

## Independent minimax lower route

A fixed seed makes `6,000` independent pair attempts and yields `5,257` valid
random compact-support pairs. One independently reconstructed Chebyshev
extremal pair is added, producing `5,258` pairs without using the theorem’s
target sample size or slope. At each of eight horizons, the checker selects the best pair for the exact Le Cam certificate

`(TV(P0,P1)/2) * (1 - upper_bound_TV(P0^n,P1^n))`,

using the exact product-affinity identity `(1-H(P0,P1)^2)^n`. The lower-bound TV slope is `-0.49711` (squared-risk slope `-0.99423`), and the search never lacks an admissible pair.

This provides genuinely separate upper and lower routes rather than fitting the theorem formula to formula-derived horizons. Raw estimator rows and every searched pair are downloadable.

## Exact reduction and controls

The symbolic verifier transfers Jia et al.’s local-entropy event through the sharp TV–Hellinger inverse and the tail-to-risk inequality. It detects the source’s same-`delta` sign problem and checks the valid `delta/2` repair permitted by the theorem’s `for every delta>0` quantifier. The proper finite-cover Yatracos experiment separately instantiates all `171` comparison sets and checks their TV identities to `<5e-15` across both formal and local platforms.

Controls reject the same-delta inverse, a fixed estimator, and a vacuous pair search. Any failed upper slope, lower slope, independent identity, or control exits nonzero.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seeds `260203514` and `260207502`; 8 replicates; one effective numerical core; HF `cpu-upgrade`; no GPU.

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete scaled result](../../evidence/raw/scaled_direct/result.json)
- [Estimator raw CSV](../../evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [5,258-pair raw CSV](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Proper Yatracos source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Yatracos raw replicates](../../evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Jia source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
