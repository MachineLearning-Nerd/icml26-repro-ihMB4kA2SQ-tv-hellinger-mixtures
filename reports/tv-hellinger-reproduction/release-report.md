- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `7–10/10`
- Best-supported possible new score: `10/10` — forecast only, not a judge result
- Current live judged score: `5/10`

# Source-complete theorem-remediation release report

The latest machine-readable verdict evaluates Space revision
`013c7ab5979d4382ffefc3957d32a8a060e82445` and labels C1–C5
`toy, toy, toy, toy, toy`. The current total is `5/10`. This release does not
claim an increase before the live judge evaluates the new revision.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | 1 | 2 | MEDIUM | VERIFIED | 420 one-dimensional cells, 14 direct d=2/d=3 cells, and expanded all-dimensional proof transcript. Risk: not foundationally formalized. |
| C2 | 1 | 2 | MEDIUM | VERIFIED | Same direct routes plus exact pointwise identity and expanded C1 route. Risk follows the proof-transcript validation model. |
| C3 | 1 | 2 | MEDIUM | VERIFIED | 11 explicit orders, independent integration, exact gamma limits, strict exponent margin, and expanded monotone-subsequence route. |
| C4 | 1 | 2 | MEDIUM | VERIFIED | Estimator upper `-0.474`, all-estimator lower `-0.497`, 21 entropy cells, and source-pinned proof replay. |
| C5 | 1 | 2 | MEDIUM | VERIFIED | Proper upper, equal-law lower, arbitrary-Q transfer, exponent→2, and source-pinned proof replay. |

## Claim changes and blockers

- C1/C2 now expand the paper’s internal analytic nodes instead of importing
  the weighted theorem as an opaque dependency.
- C3 now expands the Chebyshev-to-mixture and monotone-subsequence route.
- C4 now exposes the source-pinned Jia import and every internal inverse,
  projection, and tail-to-risk step.
- C5 now exposes the source-pinned Ma/Chen imports and expands the Yatracos,
  continuous-amplitude, and all-estimator steps.
- BLOCKED claims: none.
- Remaining common risk: the replay is machine-checked but is not a Lean/Coq
  foundational formalization.

## Winning experiment and gate

Stacked lineage:

`historical baseline → exact construction → analytic/application certificates → proper Yatracos experiment → scaled direct evidence → three-route remediation → dependency-ledger kernel → source-complete replay → publication freeze`.

Winning scientific branch: `orx/source-complete-theorem-proof-replay`, Git
SHA `e0f51b4522fb6be068cb43ecc3121901f9627570`.

Publication branch: `orx/source-complete-publication-freeze`, created directly
from the passing scientific commit.

Complete pre-freeze gate run:
`cd74ae47-2006-4c1d-86a6-ffbd0bb2cb12`, Hugging Face `cpu-upgrade`, `1m52s`,
64 logical CPUs visible and one numerical thread. Result:
`publication_gate_passed=true`.

## Commands and compute

Fixed command on every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

New formal launch:

```bash
orx exp run f916e18f-0809-4c57-a5c1-a12bfb56230f --backend hf --flavor cpu-upgrade --timeout 1h --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim
```

The successful HF science job exposed 64 logical CPUs but pinned all numerical
libraries to one thread. The source-complete proof generator used `3.660s`;
complete runtime was `1m52s`. No GPU was used. HF cost was not exposed, so
none is invented.

## Release integrity

- Protected judged revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Current HF and judge head before upload: `013c7ab5979d4382ffefc3957d32a8a060e82445`
- Protected latest judged file count: `128`; old file set is a byte-preserved subset
- Exact text upload allowlist: `246` paths
- Stable candidate manifest: `243` paths
- Visibility rows complete: `5`
- Secret scan: PASS
- Evaluator-blind review: PASS after a fresh archive traversal

## Evidence paths

- [Canonical candidate](../../release/space/README.md)
- [Scaled result](../../release/space/evidence/raw/scaled_direct/result.json)
- [Three-route result](../../release/space/evidence/raw/three_route/result.json)
- [Route matrix](../../release/space/evidence/raw/three_route/route_matrix.json)
- [Multidimensional cells](../../release/space/evidence/raw/three_route/multidimensional_direct.csv)
- [C4 calibration](../../release/space/evidence/raw/three_route/claim_4_local_entropy.csv)
- [C5 calibration](../../release/space/evidence/raw/three_route/claim_5_asymptotic.csv)
- [C1/C2 raw cells](../../release/space/evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C3 raw construction](../../release/space/evidence/raw/claim_1_3/raw_results.csv)
- [C4 estimator rows](../../release/space/evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination rows](../../release/space/evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../release/space/evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../release/space/evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../release/space/evidence/raw/scaled_direct/negative_control.json)
- [Kernel-checked proof](../../release/space/evidence/raw/kernel_certificate/proof_certificate.json)
- [Independent proof replay](../../release/space/evidence/raw/kernel_certificate/independent_checker.json)
- [Source-complete proof transcript](../../release/space/evidence/raw/source_complete_proof_replay/proof_transcript.md)
- [Independent source-complete checker](../../release/space/evidence/raw/source_complete_proof_replay/independent_checker.json)
- [Visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Blind-review record](../../release/space/evidence/release/red_team.md)
- [Upload allowlist](../../release/space/evidence/release/upload_allowlist.txt)
- [SHA-256 manifest](../../release/space/evidence/release/candidate_manifest.sha256)

Exact publication action: upload only the 246 allowlisted text paths in one
Hugging Face Hub commit to the existing `DineshAI/ihMB4kA2SQ` Space, verify
the returned revision by exact-revision download and hash traversal, then
mirror the published text paths and public report to GitHub `main`. No second
Space will be created.
