# Evaluator-blind red-team record

Rubric: the five latest `toy` criticisms plus the evaluator-visible evidence gate. The review used only a fresh candidate archive, began at `README.md`, and did not use OpenResearch logs, dashboard files, unpublished artifacts, or hints about evidence locations.

## Pass 1 — pre-freeze candidate, fixes required

Starting point: the candidate `README.md` before Git freeze.

Files opened by following visible links:

- `README.md`
- `pages/current-overview/page.md`
- `pages/current-claim-c1/page.md` through `pages/current-claim-c5/page.md`
- `pages/current-methods/page.md`
- `pages/current-visibility/page.md`
- `evidence/raw/universal_reductions/result.json`
- `evidence/raw/yatracos_experiment/result.json`
- `evidence/src/repro/src/run_publication_gate.py`

Could locate the exact symbolic certificates and the earlier finite-cover Yatracos evidence, but could not locate the new 420-cell sweep, 11-order construction, 7,000-pair lower search, or scaled contamination CSV from the landing page. The new scientific output existed internally but was not yet evaluator-visible.

Required fixes:

- place `run_scaled_direct_evidence.py` and its result first in the landing page;
- mirror all four scaled CSV files, claim contract, source audit, independent checker, negative controls, method, and limitations;
- put exact raw values inline on every claim page;
- replace the report headline and claim figures with the scaled evidence;
- require the mirrored scaled result to match freshly regenerated deterministic fields.

Pass-1 conclusion: **FAIL — scientifically useful output was hidden from the evaluator.**

## Pass 2 — frozen Git candidate

Candidate Git SHA: `94ebab9`. Fresh directory: `/tmp/tvhellinger-blind.RidcWg`, created from `git archive 94ebab9 release/space`. Starting point: `README.md` only.

Files opened:

- `README.md`
- all current overview, C1–C5, methods, visibility, release-audit, and historical-label pages;
- `evidence/src/repro/src/run_scaled_direct_evidence.py`;
- `evidence/src/repro/src/run_publication_gate.py`;
- `evidence/raw/scaled_direct/result.json`;
- `evidence/raw/scaled_direct/claim_1_2_raw.csv`;
- `evidence/raw/claim_1_3/raw_results.csv`;
- `evidence/raw/scaled_direct/claim_4_upper_raw.csv`;
- `evidence/raw/scaled_direct/claim_5_upper_raw.csv`;
- `evidence/raw/scaled_direct/pair_cloud_raw.csv`;
- scaled claim contract, source audit, independent checker, negative controls, method, and limitations;
- exact upload allowlist, candidate manifest, release check, secret scan, and `logbook.json`.

Checks and conclusions:

- C1/C2 raw row count is `420` plus one header; the result reports `60` families, TV `1.15577e-7`–`0.0475248`, and zero violations.
- C3 raw row count is `11` plus one header; orders are exactly every odd integer 11–31, and all sharpness gates pass.
- The pair cloud contains `7,000` rows plus one header. C4 upper/lower slopes are `-0.431397` and `-0.500026`.
- C5 upper H² and lower H slopes are `1.671174` and `0.929163`; the lower search has no saturated steps.
- All five negative controls are true because the intended false alternatives were rejected.
- Every claim page exposes its exact contract, assumptions, inline data, raw link, source, checker, control, limitation, fixed command, seed, and compute information.
- The cumulative entrypoint invokes every stage with `check=True`; the scaled verifier raises on a failed scientific gate.
- The historical node remains last, labeled exactly `Historical rejected baseline`, and its protected file set remains a subset.

Pass-2 conclusion: **PASS.** No conclusion required an inaccessible path or repository knowledge.

## Pass 3 — final provenance-only candidate

Candidate Git SHA: `c02901f`. Fresh directory: `/tmp/tvhellinger-final-blind.oR4Mpd`, created from `git archive c02901f release/space`.

The reviewer reopened `README.md`, current overview, methods, release audit, scaled result, upload allowlist, and manifest. The only evaluator-page changes since pass 2 were the exact successful gate SHA/run/runtime and the 88-path publication action. The reviewer located those fields, reconfirmed the headline raw values, and verified all 85 stable SHA-256 entries from inside the fresh directory.

Pass-3 conclusion: **PASS.** Provenance and manifest are consistent with the final candidate.
