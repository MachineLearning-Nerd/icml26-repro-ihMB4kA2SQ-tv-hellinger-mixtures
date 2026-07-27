# C2 — Hellinger and total variation

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Corollary 2.4 has the same compact-support and `delta>0` quantifiers as C1 and asserts

`H(f_pi,f_eta) <= max(C0, t^(-alpha(t))) t`,

where `t=TV(f_pi,f_eta)` and `alpha(t)=(2+delta)/log(max(log(1/t),e))`. This is the precise `TV^(1-o(1))` bound: the exponent correction decays as `1/log log(1/t)`.

## Direct scaled test

The exact Hellinger bound is evaluated—not the weaker generic inequality `H²<=TV`—on the same `60` compact-support families and `420` cells:

| Quantity | Result |
| --- | ---: |
| exact-bound violations | `0 / 420` |
| maximum `H / [max(1,t^-alpha(t))t]` | `0.00378670` |
| observed `H/TV` range | `0.7584` to `1.9101` |
| TV range | `1.15577e-7` to `4.75248e-2` |

The fact that `H/TV` exceeds one supplies a real negative control against replacing the logarithmic exponent with a constant-factor linear claim. Every cell is in the [raw CSV](../../evidence/raw/scaled_direct/claim_1_2_raw.csv).

## Exact certificate, checker, and control

For symbolic positive densities `x,y`, the independent verifier simplifies

`((x-y)²/y) / (sqrt(x)-sqrt(y))²`

to `(sqrt(x/y)+1)²`, establishing the pointwise Hellinger/chi-square implication before integration. The doubled-grid checker agrees to maximum relative error `2.135e-6`. Controls reject both a missing square and `alpha(t)=0`; failures exit nonzero.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seed `260203214`; one effective numerical core; HF `cpu-upgrade` for the uncertain first run; no GPU.

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Universal certificate](../../evidence/raw/universal_reductions/result.json)
- [Claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
- [Source audit](../../evidence/raw/scaled_direct/source_audit.md)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
