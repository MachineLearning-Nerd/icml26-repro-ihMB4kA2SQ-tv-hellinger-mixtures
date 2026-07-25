# Evaluator-blind red-team record

## Pass 1

Starting point: `README.md`. Rubric supplied: evaluator-visible evidence gate and five judge criticisms. No repository knowledge was used.

Files opened:

- `README.md`
- `pages/current-overview/page.md`
- five `pages/current-claim-c*/page.md` files
- `pages/current-methods/page.md`
- `pages/current-visibility/page.md`
- linked raw JSON/CSV and verifier source
- `logbook.json`

Findings:

- All five exact claim statements and proof routes were located.
- Historical pages were still easy to mistake for current pages in the inherited navigation.
- Some claim evidence was summarized without a direct raw/code/limitations link on the same page.
- The protected old/new subset assertion was not visible from the canonical entrypoint.

Fixes:

- Current pages were placed first and the old tree was labeled exactly “Historical rejected baseline.”
- Every claim page received inline raw values plus direct source, raw, checker, control, command, environment, SHA, runtime, and limitations links.
- The visibility matrix and protected manifest/subset section were linked directly from `README.md`.

## Pass 2

Starting point: `README.md` only. The reviewer followed only reachable links.

Files opened:

- `README.md`
- `pages/current-overview/page.md`
- `pages/current-claim-c1/page.md`
- `pages/current-claim-c2/page.md`
- `pages/current-claim-c3/page.md`
- `pages/current-claim-c4/page.md`
- `pages/current-claim-c5/page.md`
- `pages/current-methods/page.md`
- `pages/current-visibility/page.md`
- `pages/current-release-audit/page.md`
- `evidence/raw/claim_1_3/raw_results.csv`
- `evidence/raw/claim_1_3/independent_checker.json`
- `evidence/raw/analytic_certificate/result.json`
- `evidence/raw/application_certificate/result.json`
- `evidence/raw/primary_dependencies/result.json`
- four linked verifier files
- both linked limitations files

Conclusions:

- The current verifier was unambiguous.
- Exact quantifiers, assumptions, executable code, fixed command, pinned environment, inline data, raw downloads, independent checkers, negative controls, limitations, Git SHA, seed, CPU, and runtime were located for every claim.
- No conclusion required a hidden repository path or unpublished run dashboard.
- Each claim was scored VERIFIED/MEDIUM in the blind review. This is a pre-publication forecast, not a live judge result.
