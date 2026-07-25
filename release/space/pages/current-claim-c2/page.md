# C2 — Hellinger and total variation

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Corollary 2.4 has the same support and `delta>0` quantifiers as C1 and asserts

`H(f_pi,f_eta) <= max(C0, t^(-alpha(t))) t`,

with `t=TV(f_pi,f_eta)` and `alpha(t)=(2+delta)/log(max(log(1/t),e))`. This is the precise `TV^(1-o(1))` statement: `alpha(t)` tends to zero at order `1/log log(1/t)`.

## Verification chain

The proof is C1 plus the pointwise identity

`(sqrt(p)-sqrt(q))²/2 <= (p-q)²/q`,

integrated over the sample space. The independent proof-obligation checker rejects dropping the square. Therefore C2 inherits the universal quantifiers of the C1 derivation rather than being inferred from a fitted finite-data slope.

## Direct numerical corroboration

On the six explicit sharp Gaussian-mixture pairs, TV ranges from `1.807e-14` to `3.747e-38` and Hellinger distance ranges from `4.521e-13` to `1.032e-33`.

The exact ratio `H/(t^(1-alpha(t)))` is:

`4.428e-8, 1.867e-9, 8.335e-11, 3.880e-12, 1.868e-13, 9.201e-15`.

All are below `1`. The simpler control `H/TV` instead grows from `25.02` to `27,553`, illustrating why the theorem's logarithmic exponent is substantive and why checking only `H²<=TV` would miss the claim.

## Independent checker and control

Adaptive and fixed-node quadrature agree on the smooth Hellinger integrals to relative error below `9.62e-15`. The negative control `alpha(t)=0`, equivalent to an unsupported constant-factor `H<=TV` branch, is rejected. The verifier exits nonzero if the pointwise implication, exponent, construction validity, or numerical agreement fails.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Formal evidence SHA `de2c3a8fba29e433c552ce82c194196fefaaa4d8`; seed `260203202`; one-effective-core estimate; cumulative local runtime `1m35s`.

- [C2 analytic verifier](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Raw C1–C3 CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent quadrature output](../../evidence/raw/claim_1_3/independent_checker.json)
- [Proof-obligation output](../../evidence/raw/proof_obligations/result.json)
- [Method and limitations](../../evidence/raw/analytic_certificate/method.md)
