- Previous live judged score: `0/10`
- Current user-reported live score: `5/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` — forecast only, not a judge result

# Published scaled direct-evidence release report

The latest machine-readable verdict evaluates Space revision `7c9035a522852c4f85b7e3de054e9d9ae7591c5c` and labels C1–C5 `toy, toy, toy, toy, toy`. The current user-reported total is `5/10`, consistent with one point per toy claim. This release does not claim an increase before the live judge evaluates the new revision.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | 1 | 2 | MEDIUM | VERIFIED | 60 families, 420 exact displayed-bound cells, zero violations, doubled-grid checker. Risk: finite submodels do not enumerate the universal domain. |
| C2 | 1 | 2 | MEDIUM | VERIFIED | Same 420 cells evaluate the exact `1/log log` exponent; zero violations and a false linear control. Risk follows C1’s universal premise boundary. |
| C3 | 1 | 2 | MEDIUM | VERIFIED | Every odd order 11–31 constructs valid mixtures; all 11 sharpness inequalities pass, backed by an asymptotic certificate. Risk: source tail propositions are not proof-assistant checked. |
| C4 | 1 | 2 | MEDIUM | VERIFIED | Eight-horizon estimator slope `-0.431` plus independent 7,000-pair Le Cam lower slope `-0.500`. Risk: the numerical submodel is finite-dimensional. |
| C5 | 1 | 2 | MEDIUM | VERIFIED | Huber samples at `n=200,000`, worst of 17 Q locations, H² slope `1.671`, and equal-law lower H slope `0.929`. Risk: arbitrary Q is supported by the analytic reduction, not exhaustively searched. |

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

Winning scientific branch: `orx/scaled-direct-evidence-judge-remediation`, Git SHA `1b59b9e1b60940c8e4cce58ff7359933032f2571`.

Winning complete gate branch: `orx/scaled-evidence-publication-candidate`, Git SHA `4394cd62bc1c560c3bd7c234e84b644aed96e4f3`.

Formal complete run: `1187af96-3b0b-4cfa-9ee7-e66663935fa0`, local CPU, `1m00s`, one effective numerical thread. Result: `publication_gate_passed=true`.

## Commands and compute

Fixed command on every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

New formal launches:

```bash
orx exp run a7d6796a-606d-428d-928c-81ea90dd48d2 --backend hf --flavor cpu-upgrade
orx exp run a7d6796a-606d-428d-928c-81ea90dd48d2 --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
orx exp run 67156ee5-73b1-48ea-8455-5574d8109e5f --backend local
```

The first HF launch stopped before science because its default image lacked `uv`. The successful HF job exposed 64 logical CPUs but pinned all numerical libraries to one thread; its scaled stage used `7.999s` and approximately `111 MiB` maximum RSS. The complete local gate was launched only after runtime was bounded and finished in `1m00s`. No GPU was used. HF cost was not exposed, so none is invented.

## Release integrity

- Protected judged revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- HF and judge head before upload: `7c9035a522852c4f85b7e3de054e9d9ae7591c5c`
- Published HF revision: `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58`
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
- [7,000-pair cloud](../../release/space/evidence/raw/scaled_direct/pair_cloud_raw.csv)
- [Independent checker](../../release/space/evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../release/space/evidence/raw/scaled_direct/negative_control.json)
- [Visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Blind-review record](../../release/space/evidence/release/red_team.md)
- [Upload allowlist](../../release/space/evidence/release/upload_allowlist.txt)
- [SHA-256 manifest](../../release/space/evidence/release/candidate_manifest.sha256)

Publication action performed: uploaded only the 88 allowlisted text paths in one Hugging Face Hub commit to the existing `DineshAI/ihMB4kA2SQ` Space. An exact-revision download of `ff1f8c3b30b0a580252e7aadaca9e9c5a7d50c58` byte-matched all 88 local upload paths, verified all 85 stable manifest hashes, preserved the 22-file judged subset, and passed canonical traversal. The same published text tree, public report, notebook, and executable code were then mirrored to GitHub `main`. No second Space was created.
