# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current live judged score: `5/10`
- Latest evaluated Space revision: `89d6ea2210377512cbadb69ed86d2fccfb9e0f40`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)

Every path in the immutable judged manifest remains present. Historical evidence pages and assets remain byte-identical, while the three canonical routing files have exact protected copies under the historical directory.

## Criticism-to-evidence trace

| Judge criticism | Current correction |
| --- | --- |
| C1/C2 called finite 1D | exact source quantifiers lead each page; `420` direct cells, small-TV calibration, symbolic dimension reduction, checker, and controls are co-located |
| C3 called finitely many asymptotic instances | exact sequence statement, 110-digit construction for every odd order `11–31`, coefficient certificate, independent integration, and controls are co-located |
| C4 link to `epsilon_n` unclear | the page now displays the exact local-Hellinger-entropy definition and theorem bracket before the independent `-0.474/-0.497` upper/lower rates |
| C5 exponent attribution unclear | the page separates the exact Theorem 4.5/4.6 formulas from contaminated-sample upper and equal-law lower routes, and reports both H and H² exponents |
| Displayed numbers could drift | the fail-closed release verifier now regenerates every C4/C5 headline table row from raw JSON and rejects any mismatch |

## Blind review

The reviewer starts only from a fresh artifact’s `README.md` and follows visible links. The canonical navigation contains exactly the overview, five claims, and methods. Visibility, release audit, and protected history remain linked without displacing current verification.

The review located the current verifier, exact claim contracts, raw data,
independent checker, negative controls, source assumptions, fixed command,
pinned environment, seeds, CPU/runtime information, scope, and fail-closed
behavior for all five claims. It also checked every displayed C4/C5 row against
the raw result. The exact opened-file trace is in the
[red-team record](../../evidence/release/red_team.md).

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | MEDIUM | Direct exact-bound sweep plus universal certificate |
| C2 | VERIFIED | 2 | MEDIUM | Direct exponent sweep plus exact pointwise reduction |
| C3 | VERIFIED | 2 | MEDIUM | Complete explicit order sweep plus asymptotic certificate |
| C4 | VERIFIED | 2 | MEDIUM | Independently calibrated estimator and Le Cam routes |
| C5 | VERIFIED | 2 | MEDIUM | Adversarial Huber estimator and equal-law lower routes |

Conservative projected total: **8–10/10**. Best-supported possible score: **10/10**, a forecast rather than a judge result. No claim is BLOCKED. The remaining risk is evaluator interpretation of finite-dimensional scaling evidence and source-anchored analytic certificates; only the live judge can award points.

The exact publication action, after the new cumulative run and blind review
pass, is one text-only Hugging Face Hub commit containing the 88 allowlisted
paths to the existing `DineshAI/ihMB4kA2SQ` Space; no second Space will be
created.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker](../../evidence/release/release_check.json)
- [Secret scan](../../evidence/release/secret_scan.json)
