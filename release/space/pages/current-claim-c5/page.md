# C5 — robust Hellinger upper and lower rates

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Under `epsilon`-Huber contamination

`(1-epsilon) P_{f_pi} + epsilon Q`,

where `pi` is supported on `[-M,M]^d` and `Q` is arbitrary, Theorem 4.5 bounds the proper Yatracos estimator's expected squared-Hellinger error by

`epsilon^(2(1-(2+delta)/log(max(log(1/epsilon),e)))) + n^(-1+o_d(1))`

for every `delta>0`. Theorem 4.6 lower-bounds every estimator by the analogous contamination term with coefficient `0.33`.

## Exact universal upper reduction

The Yatracos class has at most `N²` sets. Integrating the exact Hoeffding/union tail

`min(1,2|A| exp(-n s²/2))`

gives `2(1+log(2|A|))/n`. With the paper's TV entropy bound and `eta=log(n)^(d/2)/sqrt(n)`, this yields TV squared risk `epsilon²+log(n)^(d+1)/n`.

For `G(t)=t^(1-alpha(t))`, exact derivatives show eventual increase and concavity. Hence `J(t)=max(C0t,G(t))` is subadditive. The expectation step is not assumed: an explicit envelope with `a_n=2c/log log n` is split at `log(1/t)=sqrt(log n)`, producing only an `n^o(1)` multiplier. This yields the claimed `n^(-1+o_d(1))` term.

## Exact universal lower reduction and repair

The Chen–Gao–Ren primary source is pinned at SHA-256 `7a166a8042adc601c39da0f178fe1ec941d1ed0750e2ad3ecf079c43f1395f88`. It proves that if `TV(P1,P2)<=epsilon/(1-epsilon)`, contamination laws can be chosen to make the two observed distributions identical. Metric triangle inequality then forces squared-Hellinger risk at least one quarter of the separation.

The paper jumps from C3's discrete sequence to every `epsilon`; monotone convergence alone does not justify that. The repair varies the explicit construction's mixing amplitude continuously. Choosing order

`m(epsilon) ~ 2(1-0.002) log(1/epsilon)/log log(1/epsilon)`

makes its admissible maximum TV asymptotically larger than `epsilon`, so the amplitude sets TV exactly to `epsilon`. TV is exactly linear in amplitude, while the construction’s **lower-bound ratio is uniformly amplitude-independent** because the same density-ratio bound holds at every smaller amplitude. Exact Hellinger distance itself is not asserted to be linear. The coefficient budget is

`(log(2)-2/5.53)(1-0.002) = 0.3308205607 > 0.33`.

Tensoring with common standard-Gaussian coordinates preserves both distances exactly, covering every fixed dimension.

## Actual Huber-contamination experiment

For each of four truth mixtures and `epsilon=0,0.02,0.05,0.1,0.2`, the proper finite-cover Yatracos estimator receives fresh samples from `(1-epsilon)P+epsilon*delta_q`. The point-mass adversary `q` is chosen from the fixed grid `{-6,-3,3,6}` at population level, independently of sample horizon. There are `40` replicates at each of five sample sizes.

At `n=1600`, the worst mean squared-Hellinger losses are:

| epsilon | observed worst mean H² | 95% CI on worst truth | equal-law finite-cover lower |
| ---: | ---: | ---: | ---: |
| 0.02 | `0.000443447` | `[0.000063443, 0.000823451]` | `0.0000430255` |
| 0.05 | `0.00183580` | `[0.00132461, 0.00234700]` | `0.00102137` |
| 0.10 | `0.00454531` | `[0.00386728, 0.00522335]` | `0.00239702` |
| 0.20 | `0.00595832` | `[0.00321900, 0.00869764]` | `0.0145177` |

The lower row at every epsilon uses a **distinct** cover pair satisfying the exact Chen boundary `TV<=epsilon/(1-epsilon)`. Because the observation laws can then be made identical, the finite-cover lower bound applies to every estimator, not only the implemented Yatracos rule.

## Nonvacuity audit

The practical epsilon grid was committed independently of the claimed formula. With the configured `delta=1`, the exact displayed paper term is `120.89, 412.47, 251.19, 47.59`, respectively—larger than the maximum possible squared-Hellinger loss. Therefore these finite experiments do **not** verify the asymptotic `epsilon` exponent. The observed finite-grid slope `1.1604` is a diagnostic only. The universal/asymptotic verdict rests on the exact symbolic reduction and its explicit premise ledger.

## Independent checker and controls

The analytic checker rejects the discrete-sequence-only inference, coefficient `0.34`, omission of the Yatracos union factor, and the incorrect stronger Chen threshold `TV<=epsilon` as an equivalence. The experiment checker independently verifies all `171` Yatracos set/TV identities to `4.219e-15`, rejects wrong set orientation, shows an empty comparison class is worse, and confirms no formula-derived horizon was used.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Universal-certificate SHA `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`. Estimator evidence SHA `959e052077f7edb0609e1d81b3e4b5f59c400a55`; seed `260203607`; run `05a4e1bb-3d3b-4a80-a27d-6f886c81968e`; local CPU capped to one thread; `1m30s` cumulative runtime. The independent HF `cpu-upgrade` precursor exposed 64 logical CPUs and used `2.9587s` in the estimator kernel.

- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Exact universal output](../../evidence/raw/universal_reductions/result.json)
- [Yatracos estimator source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Aggregate risk CSV](../../evidence/raw/yatracos_experiment/aggregate_results.csv)
- [Raw replicate CSV](../../evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Complete experiment JSON](../../evidence/raw/yatracos_experiment/result.json)
- [Independent checker](../../evidence/raw/yatracos_experiment/independent_checker.json)
- [Negative controls](../../evidence/raw/yatracos_experiment/negative_control.json)
- [Application verifier](../../evidence/src/repro/src/verify_application_certificate.py)
- [Raw application output](../../evidence/raw/application_certificate/result.json)
- [Exact claim contract](../../evidence/raw/application_certificate/claim_contract.json)
- [Primary dependency output](../../evidence/raw/primary_dependencies/result.json)
- [Method](../../evidence/raw/yatracos_experiment/method.md)
- [Limitations](../../evidence/raw/yatracos_experiment/limitations.md)
