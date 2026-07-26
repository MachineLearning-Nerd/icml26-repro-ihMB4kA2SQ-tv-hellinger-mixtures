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

## Pass 2

Pending a fresh archive of the fixed candidate. Publication remains blocked until this pass locates all evidence and reports no mismatch.
