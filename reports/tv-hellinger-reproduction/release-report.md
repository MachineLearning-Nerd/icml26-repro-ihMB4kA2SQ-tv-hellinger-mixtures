- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` — forecast only, not a judge result
- Current live judged score: `5/10`

# Scaled direct-evidence release report

The latest machine-readable verdict evaluates Space revision `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58` and labels C1–C5 `toy, toy, toy, toy, toy`. The current total is `5/10`, consistent with one point per toy claim. This release does not claim an increase before the live judge evaluates the new revision.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | 1 | 2 | MEDIUM | VERIFIED | 60 families, 420 exact displayed-bound cells, zero violations, doubled-grid checker. Risk: finite submodels do not enumerate the universal domain. |
| C2 | 1 | 2 | MEDIUM | VERIFIED | Same 420 cells evaluate the exact `1/log log` exponent; zero violations and a false linear control. Risk follows C1’s universal premise boundary. |
| C3 | 1 | 2 | MEDIUM | VERIFIED | Every odd order 11–31 constructs valid mixtures at 110 digits; residual `4.243e-115`, all sharpness cells pass, and an asymptotic certificate supplies the sequence route. Risk: source tail propositions are not proof-assistant checked. |
| C4 | 1 | 2 | MEDIUM | VERIFIED | Eight-horizon estimator slope `-0.474` plus independent 5,258-pair Le Cam lower slope `-0.497`. Risk: the numerical submodel is finite-dimensional. |
| C5 | 1 | 2 | MEDIUM | VERIFIED | Huber samples at `n=200,000`, worst of 17 Q locations, H² slope `1.688`, and exact-Chen equal-law lower H slope `0.960`. Risk: arbitrary Q is supported by the analytic reduction, not exhaustively searched. |

## Claim changes and blockers

- C1 now tests the exact logarithmic bound on 420 cells rather than generic inequalities.
- C2 now tests the exact corollary exponent rather than `H²<=TV`.
- C3 now constructs and integrates the actual mixtures for every odd order 11–31.
- C4 now has independently calibrated upper-estimator and all-estimator lower routes.
- C5 now instantiates Huber contamination, searches adversarial Q locations, and constructs exact equal-law lower pairs.
- BLOCKED claims: none.
- Remaining common risk: evaluator acceptance of combined scoped numerical evidence and independently reconstructed source-anchored certificates without proof-assistant formalization.

## Winning experiment and gate

Stacked lineage:

`historical baseline → exact construction → analytic/application certificates → proper Yatracos experiment → scaled direct evidence → evaluator-visible candidate → publication candidate`.

Winning scientific branch: `orx/evaluator-calibrated-exact-replication-v2`, Git SHA `9ef83c11c7c527c32bebfbae69585518eac8551b`.

Publication branch: `orx/evaluator-calibrated-publication-release`, created directly from the passing scientific commit.

Complete pre-freeze gate run: `1fe4016d-5c41-4c6f-9f89-99a36bc3e2c8`, local CPU, `2m25s`, one effective numerical thread. Result: `publication_gate_passed=true`. The same science stage previously passed on Hugging Face `cpu-upgrade` with 64 logical CPUs visible and numerical libraries pinned to one thread.

## Commands and compute

Fixed command on every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

New formal launches:

```bash
orx exp run 57908ed9-d3e1-4427-aacd-4a89361a81e1 --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
orx exp run 57908ed9-d3e1-4427-aacd-4a89361a81e1 --backend local
orx exp run f50a2a14-b286-4d43-99ee-e9c0a57c3e3a --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
```

The successful HF science job exposed 64 logical CPUs but pinned all numerical libraries to one thread; its scaled stage used `13.744s`. The complete local gate was launched only after runtime was bounded and finished in `2m25s`. No GPU was used. HF cost was not exposed, so none is invented.

## Release integrity

- Protected judged revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- Current HF and judge head before upload: `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58`
- Protected historical file count: `22`; old file set is a byte-preserved subset
- Exact text upload allowlist: `88` paths
- Stable candidate manifest: `85` paths
- Visibility rows complete: `5`
- Secret scan: PASS
- Evaluator-blind review: PASS after a fresh archive traversal

## Evidence paths

- [Canonical candidate](../../release/space/README.md)
- [Scaled result](../../release/space/evidence/raw/scaled_direct/result.json)
- [C1/C2 raw cells](../../release/space/evidence/raw/scaled_direct/claim_1_2_raw.csv)
- [C3 raw construction](../../release/space/evidence/raw/claim_1_3/raw_results.csv)
- [C4 estimator rows](../../release/space/evidence/raw/scaled_direct/claim_4_upper_raw.csv)
- [C5 contamination rows](../../release/space/evidence/raw/scaled_direct/claim_5_upper_raw.csv)
- [5,258-pair cloud](../../release/space/evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../release/space/evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../release/space/evidence/raw/scaled_direct/negative_control.json)
- [Visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Blind-review record](../../release/space/evidence/release/red_team.md)
- [Upload allowlist](../../release/space/evidence/release/upload_allowlist.txt)
- [SHA-256 manifest](../../release/space/evidence/release/candidate_manifest.sha256)

Exact publication action: upload only the 88 allowlisted text paths in one Hugging Face Hub commit to the existing `DineshAI/ihMB4kA2SQ` Space, verify the returned revision by exact-revision download and hash traversal, then mirror the published text paths and public report to GitHub `main`. No second Space will be created.
