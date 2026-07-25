- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `6–10/10`
- Best-supported possible new score: `10/10` — forecast only; the live judge has not evaluated the new revision

# Final release report

The claim-by-claim evaluator artifact was published to the existing Hugging Face Space `DineshAI/ihMB4kA2SQ` at revision `7c0bf4dc84363ff022c388d366397e3b295010a6`. The Judge Head remains the previously evaluated `1c98799a89d8c1d3c45136c8b912e74371e975b3`, so the current score remains `0/10` until a new verdict is recorded.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | 0 | 2 | MEDIUM | VERIFIED | Exact quantifiers, reconstructed universal implication, six direct mixtures, independent quadrature, and fail-closed controls. Risk: weighted-polynomial lemmas are reconstructed rather than proof-assistant formalized. |
| C2 | 0 | 2 | MEDIUM | VERIFIED | Exact `1/log log` exponent follows from C1 and an independently checked pointwise Hellinger/chi-square inequality; six direct ratios agree. Risk follows C1's imported lemmas. |
| C3 | 0 | 2 | MEDIUM | VERIFIED | Valid Chebyshev mixtures satisfy all six sharpness inequalities; exact norm asymptotics, coefficient budget, controls, and decreasing-subsequence repair are checked. Risk: analytic reconstruction is not machine-formal logic. |
| C4 | 0 | 2 | MEDIUM | VERIFIED | Jia's primary Fano result is pinned and assumption-mapped; the minimax proof is reconstructed with a necessary `delta/2` inversion repair. Risk: evaluator acceptance of the quantified-slack repair. |
| C5 | 0 | 2 | MEDIUM | VERIFIED | Proper Yatracos upper chain and Chen lower chain are reconstructed; continuous amplitude covers every small contamination level while retaining coefficient `0.3308206>0.33`. Risk: external entropy/two-point dependencies remain imported. |

## Score and claim changes

- Current total score: `0/10`.
- Conservative projected total score range: `6–10/10`.
- Best-supported possible total: `10/10`, forecast only.
- Claims changed in the reproduction artifact: C1–C5 moved from the judge's INCONCLUSIVE evidence state to current VERIFIED/MEDIUM scientific verdicts.
- BLOCKED claims: none.
- No score increase is claimed; only the live evaluator can change the result.

## Experiment tree and winner

The tree used a stacked sequence: frozen historical baseline → independent C1–C3 quadrature siblings → C1–C3 analytic certificate → C4–C5 application certificate → evaluator-visible release candidate.

Winning experiment branch: `orx/evaluator-visible-release-candidate`.

Winning Git SHA: `108047a42ce57397fa7c33799e7d6ac1d368a6ae`.

Formal winning run: `f09c11ab-b056-4346-8d76-392405738c3d`, `1m05s`, local CPU, 8 logical CPUs visible and one effective core used. Pre-run estimate was one effective core and under three minutes. No GPU was used.

## Formal command ledger

The fixed command inherited unchanged by every experiment was:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

The formal launches were:

```bash
orx exp run 4476ad2b-764d-45df-9dd6-470e97903568 --backend local
orx exp run ea932faf-a8e9-44fd-a357-ea46116c04cb --backend hf --flavor cpu-upgrade
orx exp run 6bad9825-832b-4627-b072-c11b3a060844 --backend hf --flavor cpu-upgrade
orx exp run 8bce8c53-583c-413f-a804-20327ade0776 --backend hf --flavor cpu-upgrade
orx exp run 04fa6b95-b47f-4c79-926c-ab21a3e6bb96 --backend local
orx exp run f2640c4d-aa8b-4f5f-8519-35ca5230fe6f --backend local
orx exp run 17331298-296a-45ce-a4a8-a42c8e1e4537 --backend local
orx exp run 1b6d9ed8-ea6a-4bcb-b386-61a17992626d --backend local
```

Hugging Face `cpu-upgrade` exposed 64 logical CPUs; the verifier remained serial and used one effective core. Local runs exposed 8 logical CPUs and likewise remained serial. Hugging Face billing cost was not present in the logs, so no cost is inferred; local runs had no billed remote cost.

## Release integrity

- Baseline HF Head and Judge Head before publication: `1c98799a89d8c1d3c45136c8b912e74371e975b3`.
- Published HF Head: `7c0bf4dc84363ff022c388d366397e3b295010a6`.
- Exact judged file count: 22; old set is a byte-preserved subset of the new 78-file tree.
- Text-only upload: 59 paths in the [exact allowlist](../../release/space/evidence/release/upload_allowlist.txt).
- Stable SHA-256 coverage: 56 paths in the [candidate manifest](../../release/space/evidence/release/candidate_manifest.sha256); the manifest and two generated audit outputs are the deliberate self-reference exclusions.
- Post-publication download: all 59 uploaded hashes matched, canonical traversal passed, secret scan passed, and two evaluator-blind red-team passes remained reachable.

## Evidence

- [Canonical Space entrypoint](../../release/space/README.md)
- [Evaluator visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Release checker output](../../release/space/evidence/release/release_check.json)
- [Red-team record](../../release/space/evidence/release/red_team.md)
- [Raw C1–C3 CSV](../../release/space/evidence/raw/claim_1_3/raw_results.csv)
- [C1–C3 analytic certificate](../../release/space/evidence/raw/analytic_certificate/result.json)
- [C4–C5 application certificate](../../release/space/evidence/raw/application_certificate/result.json)

Publication action performed: one text-only Hugging Face API commit to the existing `DineshAI/ihMB4kA2SQ` Space, followed by an exact-revision download and hash/traversal verification. The campaign is awaiting the live judge.
