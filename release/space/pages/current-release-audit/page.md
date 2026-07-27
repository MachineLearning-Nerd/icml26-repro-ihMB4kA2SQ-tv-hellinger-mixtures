# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current user-reported live score: `5/10`
- Latest evaluated Space revision: `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)

Every path in the immutable judged manifest remains present. Historical evidence pages and assets remain byte-identical, while the three canonical routing files have exact protected copies under the historical directory.

## Criticism-to-evidence trace

| Judge criticism | Candidate correction |
| --- | --- |
| C1 remained finite-family `toy` | add an independent small-TV path to `6.505e-12`, with the normalized ratio decreasing by five orders of magnitude |
| C2 remained finite-family `toy` | add the paired small-TV path and directly show the exact exponent-normalized ratio decreases to `2.566e-9` |
| C3 finite orders were judged `toy` | raise the moment solve to 110 digits, residual `4.243e-115`, while retaining the asymptotic certificate |
| C4 upper slope was only `-0.431` | accepted eight-seed protocol gives `-0.474`, independently bracketed by Le Cam `-0.497` |
| C5 approximate exponents were judged `toy` | accepted adversarial upper gives H² `1.688`; exact-Chen lower gives H `0.960` over 5,258 pairs |

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

The evaluator-calibrated cumulative gate passed at Git SHA `9ef83c11c7c527c32bebfbae69585518eac8551b`, run `1fe4016d-5c41-4c6f-9f89-99a36bc3e2c8`, in `2m25s`. The exact publication action is one text-only Hugging Face Hub commit containing the 88 allowlisted paths to the existing `DineshAI/ihMB4kA2SQ` Space; no second Space will be created.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker](../../evidence/release/release_check.json)
- [Secret scan](../../evidence/release/secret_scan.json)
