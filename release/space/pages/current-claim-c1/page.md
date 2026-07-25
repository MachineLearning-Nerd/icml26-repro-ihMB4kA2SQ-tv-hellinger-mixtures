# C1 — chi-square and total variation

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Theorem 2.1 quantifies over every pair of probability measures `pi,eta` supported on `[-M,M]^d` and every `delta>0`. It asserts the existence of `C0=C0(delta,M,d)>0`, independent of `pi,eta`, such that, with `t=TV(f_pi,f_eta)`,

`sqrt(chi²(f_pi || f_eta)) <= max(C0, t^(-alpha(t))) t`,

where `alpha(t)=(2+delta)/log(max(log(1/t),e))`.

The square root is part of the exact source theorem. The domain is compactly supported, unit-covariance Gaussian **location** mixtures; the result is not claimed here for heteroscedastic or unbounded-support mixtures.

## Verification chain

The source-pinned derivation audits the weighted-polynomial `L1(phi_d)`–`L2(phi_d)` theorem, the exact selection `kappa1=kappa2=sqrt(1+delta/2)`, the multinomial Hermite-tail identity `sum_{|k|=m}1/k!=d^m/m!`, all deterministic threshold implications, translation from `[-M,M]^d` to `[-2M,2M]^d`, and the Jensen/Fubini reduction to chi-square. The final exponent identity is exact: `2*kappa1*kappa2=2+delta`.

This is an independently reconstructed derivation relying on the weighted-polynomial propositions proved in the pinned paper, not a Lean/Coq formalization. That limitation is why confidence is MEDIUM.

## Direct numerical corroboration

The exact Chebyshev construction produces valid probability weights (minimum weights `0.08286` down to `0.03123`) and moment residuals below `2.17e-19`. For `n=11,15,19,23,27,31`, TV ranges from `7.228e-14` to `1.499e-37`, while `sqrt(chi²)` ranges from `5.115e-12` to `1.168e-32`.

The ratio `sqrt(chi²)/(t^(1-alpha(t)))` is:

`2.351e-7, 9.616e-9, 4.196e-10, 1.918e-11, 9.102e-13, 4.428e-14`.

Thus the explicit exponent branch is satisfied in all six faithful cells without using an unspecified large `C0`.

## Independent checker and control

Adaptive Gauss–Kronrod is checked against 1,536-node, 20-extra-digit Gauss–Hermite quadrature. Smooth chi-square values agree to relative error below `9.62e-15`. Negative controls reject the nearby but stronger `alpha(t)=0` claim and a reversed Jensen step. Each failed obligation makes the verifier exit nonzero.

## Reproduce and download

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Formal evidence SHA `de2c3a8fba29e433c552ce82c194196fefaaa4d8`; seed `260203202`; CPU estimate one effective core. The cumulative local run `c2f14a57-63e5-4320-ac3d-eaa6cd270051` completed in `1m35s` with 8 logical CPUs visible; the C1–C3 stage used `43.590s`.

- [Verifier source](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Construction/integration source](../../evidence/src/repro/src/verify_claims_1_3.py)
- [Raw CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent checker](../../evidence/raw/claim_1_3/independent_checker.json)
- [Analytic certificate](../../evidence/raw/analytic_certificate/result.json)
- [Limitations](../../evidence/raw/analytic_certificate/limitations.md)
