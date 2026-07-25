# C3 — sharp Chebyshev construction

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Theorem 3.1 asserts the existence of two sequences of probability measures supported on `[-M,M]` such that `TV_n` decreases to zero, every `TV_n<e^-e`, and

`H_n >= TV_n^(1-0.33/log log(1/TV_n))`

for every relabeled sequence index. Lemma 3.2 supplies the explicit odd-order construction from the zeros

`theta_j=cos((2j+1)pi/(2n+2))`.

## Constructed mixtures and observed inequality

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

## Analytic certificate and source repair

Exact gamma formulas for the `L1` and `L2` norms of `x^n/n!` yield the common normalized logarithmic rate `1/2`. A high-precision asymptotic probe gives `0.495657` and `0.492647`. The available coefficient is

`log(2)-2/5.53 = 0.331483527757052 > 0.33`.

The source's direct relabel `n -> 2(n+N0)+1` does not itself prove monotone TV. The verified existential statement is repaired by recursively selecting a strictly decreasing subsequence from the positive sequence converging to zero. Subsequencing preserves every distance inequality.

## Independent checker and controls

Adaptive Gauss–Kronrod and 1,536-node Gauss–Hermite quadrature agree; maximum relative TV disagreement is `3.33e-5` despite TV reaching `1e-38`. Controls reject wrong Chebyshev nodes, coefficient `0.50`, coefficient `0.34`, and the claim that the source's direct relabel is automatically monotone.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Formal evidence SHA `de2c3a8fba29e433c552ce82c194196fefaaa4d8`; seed `260203202`; one-effective-core estimate; cumulative local runtime `1m35s`.

- [Raw construction CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent checker JSON](../../evidence/raw/claim_1_3/independent_checker.json)
- [Analytic certificate JSON](../../evidence/raw/analytic_certificate/result.json)
- [Construction verifier](../../evidence/src/repro/src/verify_claims_1_3.py)
- [Analytic verifier](../../evidence/src/repro/src/verify_analytic_certificate.py)
- [Limitations](../../evidence/raw/analytic_certificate/limitations.md)
