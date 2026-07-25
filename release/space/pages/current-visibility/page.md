# Evaluator visibility matrix

Traversal starts at `README.md`, then follows only its current links. “Reviewer verdict” records the evaluator-blind pre-publication review, not a live judge score.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | [C1](#/current-claim-c1) | Yes | Yes | [CSV](../../evidence/raw/claim_1_3/raw_results.csv) | [analytic](../../evidence/src/repro/src/verify_analytic_certificate.py) + [independent](../../evidence/raw/claim_1_3/independent_checker.json) | `alpha=0`, reverse Jensen | Yes: square-root chi-square bound, support, delta, C0 quantifiers | Located; VERIFIED/MEDIUM |
| C2 | [C2](#/current-claim-c2) | Yes | Yes | [JSON](../../evidence/raw/claim_1_3/result.json) | [analytic](../../evidence/src/repro/src/verify_analytic_certificate.py) | missing square, `alpha=0` | Yes: Hellinger bound and exact logarithmic exponent | Located; VERIFIED/MEDIUM |
| C3 | [C3](#/current-claim-c3) | Yes | Yes | [CSV](../../evidence/raw/claim_1_3/raw_results.csv) | [construction](../../evidence/src/repro/src/verify_claims_1_3.py) + [independent](../../evidence/raw/claim_1_3/independent_checker.json) | wrong nodes, `0.50`, `0.34`, direct relabel | Yes: valid mixtures, all-n existential sequence, `0.33` | Located; VERIFIED/MEDIUM |
| C4 | [C4](#/current-claim-c4) | Yes | Yes | [JSON](../../evidence/raw/application_certificate/result.json) | [application](../../evidence/src/repro/src/verify_application_certificate.py) | same-delta inverse | Yes: compact-class minimax upper/lower quantifiers | Located; VERIFIED/MEDIUM |
| C5 | [C5](#/current-claim-c5) | Yes | Yes | [JSON](../../evidence/raw/application_certificate/result.json) | [application](../../evidence/src/repro/src/verify_application_certificate.py) | discrete-only, `0.34`, omitted union factor | Yes: Yatracos upper and all-estimator Huber lower | Located; VERIFIED/MEDIUM |

Every claim page also exposes assumptions, exact fixed command, locked environment, raw inline numbers, Git SHA, seed, CPU/runtime, limitations, and a verifier that fails nonzero.
