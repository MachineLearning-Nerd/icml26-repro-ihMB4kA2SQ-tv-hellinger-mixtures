- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` — forecast only, not a judge result
- Current live judged score: `5/10`

# Scaled direct-evidence release report

The latest machine-readable verdict evaluates Space revision
`89d6ea2210377512cbadb69ed86d2fccfb9e0f40` and labels C1–C5
`toy, toy, toy, toy, toy`. The current total is `5/10`. Corrected revision
`8454efce45d0b2946efff5f6e05666ec40abb915` is published and awaiting judge;
this report does not claim an increase before that live evaluation.

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

`historical baseline → exact construction → analytic/application certificates → proper Yatracos experiment → scaled direct evidence → evaluator-calibrated release → exact-display remediation → publication freeze`.

Winning scientific remediation branch:
`orx/exact-display-and-evaluator-path-remediation`, Git SHA
`f8c9cd3a37b8d54f82eecc197734708cd9e97048`.

Publication branch: `orx/exact-display-publication-freeze`, Git SHA
`bddd1077e4f6fc1424ff54128318633a2181b902`.

The remediation gate run `374f88a3-d40f-4a8c-840f-4f9d3a0d3ed4`
passed in `2m00s`. The exact publication-freeze run
`4d7b98a6-81b0-48ae-992b-57eff501b3ed` passed in `3m06s`. Both used the
local CPU backend, eight logical CPUs visible, and one effective numerical
thread. Result: `publication_gate_passed=true`.

## Commands and compute

Fixed command on every experiment node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Current formal launches:

```bash
orx exp run 1f505a46-ee91-4006-8b48-ec28e84b9919 --backend local
orx exp run 2882629b-41ae-4ffa-af97-7f63e9ae4325 --backend local
```

The publication-freeze scaled stage used `31.403s` and `115,638,272` bytes
maximum RSS. No GPU was used. Prior uncertain work used Hugging Face
`cpu-upgrade`; HF cost was not exposed, so none is invented.

## Release integrity

- Protected judged revision: `1c98799a89d8c1d3c45136c8b912e74371e975b3`
- HF and judge head before upload: `89d6ea2210377512cbadb69ed86d2fccfb9e0f40`
- Exact published HF revision: `8454efce45d0b2946efff5f6e05666ec40abb915`
- Protected historical file count: `22`; old file set is a byte-preserved subset
- Exact text upload allowlist: `88` paths
- Stable candidate manifest: `85` paths
- Visibility rows complete: `5`
- Secret scan: PASS
- Evaluator-blind review: six passes; final no-delete overlay retained all `107` paths
- Post-publication verification: all `88` uploaded files byte-identical, `85` hashes pass, `94` canonical links resolve

## Evidence paths

- [Exact published tree](../../release/space/README.md)
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

Publication action completed: the 88 allowlisted text paths were committed to
the existing `DineshAI/ihMB4kA2SQ` Space without deletion or a second Space.
Exact revision `8454efce45d0b2946efff5f6e05666ec40abb915` was downloaded and
verified, then mirrored here.
