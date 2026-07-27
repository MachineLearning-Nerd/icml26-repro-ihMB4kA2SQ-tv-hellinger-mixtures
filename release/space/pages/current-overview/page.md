# Executive summary

Every claim is tested at its displayed formula or construction. The fixed
command regenerates all raw files, runs independent checkers and negative
controls, and exits nonzero on any failed gate.

| Claim | Paper object tested | Observed evidence |
| --- | --- | --- |
| C1 | `sqrt(chi²) <= max(C0,t^-alpha(t))t` with the stated `alpha(t)` | `420/420` compact-support cells pass with `C0=1`; controlled TV reaches `6.505e-12` |
| C2 | `H <= max(C0,t^-alpha(t))t` and its `1/log log` correction | `420/420` pass; small-TV normalized ratio falls to `2.566e-9` |
| C3 | Explicit Chebyshev Gaussian-mixture sharpness construction | all odd orders `11,...,31` pass; TV reaches `3.747e-38`; margin grows `1.217` to `46.636` |
| C4 | TV minimax rate, with sample upper and all-estimator lower routes | upper `n^-0.474`; lower `n^-0.497`; `5,258` valid Le Cam pairs |
| C5 | Huber-contamination Hellinger rate, with worst-Q upper and equal-law lower routes | upper `H² ~ epsilon^1.688`; lower `H ~ epsilon^0.960` (`H² ~ epsilon^1.920`) |

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

The exact source statements, compact-support assumptions, arbitrary-contaminant
quantifier, symbolic reductions, and finite direct experiments are separated
on each claim page. Direct experiments use explicit one-dimensional submodels;
dimension extension and universal quantifier handling are recorded in the
[source-pinned reduction certificate](../../evidence/raw/universal_reductions/result.json).

## Evidence

- [Executable scaled verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Complete machine-readable result](../../evidence/raw/scaled_direct/result.json)
- [C1/C2 raw cells](../../evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C4 estimator rows](../../evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination rows](../../evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
