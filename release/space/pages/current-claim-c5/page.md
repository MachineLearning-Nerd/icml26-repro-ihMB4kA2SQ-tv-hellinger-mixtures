# C5 — robust Hellinger upper and lower rates

## Exact theorem

For samples from `(1-epsilon)P_fpi + epsilon Q`, with arbitrary `Q`,
Theorem 4.5 gives the proper Yatracos estimator

`sup_pi,Q E[H(f_pi,f_hat)^2]`

`<= epsilon^(2(1-(2+delta)/log(max(log(1/epsilon),e)))) + n^(-1+o_d(1))`.

Theorem 4.6 lower-bounds every estimator by the corresponding contamination
term with coefficient `0.33`. The quantifiers, compact support, squared
Hellinger loss, proper upper estimator, and all-estimator lower bound are
encoded in the [claim contract](../../evidence/raw/scaled_direct/claim_contract.json).

## Approach 1 — proper estimator and adversarial-Huber upper route

At `n=200,000`, the estimator is run for four replicates at each epsilon and
the worst result over 17 fixed point-mass contaminant locations is reported:

| epsilon | worst Q | mean H | 95% CI | mean H² |
| ---: | ---: | ---: | ---: | ---: |
| .01 | -4.0 | .0127385 | [.0101047, .0153723] | .000162270 |
| .02 | -4.0 | .0233112 | [.0173132, .0293092] | .000543412 |
| .04 | -4.0 | .0432097 | [.0320204, .0543991] | .001867082 |
| .08 | -4.0 | .0777695 | [.0596811, .0958579] | .006048097 |
| .16 | -4.0 | .1365205 | [.1093619, .1636791] | .018637840 |
| .32 | -4.0 | .2356158 | [.1967960, .2744355] | .055514788 |

The fitted exponents are `H ~ epsilon^0.84411` and
`H² ~ epsilon^1.68821`. A benign-Q control produces materially smaller error
and is rejected, so the result is not selected from a convenient contaminant.

## Approach 2 — independent all-estimator lower route

The separate `5,258`-pair cloud is filtered at the exact Chen boundary
`TV(P0,P1)<=epsilon/(1-epsilon)`. For all nine epsilon values from `1e-5` to
`.1`, an admissible pair makes the two contaminated observation laws identical.
Triangle inequality then lower-bounds every estimator by half the pair’s
Hellinger separation. The fitted lower exponents are
`H ~ epsilon^0.96006` and `H² ~ epsilon^1.92011`, with zero saturated search
steps. The upper and lower routes therefore bracket the claimed
`epsilon^(2(1-o(1)))` squared-Hellinger scale.

## Approach 3 — small-epsilon asymptotics and proof-kernel replay

The finite fitted upper exponent `1.68821` is not presented as the asymptotic
limit. A separate underflow-safe log-space calibration evaluates the exact
effective exponents as `log log(1/epsilon)` grows:

| log log(1/epsilon) | upper H² exponent | lower H² exponent |
| ---: | ---: | ---: |
| 4 | `.9000` | `1.8350` |
| 8 | `1.4500` | `1.9175` |
| 20 | `1.7800` | `1.9670` |
| 80 | `1.9450` | `1.99175` |

This directly demonstrates the claimed convergence to `2`. The symbolic half
of the route proves the Yatracos expectation transfer for an arbitrary
`[0,1]` deviation and every Huber contaminant `Q`, rather than a finite Q grid.
For the lower bound it verifies continuous amplitude, the Chen equal-law
condition, the all-estimator triangle argument, and the common-Gaussian
product lift to every fixed dimension.

The exact symbolic checker separately verifies the Yatracos expectation
transfer, continuous-amplitude Chebyshev extension, Chen boundary, coefficient
budget `0.3308206>0.33`, and dimension-preserving tensorization. All `171`
finite Yatracos comparison-set identities agree to `<5e-15`.

The proof kernel carries the arbitrary-`Q`, proper-upper, all-estimator-lower,
and sufficiently-small-`epsilon` quantifiers through the dependency graph. It
recomputes the exponent limit and exact Chen equal-law budget, while the
independent replay rejects the weaker invalid `TV<=epsilon` mutation.

## Reproduce

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seeds `260203625` and `260207502`; one effective numerical core; CPU only.

- [Verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Three-route verifier](../../evidence/src/repro/src/run_three_route_evidence.py)
- [Three-route matrix](../../evidence/raw/three_route/route_matrix.json)
- [Small-epsilon exponent CSV](../../evidence/raw/three_route/claim_5_asymptotic.csv)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Contamination CSV](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact reduction](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Proof-kernel generator](../../evidence/src/repro/src/verify_kernel_certificate.py)
- [Independent proof replay](../../evidence/src/repro/src/check_kernel_certificate.py)
- [Kernel certificate](../../evidence/raw/kernel_certificate/proof_certificate.json)
- [Kernel replay output](../../evidence/raw/kernel_certificate/independent_checker.json)
- [Chen source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Scope and deviations](../../evidence/raw/scaled_direct/limitations.md)
