- Previous live judged score: `0/10`
- Conservative projected score range after the proposed change: `4–8/10`
- Best-supported possible new score: `10/10` — forecast only; the live judge has not evaluated revision `7c9035a522852c4f85b7e3de054e9d9ae7591c5c`

# Final judge-remediation release report

The exact candidate was published by one text-only API commit to the existing Hugging Face Space `DineshAI/ihMB4kA2SQ`. Published revision: `7c9035a522852c4f85b7e3de054e9d9ae7591c5c`.

The original numeric judge result remains `0/10`. A later verdict evaluated prior Space revision `7c0bf4dc84363ff022c388d366397e3b295010a6` as `toy, toy, toy, inconclusive, inconclusive`, but that dataset exposes no numeric total. No new score is inferred, and no increase is claimed.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| C1 | not exposed | 2 | MEDIUM | VERIFIED | Exact symbolic exponent, threshold, norm, max/min, and Jensen reductions; source-anchored premise ledger; finite mixtures only corroborate. Risk: imported weighted-polynomial lemmas are not proof-assistant checked. |
| C2 | not exposed | 2 | MEDIUM | VERIFIED | Exact pointwise Hellinger/chi-square identity inherits C1’s universal scope; missing-square and zero-exponent controls fail. Risk follows C1’s imported premises. |
| C3 | not exposed | 2 | MEDIUM | VERIFIED | Exact gamma limits, coefficient margin, and monotone-subsequence rule plus explicit Chebyshev mixtures and independent quadrature. Risk: source uniform-tail premises remain imported. |
| C4 | not exposed | 2 | MEDIUM | VERIFIED | Exact Jia-to-TV implication with `delta/2` inverse repair, implemented proper estimator, 95% intervals, and exhaustive 19-cover pair lower bounds. Risk: finite experiment does not prove the infinite-class theorem. |
| C5 | not exposed | 2 | MEDIUM | VERIFIED | Arbitrary-deviation expectation transfer, continuous-amplitude lower repair, actual Huber samples/estimation/risk, and distinct equal-law pairs at every epsilon. Risk: practical epsilon term is vacuous, so asymptotic support is proof-level rather than empirical. |

## Score and claim changes

- Current numeric total: latest verdict dataset does not expose one; last exposed numeric score is `0/10`.
- Conservative projected total: `4–8/10`.
- Best-supported possible total: `10/10`, forecast only.
- Changed evidence: C1–C3 now lead with exact universal/asymptotic certificates rather than finite rows; C4–C5 now include a proper Yatracos estimator, actual Huber contamination, risk intervals, and exhaustive finite-cover lower mechanisms.
- BLOCKED claims: none.
- Remaining risk: evaluator acceptance of source-anchored symbolic proof certificates without proof-assistant formalization.

## Experiment tree and winning evidence

The stacked tree was:

`historical baseline → independent quadrature → analytic/application certificates → universal proof remediation → proper Yatracos experiment → immutable release gates → blind-review fixes → text-only upload staging`.

Winning scientific/release-gate branch: `orx/publishable-judge-remediation-candidate`.

Winning gate Git SHA: `7dcfa9a`.

Formal winning run: `7faa2f57-f13c-43bf-9ba2-2d3699476109`, local CPU, `1m35s`. The committed estimator was explicitly capped to one thread; 8 logical CPUs were visible. Its estimator stage used `8.939s` and reported maximum RSS `167362560` bytes. No GPU was used.

Immutable promoted scientific output came from SHA `959e052077f7edb0609e1d81b3e4b5f59c400a55`, run `05a4e1bb-3d3b-4a80-a27d-6f886c81968e`. The final run independently regenerated identical deterministic scientific fields.

## Commands and compute

The fixed experiment command was identical on every node:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

New formal launches in this remediation:

```bash
orx exp run 4d627e7e-6717-4009-a634-10a301e3e9b3 --backend local
orx exp run d327fa42-c1cc-4c64-a29e-3fb0cb04ad8e --backend hf --flavor cpu-upgrade
orx exp run d327fa42-c1cc-4c64-a29e-3fb0cb04ad8e --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
orx exp run 617995b4-77f9-458d-9dcd-18ac6a92edbf --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 1h
orx exp run e3eb80a1-e8b1-4720-acd2-94b20ae15cd4 --backend local
orx exp run c8668574-5c1c-4343-bf1d-8bcecad03d7d --backend local
orx exp run 66e8a101-4e8e-48d5-a021-a5894670a23f --backend local
```

HF `cpu-upgrade` exposed 64 logical CPUs. The refined remote estimator run completed in `58s` total with a `2.9587s` estimator kernel. The default-image precursor failed before science because `uv` was absent; it is retained as environmental history. HF billing cost was not exposed, so none is inferred. Local runs have no remote billed cost.

## Release integrity

- Prior HF Head: `7c0bf4dc84363ff022c388d366397e3b295010a6`.
- Published HF Head: `7c9035a522852c4f85b7e3de054e9d9ae7591c5c`.
- Protected judged file count: `22`; the old file set is a byte-preserved subset.
- Exact text upload allowlist: `75` paths.
- Stable candidate manifest: `72` paths; only the manifest itself, release-check JSON, and secret-scan JSON are excluded to avoid self-reference.
- Secret scan: PASS.
- Evaluator-blind reviews: pass 1 found two displayed-data mismatches; pass 2 after fixes located all required evidence and passed.
- Post-publication exact-revision download: `285` files; every manifest hash matched; canonical traversal and current-verifier prominence passed.

## Evidence

- [Canonical published Space tree](../../release/space/README.md)
- [Visibility matrix](../../release/space/pages/current-visibility/page.md)
- [Exact universal output](../../release/space/evidence/raw/universal_reductions/result.json)
- [Proper Yatracos result](../../release/space/evidence/raw/yatracos_experiment/result.json)
- [Raw estimator replicates](../../release/space/evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Independent checker](../../release/space/evidence/raw/yatracos_experiment/independent_checker.json)
- [Red-team record](../../release/space/evidence/release/red_team.md)
- [Exact upload allowlist](../../release/space/evidence/release/upload_allowlist.txt)
- [SHA-256 manifest](../../release/space/evidence/release/candidate_manifest.sha256)

Publication action performed: one direct Hugging Face Hub commit containing exactly the 75 allowlisted text paths, to the existing `DineshAI/ihMB4kA2SQ` Space only, followed by an exact-revision download and hash/traversal verification. The campaign is awaiting the live judge.
