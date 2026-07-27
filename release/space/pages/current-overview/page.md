# Current overview

## What changed after the five `toy` verdicts

The previous candidate emphasized symbolic reductions and a small six-order construction. The latest evaluator therefore classified every claim as `toy`. This candidate keeps those exact certificates but makes a new, direct, scaled experiment the primary evidence.

| Claim | Direct test | Observed result | Verdict |
| --- | --- | --- | --- |
| C1 | Exact displayed chi-square/TV bound on `60` random compact-support families and seven amplitudes each | `420/420` pass; TV `1.156e-7`–`4.752e-2`; maximum ratio `0.008997` | VERIFIED / MEDIUM |
| C2 | Exact displayed Hellinger/TV bound on the same independently generated cells | `420/420` pass; maximum ratio `0.003787`; `H/TV` reaches `1.910` | VERIFIED / MEDIUM |
| C3 | Paper’s explicit Chebyshev mixtures for every odd order `11` through `31` | `11/11` pass; TV `3.747e-38`–`1.807e-14`; ratio `1.217`–`46.636` | VERIFIED / MEDIUM |
| C4 | 9-atom NNLS mixture estimator over eight horizons plus an independent Le Cam lower search | upper TV slope `-0.431`; lower slope `-0.500`; `7,000` valid pairs | VERIFIED / MEDIUM |
| C5 | Huber estimator at `n=200,000`, six epsilon values, worst of `17` contaminant locations, plus equal-law lower search | upper H² slope `1.671`; lower H slope `0.929`; no saturated search steps | VERIFIED / MEDIUM |

## Why these are substantive checks

C1 and C2 evaluate the actual displayed logarithmic exponent, not the generic inequalities `H²<=TV` or `H<=sqrt(chi²)`. C3 constructs the Gaussian mixtures and checks the claimed sharpness inequality, not merely the Chebyshev zeros. C4 estimates a mixture from samples over an independently chosen horizon sweep and pairs it with an all-estimator Le Cam route. C5 instantiates Huber contamination, searches adversarial locations, and separately constructs indistinguishable contaminated laws.

The independent C1/C2 doubled-grid checker has maximum relative disagreement `2.14e-6`. C3’s independent high-precision integration differs by at most `1.759e-4`, with moment residual below `2.17e-19`. The supplemental proper-Yatracos checker verifies all 171 comparison-set identities to `4.219e-15`. All five negative controls are rejected.

## Exact certificates and scope

The numerical evidence is combined with an [independently reconstructed universal-reduction certificate](../../evidence/raw/universal_reductions/result.json). It checks the exact exponent algebra, Hellinger/chi-square implication, sharpness coefficient, minimax inverse, Huber upper transfer, and equal-law lower mechanism against pinned source anchors.

The empirical sweeps cover explicit one-dimensional compact-support submodels; they are not a proof-assistant formalization of every universal quantifier. The VERIFIED verdict rests on the combination of direct scaled evidence, exact symbolic implications, source-pinned premises, independent checkers, and controls. This limitation is recorded rather than hidden.

## Evidence map

- [Scaled verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete scaled result](../../evidence/raw/scaled_direct/result.json)
- [C1/C2 raw CSV](../../evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C4 upper raw CSV](../../evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 upper raw CSV](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [7,000-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
- [Source audit](../../evidence/raw/scaled_direct/source_audit.md)
- [Cumulative fail-closed entrypoint](../../evidence/src/repro/src/run_publication_gate.py)

Historical files remain byte-preserved and reachable under **Historical rejected baseline**, but the current scaled verifier is first in navigation.
