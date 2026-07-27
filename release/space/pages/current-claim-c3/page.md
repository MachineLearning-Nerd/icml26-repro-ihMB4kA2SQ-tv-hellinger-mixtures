# C3 — sharp Chebyshev construction

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Theorem 3.1 asserts the existence of compactly supported mixing-law sequences for which `TV_n` decreases to zero and

`H_n >= TV_n^(1-0.33/log log(1/TV_n))`.

Lemma 3.2 supplies the explicit odd-order Chebyshev construction with zeros

`theta_j=cos((2j+1)pi/(2n+2))`.

## Complete explicit order sweep

The verifier solves the paper’s moment system, checks probability weights, constructs the Gaussian location mixtures, and evaluates every odd order from `11` through `31` at 100-digit working precision.

| n | TV | H / required RHS |
| ---: | ---: | ---: |
| 11 | `1.807e-14` | `1.217` |
| 13 | `1.049e-16` | `1.742` |
| 15 | `5.704e-19` | `2.502` |
| 17 | `2.853e-21` | `3.610` |
| 19 | `1.319e-23` | `5.171` |
| 21 | `5.723e-26` | `7.447` |
| 23 | `2.335e-28` | `10.734` |
| 25 | `8.977e-31` | `15.506` |
| 27 | `3.270e-33` | `22.399` |
| 29 | `1.132e-35` | `32.365` |
| 31 | `3.747e-38` | `46.636` |

All `11/11` sharpness cells pass. The maximum moment residual is `2.17e-19`, and the minimum probability weight remains positive.

## Asymptotic certificate, checker, and controls

The symbolic route checks the exact gamma limits, the coefficient margin

`log(2)-2/5.53 = 0.3314835 > 0.33`,

and a valid monotone-subsequence selection. An independent fixed-node Gauss–Hermite engine at 20 extra digits agrees with the primary construction to maximum relative error `1.759e-4`.

Controls reject the wrong Chebyshev nodes and the stronger coefficient `0.50`. Each control must fail for the intended reason, and every accepted row must pass, or the verifier exits nonzero.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seed `260203202`; one effective core; no GPU. The full row data are in the [construction CSV](../../evidence/raw/claim_1_3/raw_results.csv).

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Construction verifier](../../evidence/src/repro/src/verify_claims_1_3.py)
- [Complete scaled result](../../evidence/raw/scaled_direct/result.json)
- [Independent construction checker](../../evidence/raw/claim_1_3/independent_checker.json)
- [Negative controls](../../evidence/raw/claim_1_3/negative_control.json)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Universal certificate](../../evidence/raw/universal_reductions/result.json)
- [Source audit](../../evidence/raw/claim_1_3/source_audit.md)
- [Method](../../evidence/raw/claim_1_3/method.md)
- [Limitations](../../evidence/raw/claim_1_3/limitations.md)
