# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current live judged score: `5/10`
- Latest evaluated Space revision: `6e08ad1e3b8345baf56246f4c50ed663d2365aa6`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)

Every path in the immutable judged manifest remains present. Historical evidence pages and assets remain byte-identical, while the three canonical routing files have exact protected copies under the historical directory.

## Criticism-to-evidence trace

| Judge criticism | Current correction |
| --- | --- |
| C1/C2 called finite-instance checks rather than proof | added a fail-closed proof graph with the exact all-dimensional quantifiers, algebraic obligations, dependency closure, independent replay, and mutated-proof controls |
| C3 called finitely many asymptotic instances | kernel pins Lemma 3.2/Theorem 3.1, checks the gamma limit and `0.3314835>0.33`, and closes the existential infinite-sequence conclusion |
| C4 called numerical support rather than exact rate proof | kernel closes C2 + pinned Jia local-entropy + `delta/2` inversion + proper-projection/all-estimator chain |
| C5 called finite-sample support rather than rate proof | kernel closes arbitrary-Q Yatracos upper and Chen equal-law all-estimator lower chains, with exact exponent limit |
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
remaining risk is evaluator interpretation of the explicit named analytic
theorem dependencies; only the live judge can award points.

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
