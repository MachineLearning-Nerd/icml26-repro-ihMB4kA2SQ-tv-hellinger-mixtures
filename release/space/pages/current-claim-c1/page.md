# C1 — chi-square and total variation

## Exact theorem

Theorem 2.1 quantifies over every pair of mixing laws `pi,eta` supported on `[-M,M]^d` and every `delta>0`. There is a constant `C0=C0(delta,M,d)>0`, independent of `pi,eta`, such that, for `t=TV(f_pi,f_eta)`,

`sqrt(chi²(f_pi || f_eta)) <= max(C0, t^(-alpha(t))) t`,

where `alpha(t)=(2+delta)/log(max(log(1/t),e))`. The square root, unit covariance, location-mixture model, compact support, and quantifiers are all enforced by the [claim contract](../../evidence/raw/scaled_direct/claim_contract.json).

## Outcome: exact expression tested directly

`run_scaled_direct_evidence.py` generates `60` deterministic but independently randomized compact-support mixture families. Each family is evaluated at seven amplitude levels, producing `420` direct theorem cells:

| Quantity | Result |
| --- | ---: |
| TV range | `1.15577e-7` to `4.75248e-2` |
| exact-bound violations | `0 / 420` |
| maximum `sqrt(chi²) / [max(1,t^-alpha(t))t]` | `0.00899694` |
| support half-width range | `1.0307` to `3.9866` |

This tests the exact exponent branch with the stricter explicit choice `C0=1`; no unknown fitted constant is used. The family parameters and every divergence are downloadable in the [420-cell CSV](../../evidence/raw/scaled_direct/claim_1_2_raw.csv).

A separate deterministic 11-location path uses amplitudes `2^-4` through
`2^-32` and 8,192-point Gauss–Legendre quadrature. TV falls from
`1.746e-3` to `6.505e-12`, while the normalized square-root chi-square ratio
falls from `5.487e-4` to `7.257e-9`. This independently exercises the
small-TV regime that drives the theorem's logarithmic exponent.

## Independent checker and control

The independent symbolic verifier reconstructs the exponent identity, norm chain, tail thresholds, max/min inversion, and mixture-denominator Jensen step for symbolic `delta>0`. The numerical checker recomputes eight sentinel cells on a doubled `16,385`-point grid; maximum relative disagreement is `2.135e-6`.

The stronger linear control `sqrt(chi²)<=TV` is deliberately false on the same valid mixtures and is rejected. A failed bound, checker tolerance, assumption audit, or control makes the verifier exit nonzero.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seed `260203214`; one effective numerical core; eight logical CPUs visible;
threads pinned to one. The scaled stage took `15.070s` and the cumulative local
run `2m00s`. No GPU.

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Universal certificate](../../evidence/raw/universal_reductions/result.json)
- [Source audit](../../evidence/raw/scaled_direct/source_audit.md)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
