# C1 — chi-square and total variation

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Theorem 2.1 quantifies over every pair of probability measures `pi,eta` supported on `[-M,M]^d` and every `delta>0`. It asserts the existence of `C0=C0(delta,M,d)>0`, independent of `pi,eta`, such that, with `t=TV(f_pi,f_eta)`,

`sqrt(chi²(f_pi || f_eta)) <= max(C0, t^(-alpha(t))) t`,

where `alpha(t)=(2+delta)/log(max(log(1/t),e))`.

The square root is part of the exact source theorem. The domain is compactly supported, unit-covariance Gaussian **location** mixtures; the result is not claimed here for heteroscedastic or unbounded-support mixtures.

## Exact universal certificate

The fail-closed symbolic verifier checks, for the stated symbolic `delta>0`, the exact selection `kappa1=kappa2=sqrt(1+delta/2)`, exponent identity `2*kappa1*kappa2=2+delta`, norm-chain constants, both tail thresholds, max/min inversion, and the mixture-denominator Jensen identity. It anchors the Hermite expansion, Christoffel–Darboux bound, restricted-range/Nikolskii inequalities, and Lambert lemma in the pinned source and exposes them as imported premises rather than silently treating six finite rows as a proof.

This is an independently reconstructed exact reduction relying on weighted-polynomial propositions proved in the pinned paper, not a Lean/Coq proof. That remaining trust boundary is why confidence is MEDIUM.

## Finite corroboration only

The exact Chebyshev construction produces valid probability weights (minimum weights `0.08286` down to `0.03123`) and moment residuals below `2.17e-19`. For `n=11,15,19,23,27,31`, TV ranges from `7.228e-14` to `1.499e-37`, while `sqrt(chi²)` ranges from `5.115e-12` to `1.168e-32`.

The ratio `sqrt(chi²)/(t^(1-alpha(t)))` is:

`2.351e-7, 9.616e-9, 4.196e-10, 1.918e-11, 9.102e-13, 4.428e-14`.

Thus the explicit exponent branch is satisfied in all six faithful cells without using an unspecified large `C0`. These cells corroborate the theorem but do not establish its universal quantifier.

## Independent checker and control

Adaptive Gauss–Kronrod is checked against 1,536-node, 20-extra-digit Gauss–Hermite quadrature. Smooth chi-square values agree to relative error below `9.62e-15`. Negative controls reject the nearby but stronger `alpha(t)=0` claim and a reversed Jensen step. Each failed obligation makes the verifier exit nonzero.

## Reproduce and download

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Universal-certificate SHA `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`; seed `260203202`; CPU estimate one effective core. Run `d7149367-8f62-4a3b-857c-29d2eb303054` completed in `1m15s`.

- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Exact universal output](../../evidence/raw/universal_reductions/result.json)
- [Exact universal contract](../../evidence/raw/universal_reductions/claim_contract.json)
- [Verifier source](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Construction/integration source](../../evidence/src/repro/src/verify_claims_1_3.py)
- [Raw CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent checker](../../evidence/raw/claim_1_3/independent_checker.json)
- [Analytic certificate](../../evidence/raw/analytic_certificate/result.json)
- [Limitations](../../evidence/raw/universal_reductions/limitations.md)
