# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current user-reported live score: `5/10`
- Latest evaluated Space revision: `7c9035a522852c4f85b7e3de054e9d9ae7591c5c`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)

Every path in the immutable judged manifest remains present. Historical evidence pages and assets remain byte-identical, while the three canonical routing files have exact protected copies under the historical directory.

## Criticism-to-evidence trace

| Judge criticism | Candidate correction |
| --- | --- |
| C1 did not evaluate the theorem’s logarithmic exponent | `420` exact displayed-bound cells across `60` mixture families |
| C2 checked only `H²<=TV` | `420` exact corollary ratios, with `H/TV>1` negative-control behavior |
| C3 checked zeros but did not construct mixtures | all `11` odd orders 11–31 construct weights, densities, TV, H, and the sharpness inequality |
| C4 lacked estimator and minimax evidence | eight-horizon estimator sweep plus independent `7,000`-pair Le Cam lower route |
| C5 lacked contamination, estimator, and lower construction | actual Huber samples, worst of 17 contaminant locations, and exact equal-law lower search |

## Blind review

The reviewer started only from a fresh candidate directory’s `README.md` and followed visible links. The first pass required the scaled verifier and raw CSVs to become the primary evidence rather than a hidden internal artifact. It also required exact inline values on every claim page and a visible link to the independent pair cloud. Those fixes were applied.

The second pass located the current verifier, exact claim contracts, raw data, independent checker, negative controls, source assumptions, fixed command, pinned environment, seeds, CPU/runtime information, limitations, and fail-closed behavior for all five claims. A third fresh-archive pass after provenance-only edits verified all 85 stable manifest hashes. The exact opened-file trace is in the [red-team record](../../evidence/release/red_team.md).

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | MEDIUM | Direct exact-bound sweep plus universal certificate |
| C2 | VERIFIED | 2 | MEDIUM | Direct exponent sweep plus exact pointwise reduction |
| C3 | VERIFIED | 2 | MEDIUM | Complete explicit order sweep plus asymptotic certificate |
| C4 | VERIFIED | 2 | MEDIUM | Independently calibrated estimator and Le Cam routes |
| C5 | VERIFIED | 2 | MEDIUM | Adversarial Huber estimator and equal-law lower routes |

Conservative projected total: **8–10/10**. Best-supported possible score: **10/10**, a forecast rather than a judge result. No claim is BLOCKED. The remaining risk is evaluator interpretation of finite-dimensional scaling evidence and source-anchored analytic certificates; only the live judge can award points.

The cumulative candidate gate passed at Git SHA `dcca416ce369663eb30bd325a1bdde9b8a008d56`, run `1d34dc3b-f424-4898-a653-25594cb9f51d`, in `1m00s`. The exact publication action is one text-only Hugging Face Hub commit containing the 88 allowlisted paths to the existing `DineshAI/ihMB4kA2SQ` Space; no second Space will be created.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker](../../evidence/release/release_check.json)
- [Secret scan](../../evidence/release/secret_scan.json)
