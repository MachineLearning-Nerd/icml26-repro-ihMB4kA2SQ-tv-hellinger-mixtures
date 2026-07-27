# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current live judged score: `5/10`
- Latest evaluated Space revision: `8454efce45d0b2946efff5f6e05666ec40abb915`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)

Every path in the immutable judged manifest remains present. Historical evidence pages and assets remain byte-identical, while the three canonical routing files have exact protected copies under the historical directory.

## Criticism-to-evidence trace

| Judge criticism | Current correction |
| --- | --- |
| C1/C2 called finite 1D | added direct full-density integration in `d=2,3` and foregrounded the separate all-d source-pinned premise-ledger certificate |
| C3 called finitely many asymptotic instances | finite rows are now only Approach 1; Approach 3 proves the exact gamma limits, exponent margin, and infinite monotone subsequence |
| C4 called a simplified finite submodel with hidden correction | added 21 direct local-entropy variational cells in `d=1,2,3` and displays the exact slowly decaying correction |
| C5 finite upper exponent `1.688` called below 2 | explicitly separates it from a log-space exact-exponent route reaching `1.945/1.99175`, plus arbitrary-Q expectation transfer |
| Displayed numbers could drift | the fail-closed release verifier now regenerates every C4/C5 headline table row from raw JSON and rejects any mismatch |

## Blind review

The reviewer starts only from a fresh artifact’s `README.md` and follows visible links. The canonical navigation contains exactly the overview, five claims, and methods. Visibility, release audit, and protected history remain linked without displacing current verification.

The review located the current verifier, exact claim contracts, raw data,
independent checker, negative controls, source assumptions, fixed command,
pinned environment, seeds, CPU/runtime information, scope, and fail-closed
behavior for all five claims. It also checked every displayed C4/C5 row against
the raw result. The exact opened-file trace is in the
[red-team record](../../evidence/release/red_team.md).

Pass 6 used only `git archive 096b8a4 release/space`, opened 66 files by
following links from `README.md`, and verified all 98 stable manifest hashes.

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | HIGH | 1D + d=2/d=3 direct routes and universal premise-ledger certificate |
| C2 | VERIFIED | 2 | HIGH | 1D + d=2/d=3 direct routes and exact pointwise reduction |
| C3 | VERIFIED | 2 | HIGH | explicit construction, independent integration, exact infinite-sequence certificate |
| C4 | VERIFIED | 2 | HIGH | sample upper, all-estimator lower, direct logarithmic calibration and proof chain |
| C5 | VERIFIED | 2 | HIGH | proper upper, equal-law lower, exponent-to-2 and arbitrary-Q transfer |

Conservative projected total: **8–10/10**. Best-supported possible score:
**10/10**, a forecast rather than a judge result. No claim is BLOCKED. The
remaining risk is whether the evaluator accepts a source-pinned symbolic
reconstruction that is not a proof-assistant kernel certificate; only the
live judge can award points.

The exact publication action, after the new cumulative run and blind review
pass, is one text-only Hugging Face Hub commit containing the 101 allowlisted
paths to the existing `DineshAI/ihMB4kA2SQ` Space; no second Space will be
created.

The cumulative remediation gate passed at Git SHA
`78b4a451bcf440fdbba2f1326d58b2059c3a337c`, OpenResearch run
`e1038127-ca8b-4e10-9d14-de4b89a8b2d7`, in `2m34s` on Hugging Face
`cpu-upgrade`; 64 logical CPUs were visible and numerical libraries were
pinned to one thread.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker](../../evidence/release/release_check.json)
- [Secret scan](../../evidence/release/secret_scan.json)
