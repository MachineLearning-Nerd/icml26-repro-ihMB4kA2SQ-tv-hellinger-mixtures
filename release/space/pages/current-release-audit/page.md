# Release and red-team audit

## Protected history

- Judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Previous live judged score: `0/10`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)
- Subset rule: every path present at the judged revision is present in this candidate. Historical claim pages and assets are byte-identical. The three canonical routing files have exact historical copies under the protected directory.

The later live verdict dataset evaluated published revision `7c0bf4dc84363ff022c388d366397e3b295010a6` on `2026-07-25T06:40:51Z` and rated C1–C5 `toy, toy, toy, inconclusive, inconclusive`. The dataset has no numeric total-score field, so no new numeric live score is invented. This candidate directly addresses that verdict’s finite-vs-universal and missing-estimator criticisms.

## Blind review

The reviewer began only at a fresh candidate download’s `README.md` and the evaluator rubric. The first pass treated finite sweeps as corroboration and flagged the hidden universal certificate, old historical navigation children, missing estimator data, and the misleading amplitude-invariance wording. The candidate was revised to place the exact reductions first, remove historical children while preserving every old file, expose the proper Yatracos experiment and nonvacuity audit, and correct the lower-bound wording. The second pass located all required fields for all five claims without repository knowledge.

Detailed files opened and pass-by-pass findings are in the [red-team record](../../evidence/release/red_team.md).

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | MEDIUM | Exact theorem and direct construction visible |
| C2 | VERIFIED | 2 | MEDIUM | Exact corollary and exponent visible |
| C3 | VERIFIED | 2 | MEDIUM | Construction, inequality, and repair visible |
| C4 | VERIFIED | 2 | MEDIUM | Minimax reduction plus actual proper-estimator and finite-domain lower evidence visible |
| C5 | VERIFIED | 2 | MEDIUM | Universal reduction plus actual contamination, risk, checker, and lower evidence visible |

Conservative projected total: **4–8/10**. Best-supported possible score: **10/10**, a forecast rather than a judge result. Remaining risk is evaluator acceptance of independently reconstructed analytic certificates and source-proof repairs without proof-assistant formalization; finite experiments cannot by themselves establish the infinite-class/asymptotic quantifiers.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker output](../../evidence/release/release_check.json)
- [Secret scan output](../../evidence/release/secret_scan.json)
