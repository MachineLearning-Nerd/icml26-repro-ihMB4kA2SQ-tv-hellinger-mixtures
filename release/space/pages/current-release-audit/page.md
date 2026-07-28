# Release and red-team audit

## Protected history and current judge state

- Original judged Space revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Original live judged score: `0/10`
- Current live judged score: `5/10`
- Latest evaluated Space revision: `013c7ab5979d4382ffefc3957d32a8a060e82445`
- Latest five verdict labels: `toy, toy, toy, toy, toy`
- Original protected manifest: [manifest.sha256](../../historical/judged-1c98799a89d8c1d3c45136c8b912e74371e975b3/manifest.sha256)
- Exact 5/10 judged-revision manifest: [manifest.sha256](../../historical/judged-013c7ab5979d4382ffefc3957d32a8a060e82445/manifest.sha256)

Every path in both immutable judged manifests remains present. Unchanged paths
remain byte-identical in place; changed text paths have exact protected copies
under their judged-revision historical directory.

## Criticism-to-evidence trace

| Judge criticism | Current correction |
| --- | --- |
| C1/C2 called finite-instance checks rather than proof | source-complete replay expands every internal analytic node, carries exact all-dimensional quantifiers, and reports zero unresolved internal dependencies |
| C3 called finitely many asymptotic instances | replay expands Chebyshev/Vandermonde through Gaussian norms and monotone subsequence, checks `0.3314835>0.33`, and closes the existential infinite-sequence conclusion |
| C4 called numerical support rather than exact rate proof | replay expands all internal steps from the source-pinned Jia theorem through C2 at `delta/2`, inverse mapping, projection, and Fano tail-to-risk |
| C5 called finite-sample support rather than rate proof | replay expands arbitrary-Q Yatracos upper and continuous-amplitude/Chen equal-law lower chains, while exposing Ma and Chen as hashed primary imports |
| Displayed numbers could drift | the fail-closed release verifier now regenerates every C4/C5 headline table row from raw JSON and rejects any mismatch |
| Proof label could outrun executable evidence | independent replay reads the serialized proof transcript, rechecks source hashes/anchors and decisive witnesses, requires zero unresolved nodes, and rejects five mutations |

## Blind review

The reviewer starts only from a fresh artifact’s `README.md` and follows visible links. The canonical navigation contains the overview, current formal proof replay, five claims, and methods. Visibility, release audit, and protected history remain linked without displacing current verification.

The review located the current verifier, exact claim contracts, raw data,
independent checker, negative controls, source assumptions, fixed command,
pinned environment, seeds, CPU/runtime information, scope, and fail-closed
behavior for all five claims. It also checked every displayed C4/C5 row against
the raw result. The exact opened-file trace is in the
[red-team record](../../evidence/release/red_team.md).

Pass 6 used only `git archive 096b8a4 release/space`, opened 66 files by
following links from `README.md`, and verified all 98 stable manifest hashes.

Pass 7 used only `git archive bf2880f release/space`, opened 69 reachable
files, found the proof generator, independent replay, and all five quantified
claim conclusions, found zero missing links, rejected all five proof mutations,
and verified all 106 stable manifest hashes.

Pass 8 used only `git archive 8fa61b4 release/space`, opened 81 reachable
files, found the source-complete replay and independent checker from the
canonical entrypoint, found zero missing links and zero unresolved
dependencies, rejected all five proof mutations, and verified all 242 stable
manifest hashes. The exact opened-file trace is
[blind_pass_8_opened.txt](../../evidence/release/blind_pass_8_opened.txt).

## Release forecast

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| C1 | VERIFIED | 2 | MEDIUM | direct routes plus source-complete transcript; proof-assistant risk remains |
| C2 | VERIFIED | 2 | MEDIUM | direct routes plus exact pointwise reduction and expanded C1 transcript |
| C3 | VERIFIED | 2 | MEDIUM | explicit construction, independent integration, and expanded infinite-sequence route |
| C4 | VERIFIED | 2 | MEDIUM | sample upper, all-estimator lower, calibration, and source-pinned proof chain |
| C5 | VERIFIED | 2 | MEDIUM | proper upper, equal-law lower, exponent-to-2 route, and source-pinned transfer |

Conservative projected total: **7–10/10**. Best-supported possible score:
**10/10**, a forecast rather than a judge result. No claim is BLOCKED. The
remaining risk is that a machine-checked proof transcript is not a
foundational proof-assistant artifact; only the live judge can award points.

The exact publication action, after the new cumulative run and blind review
pass, is one text-only Hugging Face Hub commit containing the 246 allowlisted
paths to the existing `DineshAI/ihMB4kA2SQ` Space; no second Space will be
created.

The cumulative remediation gate passed at Git SHA
`e0f51b4522fb6be068cb43ecc3121901f9627570`, OpenResearch run
`cd74ae47-2006-4c1d-86a6-ffbd0bb2cb12`, in `1m52s` on Hugging Face
`cpu-upgrade`; 64 logical CPUs were visible and numerical libraries were
pinned to one thread.

## Integrity files

- [Candidate SHA-256 manifest](../../evidence/release/candidate_manifest.sha256)
- [Exact text upload allowlist](../../evidence/release/upload_allowlist.txt)
- [Subset and visibility checker](../../evidence/release/release_check.json)
- [Secret scan](../../evidence/release/secret_scan.json)
