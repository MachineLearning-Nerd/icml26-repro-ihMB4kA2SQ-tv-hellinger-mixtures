# C2 — Hellinger and total variation

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Corollary 2.4 has the same support and `delta>0` quantifiers as C1 and asserts

`H(f_pi,f_eta) <= max(C0, t^(-alpha(t))) t`,

with `t=TV(f_pi,f_eta)` and `alpha(t)=(2+delta)/log(max(log(1/t),e))`. This is the precise `TV^(1-o(1))` statement: `alpha(t)` tends to zero at order `1/log log(1/t)`.

## Exact universal certificate

For symbolic positive densities `x,y`, the verifier reduces

`((x-y)²/y) / (sqrt(x)-sqrt(y))²`

exactly to `(sqrt(x/y)+1)²`, proving the pointwise implication before integration. Therefore C2 inherits the universal quantifiers of C1 rather than being inferred from a fitted finite-data slope. The checker rejects dropping the square.

## Direct numerical corroboration

On the six explicit sharp Gaussian-mixture pairs, TV ranges from `1.807e-14` to `3.747e-38` and Hellinger distance ranges from `4.521e-13` to `1.032e-33`.

The exact ratio `H/(t^(1-alpha(t)))` is:

`4.428e-8, 1.867e-9, 8.335e-11, 3.880e-12, 1.868e-13, 9.201e-15`.

All are below `1`. The simpler control `H/TV` instead grows from `25.02` to `27,553`, illustrating why the theorem's logarithmic exponent is substantive and why checking only `H²<=TV` would miss the claim. These six rows are corroboration only.

## Independent checker and control

Adaptive and fixed-node quadrature agree on the smooth Hellinger integrals to relative error below `9.62e-15`. The negative control `alpha(t)=0`, equivalent to an unsupported constant-factor `H<=TV` branch, is rejected. The verifier exits nonzero if the pointwise implication, exponent, construction validity, or numerical agreement fails.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Universal-certificate SHA `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`; seed `260203202`; one-effective-core estimate; cumulative runtime `1m15s`.

- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Exact universal output](../../evidence/raw/universal_reductions/result.json)
- [C2 analytic verifier](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Raw C1–C3 CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent quadrature output](../../evidence/raw/claim_1_3/independent_checker.json)
- [Proof-obligation output](../../evidence/raw/proof_obligations/result.json)
- [Method](../../evidence/raw/universal_reductions/method.md)
- [Limitations](../../evidence/raw/universal_reductions/limitations.md)
