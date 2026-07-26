# Evaluator-blind red-team record

Rubric: five live-judge criticisms plus the evaluator-visible evidence gate. Reviewers were not told where evidence was stored and used no unpublished repository, dashboard, or OpenResearch-log knowledge.

## Pass 1 — exact Git candidate, fixes required

Candidate Git SHA: `fe2d52b`. Fresh empty directory: an archive of `release/space` at that SHA. Starting point: `README.md` only.

Files opened by following reachable links:

- `README.md`
- `pages/current-overview/page.md`
- `pages/current-claim-c1/page.md` through `pages/current-claim-c5/page.md`
- `pages/current-methods/page.md`
- `pages/current-visibility/page.md`
- `pages/current-release-audit/page.md`
- `pages/historical-rejected-baseline/page.md`
- `evidence/raw/universal_reductions/result.json`
- `evidence/raw/yatracos_experiment/result.json`
- `evidence/raw/yatracos_experiment/aggregate_results.csv`
- `evidence/raw/yatracos_experiment/raw_replicates.csv`
- `evidence/raw/yatracos_experiment/independent_checker.json`
- `evidence/raw/yatracos_experiment/negative_control.json`
- `logbook.json`

Located:

- all five exact contracts, assumptions, verdicts, and confidence labels;
- exact universal-reduction source/output and explicit premise ledgers;
- proper-estimator source, actual Huber model, horizons, seeds, confidence intervals, finite-cover lower bounds, checkers, controls, limitations, and raw rows;
- fixed command, lockfile, CPU/runtime metadata, fail-closed entrypoint, history subset statement, and no-children historical navigation.

Could not accept:

- C4/C5 pages and the canonical overview still displayed the earlier HF checker error `7.216e-16`, while the promoted immutable raw evidence displays `4.218847493575595e-15`;
- C4/C5 pages still cited preliminary estimator SHA `094d92e` and run `7bc34e8e…`, while the current raw result cites immutable SHA `959e052` and run `05a4e1bb…`.

Fixes:

- changed every current displayed checker error to `4.219e-15`;
- changed current estimator provenance to SHA `959e052077f7edb0609e1d81b3e4b5f59c400a55`, run `05a4e1bb-3d3b-4a80-a27d-6f886c81968e`, and cumulative runtime `1m30s`;
- added a fail-closed release assertion that the displayed checker error equals the formatted raw value.

Pass-1 conclusion: **FAIL until the displayed-data/provenance mismatches are fixed.**

## Pass 2 — fixed candidate, visibility complete

Candidate Git SHA: `f3baf49`. Fresh empty directory: a new archive of `release/space` at that SHA. Starting point: `README.md` only.

Files opened:

- `README.md`
- all current overview, C1–C5, methods, visibility, release-audit, and historical-label pages;
- current cumulative entrypoint, exact universal verifier, and proper Yatracos estimator source;
- universal and Yatracos result JSON;
- aggregate and raw-replicate CSV;
- independent checker, negative controls, and limitations;
- exact upload allowlist and `logbook.json`.

Conclusions:

- all five exact contracts, assumptions, verdicts, and MEDIUM confidence labels were found;
- every page exposes the fixed command, raw links, source, checker, control, limitation, provenance, CPU/runtime, and fail-closed behavior;
- displayed checker error `4.219e-15` and evidence SHA `959e052…` match raw data;
- the proper estimator, actual Huber contamination, 95% intervals, exhaustive finite-cover lower bounds, and raw replicates are directly reachable;
- every practical epsilon row is visibly and machine-readably `nonvacuous_paper_term=false`, so no finite slope is misrepresented as asymptotic verification;
- universal/asymptotic conclusions point to exact symbolic reductions and explicit imported-premise ledgers rather than finite cells;
- the historical node is last, labeled exactly `Historical rejected baseline`, has no children, and its preserved files remain reachable.

Pass-2 conclusion: **PASS.** No conclusion required a hidden repository path, unpublished branch, dashboard artifact, or agent hint.
