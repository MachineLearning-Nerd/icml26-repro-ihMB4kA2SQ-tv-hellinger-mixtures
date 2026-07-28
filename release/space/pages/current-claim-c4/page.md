# C4 — minimax TV learning rate

## Exact theorem

For every `delta>0` and every Hellinger-compact
`P` inside the bounded-support Gaussian-mixture class, Theorem 4.3 states

`epsilon_n^(2(1+(2+delta)/log(max(log(1/epsilon_n),e))))`

`<= inf_est sup_P E[TV(P,est)^2] <= epsilon_n^2`

up to constants. Here
`epsilon_n^2 ~ inf_epsilon {epsilon^2 + log N_H,loc(P,epsilon)/n}`.
The arbitrary-estimator and proper-estimator risks agree up to constants.

## Approach 1 — sample upper-risk route

The upper route samples a fixed 9-atom mixture and fits nonnegative mixture
weights on an independently fixed 121-point support grid. Eight replicates are
run at each horizon:

| n | 200 | 500 | 1,000 | 2,000 | 5,000 | 10,000 | 20,000 | 50,000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean TV | .05952 | .04880 | .03175 | .02303 | .01697 | .00976 | .00734 | .00488 |

The fitted TV exponent is `-0.47376`, hence squared-TV exponent `-0.94752`.
A fixed-estimator control has slope `0` and is rejected.

## Approach 2 — all-estimator lower route

This route is independent of that estimator. It generates `5,257` valid
random compact-support pairs and adds one Chebyshev extremal pair. At each
horizon it maximizes the exact Le Cam certificate

`(TV(P0,P1)/2) * (1 - upper_bound_TV(P0^n,P1^n))`,

using product affinity `(1-H(P0,P1)^2)^n`. The lower TV exponent is `-0.49711`
(squared-risk exponent `-0.99423`). Thus upper and all-estimator lower routes
bracket the same near-`n^-1/2` TV scale.

## Approach 3 — local-entropy correction and proof-kernel replay

The new calibration independently minimizes

`epsilon² + log(1/epsilon)^(d+1)/n`

over a broad log-scale grid for `d=1,2,3`, then evaluates the exact theorem
lower power. It exposes, rather than hides, the correction
`(2+delta)/log log(1/epsilon_n)`:

| d | log10 n | log(1/epsilon_n) | correction (`delta=.5`) |
| ---: | ---: | ---: | ---: |
| 1 | 4 | `3.922` | `1.8294` |
| 1 | 12 | `12.551` | `.9882` |
| 1 | 40 | `44.158` | `.6600` |
| 1 | 80 | `89.854` | `.5558` |

All `21` `(d,n)` calibration cells are downloadable. The correction is
positive and decreases at every horizon within each dimension. A fixed
exponent would erase this measured gap and is rejected.

The source-pinned symbolic checker separately reconstructs the local-entropy
definition, Fano event, monotone inverse, projection-to-proper-estimator step,
and the exact logarithmic exponent. It also detects and repairs the
same-`delta` inversion issue by applying the theorem’s `for every delta>0`
quantifier at `delta/2`.
The separate finite Yatracos checker verifies all `171` comparison-set
identities to `<5e-15`.

The current source-complete replay expands every internal node from the
source-pinned Jia local-entropy import through proper projection, C2 metric
conversion at `delta/2`, inverse mapping, and the Fano tail-to-risk step. It
reports **zero unresolved** internal dependencies and names the Jia theorem as
an explicit external primary-source import. The separate
`check_source_complete_proof_replay.py` checker rejects the invalid
same-`delta` inversion.

## Reproduce

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seeds `260203514` and `260207502`; one effective numerical core; CPU only.

- [Verifier](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Three-route verifier](../../evidence/src/repro/src/run_three_route_evidence.py)
- [Three-route matrix](../../evidence/raw/three_route/route_matrix.json)
- [Local-entropy calibration CSV](../../evidence/raw/three_route/claim_4_local_entropy.csv)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Estimator CSV](../../evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [5,258-pair cloud](../../evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact reduction](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Proof-kernel generator](../../evidence/src/repro/src/verify_kernel_certificate.py)
- [Independent proof replay](../../evidence/src/repro/src/check_kernel_certificate.py)
- [Kernel certificate](../../evidence/raw/kernel_certificate/proof_certificate.json)
- [Kernel replay output](../../evidence/raw/kernel_certificate/independent_checker.json)
- [Source-complete generator](../../evidence/src/repro/src/verify_source_complete_proof_replay.py)
- [Independent source-complete checker](../../evidence/src/repro/src/check_source_complete_proof_replay.py)
- [Current proof transcript](../../evidence/raw/source_complete_proof_replay/proof_transcript.md)
- [Current proof object](../../evidence/raw/source_complete_proof_replay/proof_replay.json)
- [Jia source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Scope and deviations](../../evidence/raw/scaled_direct/limitations.md)
