# Current overview

## Central question and result

For unit-covariance Gaussian location mixtures whose mixing laws are supported in `[-M,M]^d`, how much larger can Hellinger or chi-square distance be than total variation when TV is tiny?

This reproduction audits the exact theorem quantifiers, reconstructs their analytic implications, instantiates the paper's explicit Chebyshev mixtures, and independently recomputes the distances with adaptive Gauss–Kronrod and fixed-node Gauss–Hermite quadrature. All five claim contracts are **VERIFIED at MEDIUM confidence**. “VERIFIED” here is a scientific conclusion supported by the displayed proof/evidence chain; only the live judge can award points.

| Claim | Verdict | Confidence | Direct basis |
| --- | --- | --- | --- |
| C1 | VERIFIED | MEDIUM | Source-pinned universal derivation; exact exponent/tail algebra; six faithful mixtures; two integration engines |
| C2 | VERIFIED | MEDIUM | C1 plus independently checked pointwise `H²<=chi²`; exact exponent ratios |
| C3 | VERIFIED | MEDIUM | Explicit valid mixing laws, exact norm asymptotics, six sharpness inequalities, subsequence repair |
| C4 | VERIFIED | MEDIUM | Jia primary-source Fano contract plus reconstructed upper/lower minimax implications and `delta/2` inverse repair |
| C5 | VERIFIED | MEDIUM | Proper Yatracos upper proof, expectation transfer, Chen primary-source lower proof, continuous-amplitude repair |

## Headline observed evidence

For `n=11,15,19,23,27,31`, the exact sharpness ratio

`H_n / TV_n^(1-0.33/log log(1/TV_n))`

is respectively:

`1.217, 2.502, 5.171, 10.733, 22.400, 46.636`.

Every value is above the required threshold `1`. The deliberately wrong coefficient `0.50` is rejected. Independent fixed-node quadrature agrees with adaptive integration to relative error at most `3.33e-5` for the nonsmooth TV integral and `9.62e-15` for the smooth Hellinger/chi-square integrals.

## What changed from the 0/10 baseline

The judged baseline only located LaTeX tokens and evaluated nearby formulas. The current artifact supplies exact claim contracts and quantifiers, valid constructed mixtures, raw distances, symbolic proof implications, primary-source dependency audits, independent checkers, negative controls, fail-closed executables, pinned environment/SHAs, CPU/runtime records, limitations, and direct raw links.

## Evidence map

- [Raw C1–C3 CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Independent quadrature JSON](../../evidence/raw/claim_1_3/independent_checker.json)
- [C1–C3 analytic certificate](../../evidence/raw/analytic_certificate/result.json)
- [C4–C5 application certificate](../../evidence/raw/application_certificate/result.json)
- [Primary dependency audit](../../evidence/raw/primary_dependencies/result.json)
- [Current executable source](../../evidence/src/repro/src/run_publication_gate.py)

Historical pages are labeled and placed last in navigation. They remain byte-preserved evidence, not the default verification.
