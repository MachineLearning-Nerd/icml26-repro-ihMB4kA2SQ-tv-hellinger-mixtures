# Executive summary

Every claim has three materially different routes: direct evidence, an
independent checker or lower-bound route, and a source-pinned
symbolic/asymptotic certificate. The remediation adds a fourth shared layer:
a small proof kernel that closes each theorem dependency graph, recomputes the
exact identities and limits, and rejects one mutated proof object per claim.
An independent replay checker reads the saved certificate from scratch. The
fixed command regenerates every raw file and exits nonzero on any failed gate.

| Claim | Route 1 | Route 2 | Route 3 |
| --- | --- | --- | --- |
| C1 | 420 1D exact-bound cells | 14 direct `d=2,3` cells | all-`d` proof chain |
| C2 | 420 direct Hellinger cells | 14 direct `d=2,3` cells | pointwise universal reduction |
| C3 | odd orders `11,...,31` | independent high-precision integration | exact infinite-sequence limits |
| C4 | sample upper `n^-0.474` | Le Cam lower `n^-0.497` | 21 local-entropy/log-correction cells |
| C5 | proper estimator/worst-Q upper | equal-law all-estimator lower | exponent→2 plus arbitrary-Q transfer |

## Why the checks are substantive

C1/C2 evaluate the paper’s logarithmic exponent, rather than only the generic
`H²<=TV` inequality. C3 constructs the probability measures and convolves them
with the Gaussian kernel, rather than checking polynomial roots alone. C4 runs
an estimator on samples and independently maximizes a Le Cam certificate. C5
generates contaminated samples, maximizes over 17 fixed contaminant locations,
and separately constructs observationally identical contaminated laws at the
exact boundary `TV<=epsilon/(1-epsilon)`.

The independent C1/C2 grid has maximum relative disagreement `2.135e-6`.
C3’s second high-precision integration engine differs by at most `1.759e-4`,
with moment residual `4.243e-115`. The finite Yatracos checker verifies all
`171` comparison-set identities to `<5e-15`. All negative controls are rejected.

The new multidimensional cells have zero C1/C2 violations; the higher-order
checker disagrees by at most `5.739e-4`, while exact tensor-factorization
identities agree to `5.315e-16`. C4 displays its slowly decaying logarithmic
correction directly. C5's log-space route reaches effective H² exponents
`1.945` (upper) and `1.99175` (lower), showing why the finite fitted `1.688`
is not the asymptotic limit.

Universal quantifiers are handled by the
[source-pinned reduction certificate](../../evidence/raw/universal_reductions/result.json)
and the [kernel-checked proof graph](../../evidence/raw/kernel_certificate/proof_certificate.json),
whose premises and quantified conclusions are explicit. The
[independent replay](../../evidence/raw/kernel_certificate/independent_checker.json)
verified all five claims and rejected all five proof mutations.

## Evidence

- [Executable scaled verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Executable three-route verifier](../../evidence/src/repro/src/run_three_route_evidence.py)
- [Proof-kernel generator](../../evidence/src/repro/src/verify_kernel_certificate.py)
- [Independent proof replay](../../evidence/src/repro/src/check_kernel_certificate.py)
- [Kernel-checked certificate](../../evidence/raw/kernel_certificate/proof_certificate.json)
- [Three-route result](../../evidence/raw/three_route/result.json)
- [Three-route matrix](../../evidence/raw/three_route/route_matrix.json)
- [d=2/d=3 cells](../../evidence/raw/three_route/multidimensional_direct.csv)
- [C4 logarithmic calibration](../../evidence/raw/three_route/claim_4_local_entropy.csv)
- [C5 asymptotic calibration](../../evidence/raw/three_route/claim_5_asymptotic.csv)
- [Complete machine-readable result](../../evidence/raw/scaled_direct/result.json)
- [C1/C2 raw cells](../../evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C4 estimator rows](../../evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination rows](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
