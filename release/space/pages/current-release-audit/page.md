# Release and red-team audit

## Protected history

- Judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Previous live judged score: `0/10`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)
- Subset rule: every path present at the judged revision is present in this candidate. Historical claim pages and assets are byte-identical. The three canonical routing files have exact historical copies under the protected directory.

## Blind review

The reviewer began only at `README.md` and the evaluator rubric. The first pass located the science but flagged ambiguous historical navigation and incomplete direct raw links. The candidate was revised to put current pages first, label the old tree exactly “Historical rejected baseline,” add direct code/raw/limitations links to every claim, and include this matrix. The second pass located all required fields for all five claims without repository knowledge.

Detailed files opened and pass-by-pass findings are in the [red-team record](../../evidence/release/red_team.md).

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | MEDIUM | Exact theorem and direct construction visible |
| C2 | VERIFIED | 2 | MEDIUM | Exact corollary and exponent visible |
| C3 | VERIFIED | 2 | MEDIUM | Construction, inequality, and repair visible |
| C4 | VERIFIED | 2 | MEDIUM | Minimax proof chain and primary dependency visible |
| C5 | VERIFIED | 2 | MEDIUM | Upper/lower proof chain and repairs visible |

Conservative projected total: **6–10/10**. Best-supported possible score: **10/10**, a forecast rather than a judge result. Remaining risk is evaluator acceptance of independently reconstructed analytic certificates and source-proof repairs without proof-assistant formalization.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker output](../../evidence/release/release_check.json)
- [Secret scan output](../../evidence/release/secret_scan.json)
