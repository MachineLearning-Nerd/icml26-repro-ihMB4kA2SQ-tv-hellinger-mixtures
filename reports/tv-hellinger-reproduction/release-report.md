- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` — forecast only, not a judge result
- Current live judged score: `5/10`

# Three-route claim-remediation release report

The latest machine-readable verdict evaluates Space revision
`6e08ad1e3b8345baf56246f4c50ed663d2365aa6` and labels C1–C5
`toy, toy, toy, toy, toy`. The current total is `5/10`. This release does not
claim an increase before the live judge evaluates the new revision.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | 1 | 2 | HIGH | VERIFIED | 420 one-dimensional cells, 14 direct d=2/d=3 cells, and a kernel-checked all-dimensional proof graph with independent replay. |
| C2 | 1 | 2 | HIGH | VERIFIED | Same direct routes plus exact pointwise Hellinger/chi-square identity under all positive densities. Risk follows C1’s pinned analytic premises. |
| C3 | 1 | 2 | HIGH | VERIFIED | 11 explicit orders, independent integration, exact gamma limits, exponent margin, and infinite monotone-subsequence rule. |
| C4 | 1 | 2 | HIGH | VERIFIED | Estimator upper `-0.474`, all-estimator Le Cam lower `-0.497`, 21 local-entropy cells, and delta/2 inverse certificate. |
| C5 | 1 | 2 | HIGH | VERIFIED | Proper upper, equal-law all-estimator lower, arbitrary-Q expectation transfer, and exact H² exponents converging to 2. |

## Claim changes and blockers

- C1/C2 add direct full-density integrations in d=2 and d=3 and foreground the universal certificate.
- C3 separates finite construction evidence from the exact infinite-sequence route.
- C4 adds a 21-cell local-entropy calibration that displays the logarithmic correction.
- C5 adds underflow-safe exponent-to-two calibration and an arbitrary-Q transfer certificate.
- BLOCKED claims: none.
- Remaining common risk: evaluator interpretation of the explicit named analytic theorem dependencies in the kernel-checked graph.

## Winning experiment and gate

Stacked lineage:

`historical baseline → exact construction → analytic/application certificates → proper Yatracos experiment → scaled direct evidence → three-route remediation → publication freeze`.

Winning scientific branch: `orx/three-route-per-claim-judge-remediation`, Git
SHA `78b4a451bcf440fdbba2f1326d58b2059c3a337c`.

Publication branch: `orx/three-route-publication-freeze`, created directly
from the passing scientific commit.

Complete pre-freeze gate run:
`e1038127-ca8b-4e10-9d14-de4b89a8b2d7`, Hugging Face `cpu-upgrade`, `2m34s`,
64 logical CPUs visible and one numerical thread. Result:
`publication_gate_passed=true`.

## Commands and compute

Fixed command on every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

New formal launch:

```bash
orx exp run d02b4429-55ca-40c5-9360-1057bf2d5b70 --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
```

The successful HF science job exposed 64 logical CPUs but pinned all numerical
libraries to one thread; its scaled and three-route stages used `15.595s` and
`0.232s`. Complete runtime was `2m34s`. No GPU was used. HF cost was not
exposed, so none is invented. The preceding environment-only launch failed
before science because its default image lacked `uv`.

## Release integrity

- Protected judged revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Current HF and judge head before upload: `8454efce45d0b2946efff5f6e05666ec40abb915`
- Protected historical file count: `22`; old file set is a byte-preserved subset
- Exact text upload allowlist: `101` paths
- Stable candidate manifest: `98` paths
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
- [Visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Blind-review record](../../release/space/evidence/release/red_team.md)
- [Upload allowlist](../../release/space/evidence/release/upload_allowlist.txt)
- [SHA-256 manifest](../../release/space/evidence/release/candidate_manifest.sha256)

Exact publication action: upload only the 101 allowlisted text paths in one
Hugging Face Hub commit to the existing `DineshAI/ihMB4kA2SQ` Space, verify
the returned revision by exact-revision download and hash traversal, then
mirror the published text paths and public report to GitHub `main`. No second
Space will be created.
