# C4 — minimax TV characterization

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

For every `delta>0` and every Hellinger-compact class `P` contained in the bounded-support Gaussian-mixture class `P_{M,d}`, Theorem 4.3 states

`epsilon_n^(2(1+(2+delta)/log(max(log(1/epsilon_n),e))))`

is a lower bound, up to constants, for the total-variation minimax squared risk, while `epsilon_n²` is an upper bound. Arbitrary and proper estimators agree up to constants. Here `epsilon_n` is the local-Hellinger-entropy rate defined by Jia et al.

## Primary-source assumptions

The exact source archive for Jia et al. (arXiv `2306.12308`) is pinned at SHA-256 `463b2b1e68d964f65c3ae4a0687ed88563d37e9508fbb92cb21a3f974ad9b56a`. Its Corollary 11, Hellinger compactness assumption, local covering number, and Fano proof event were located. The support map is exact:

`[-M,M]^d subset B_2(M sqrt(d))`.

## Exact universal reduction

The upper bound is `TV²<=2H²` plus Jia's entropy characterization. Projecting an arbitrary estimator back into `P` increases TV by at most a factor two, proving equivalence with proper estimators.

For the lower bound, Jia's Fano event has probability at least `1/2` at Hellinger threshold `epsilon_n/4`. C2 gives `H<=J(TV)`, where

`J(t)=max(C0 t,t^(1-alpha(t)))`.

Monotonic inversion and `E[X²]>=a² P(X>=a)` transfer that event to TV risk.

## Negative control and necessary repair

The source text appears to reuse the same `delta` when deriving the displayed inverse power. Exact asymptotic expansion rejects that step:

`L²[(1-(2+delta)/(L+log(1+(2+delta)/L)))(1+(2+delta)/L)-1]`

tends to `-(2+delta)²`, so the required constant-factor inequality has the wrong sign.

The theorem itself remains valid: for a target `delta>0`, invoke C2 with `delta/2`. The repaired first-order limit is `delta/2>0`, providing strict slack and exactly the theorem's target exponent. This is permitted by the theorem's “for every delta>0” quantifier.

The exact universal verifier checks both limits symbolically and records Jia et al.’s Corollary 11 as the remaining imported premise. It also checks the proper-projection triangle rule and the tail-to-risk implication for arbitrary nonnegative loss.

## Proper-estimator experiment

The new empirical route implements the proper finite-cover Yatracos estimator itself; it does not evaluate only the rate formula. The committed domain contains `19` Gaussian location mixtures and all `171` Yatracos sets. Four truth mixtures are sampled for `n=100,200,400,800,1600`, with `40` deterministic replicates per cell.

| n | worst observed mean H² | exhaustive pair TV² lower bound |
| ---: | ---: | ---: |
| 100 | `0.00420437` | `0.000184316` |
| 200 | `0.00160346` | `0.0000841968` |
| 400 | `0.000666160` | `0.0000508592` |
| 800 | `0.000439316` | `0.0000266347` |
| 1600 | `0.000175726` | `0.0000127160` |

The lower column exhausts every pair in the finite cover using a product-affinity/Le Cam certificate. It is a complete finite-domain check, not a proof of the infinite-class minimax theorem. The independent identity `Q_i(A_ij)-Q_j(A_ij)=TV(Q_i,Q_j)` has maximum absolute error `7.216e-16`.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Universal-certificate SHA `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`. Estimator evidence SHA `094d92e`; seed `260203607`; run `7bc34e8e-37bb-4602-838b-7087fbed677a`; local CPU capped to one thread; `1m35s` cumulative runtime and `2.96s` estimator-kernel reference on HF `cpu-upgrade`.

- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Exact universal output](../../evidence/raw/universal_reductions/result.json)
- [Yatracos estimator source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Aggregate risk CSV](../../evidence/raw/yatracos_experiment/aggregate_results.csv)
- [Raw replicate CSV](../../evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Independent checker](../../evidence/raw/yatracos_experiment/independent_checker.json)
- [Negative controls](../../evidence/raw/yatracos_experiment/negative_control.json)
- [Application verifier](../../evidence/src/repro/src/verify_application_certificate.py)
- [Application certificate](../../evidence/raw/application_certificate/result.json)
- [Exact claim contract](../../evidence/raw/application_certificate/claim_contract.json)
- [Jia primary-source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Primary dependency output](../../evidence/raw/primary_dependencies/result.json)
- [Limitations](../../evidence/raw/yatracos_experiment/limitations.md)
