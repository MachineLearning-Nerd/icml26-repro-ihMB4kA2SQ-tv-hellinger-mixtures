# C3 — sharp Chebyshev construction

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Theorem 3.1 asserts the existence of two sequences of probability measures supported on `[-M,M]` such that `TV_n` decreases to zero, every `TV_n<e^-e`, and

`H_n >= TV_n^(1-0.33/log log(1/TV_n))`

for every relabeled sequence index. Lemma 3.2 supplies the explicit odd-order construction from the zeros

`theta_j=cos((2j+1)pi/(2n+2))`.

## Exact asymptotic certificate

SymPy evaluates the two gamma-formula limits exactly:

`lim_n log(||x^n/n!||_1)/(n log n) = lim_n log(||x^n/n!||_2)/(n log n) = -1/2`.

It also proves the exact coefficient margin

`log(2)-200/553-33/100 > 0`

and the corresponding exponent-transfer limit. The source's direct relabel does not establish monotone TV, so the certificate uses the standard recursive rule: from any positive sequence tending to zero, select each next index with value below both its predecessor and `1/(j+1)`. The resulting subsequence decreases to zero and retains every eventual inequality. This establishes the existential sequence conditional on the source-anchored Chebyshev construction and uniform tail bounds.

## Constructed mixtures and finite corroboration

The reproduction solves the stated moment system, checks nonnegative probability weights, constructs all three mixture transformations from the paper, and integrates the resulting densities. For `n=11,15,19,23,27,31`, the sharpness ratios are:

| n | TV | H | required RHS | H/RHS |
| ---: | ---: | ---: | ---: | ---: |
| 11 | `1.807e-14` | `4.521e-13` | `3.713e-13` | `1.217` |
| 15 | `5.704e-19` | `5.823e-17` | `2.327e-17` | `2.502` |
| 19 | `1.319e-23` | `5.474e-21` | `1.059e-21` | `5.171` |
| 23 | `2.335e-28` | `3.933e-25` | `3.664e-26` | `10.733` |
| 27 | `3.270e-33` | `2.235e-29` | `9.979e-31` | `22.400` |
| 31 | `3.747e-38` | `1.032e-33` | `2.214e-35` | `46.636` |

Chebyshev residuals are below `2.12e-14`; moment residuals are below `2.17e-19`.

The available coefficient is

`log(2)-2/5.53 = 0.331483527757052 > 0.33`.

The six rows directly instantiate the paper’s construction, but the universal/asymptotic verdict comes from the exact certificate above, not from extrapolating these orders.

## Independent checker and controls

Adaptive Gauss–Kronrod and 1,536-node Gauss–Hermite quadrature agree; maximum relative TV disagreement is `3.33e-5` despite TV reaching `1e-38`. Controls reject wrong Chebyshev nodes, coefficient `0.50`, coefficient `0.34`, and the claim that the source's direct relabel is automatically monotone.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Universal-certificate SHA `be9b1613eb321a1eb7c2f467883e4d27e8540cb2`; seed `260203202`; one-effective-core estimate; cumulative runtime `1m15s`.

- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Exact universal output](../../evidence/raw/universal_reductions/result.json)
- [Raw construction CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent checker JSON](../../evidence/raw/claim_1_3/independent_checker.json)
- [Analytic certificate JSON](../../evidence/raw/analytic_certificate/result.json)
- [Construction verifier](../../evidence/src/repro/src/verify_claims_1_3.py)
- [Analytic verifier](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Limitations](../../evidence/raw/universal_reductions/limitations.md)
