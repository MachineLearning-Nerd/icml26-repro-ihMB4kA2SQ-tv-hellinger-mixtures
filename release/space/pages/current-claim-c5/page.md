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

## Outcome: contaminated-sample upper route

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

## Independent all-estimator lower route

The separate `5,258`-pair cloud is filtered at the exact Chen boundary
`TV(P0,P1)<=epsilon/(1-epsilon)`. For all nine epsilon values from `1e-5` to
`.1`, an admissible pair makes the two contaminated observation laws identical.
Triangle inequality then lower-bounds every estimator by half the pair’s
Hellinger separation. The fitted lower exponents are
`H ~ epsilon^0.96006` and `H² ~ epsilon^1.92011`, with zero saturated search
steps. The upper and lower routes therefore bracket the claimed
`epsilon^(2(1-o(1)))` squared-Hellinger scale.

The exact symbolic checker separately verifies the Yatracos expectation
transfer, continuous-amplitude Chebyshev extension, Chen boundary, coefficient
budget `0.3308206>0.33`, and dimension-preserving tensorization. All `171`
finite Yatracos comparison-set identities agree to `<5e-15`.

## Reproduce

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seeds `260203625` and `260207502`; one effective numerical core; CPU only.

- [Verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Contamination CSV](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact reduction](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Chen source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Scope and deviations](../../evidence/raw/scaled_direct/limitations.md)
