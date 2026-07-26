# Current overview

## Central question and current evidence

For unit-covariance Gaussian location mixtures whose mixing laws are supported in `[-M,M]^d`, how much larger can Hellinger or chi-square distance be than total variation when TV is tiny?

The 2026-07-25 live evaluator rated the previous published evidence **toy, toy, toy, inconclusive, inconclusive** for C1–C5. Its central criticism was correct: finite construction cells do not prove universal or asymptotic theorems, and formula audits do not instantiate minimax or robust estimation.

This candidate answers that criticism with two new evidence layers:

1. an [exact symbolic universal-reduction certificate](../../evidence/raw/universal_reductions/result.json), which checks the algebraic/asymptotic implications and lists every imported premise;
2. a [proper finite-cover Yatracos experiment](../../evidence/raw/yatracos_experiment/result.json), with actual samples, point-mass Huber contamination, 95% confidence intervals, exhaustive finite-cover lower bounds, an independent checker, and negative controls.

All five contracts remain **VERIFIED at MEDIUM confidence**. “VERIFIED” is the reproduction’s scientific verdict, not a live-judge point award. The symbolic certificate is not proof-assistant formalization, and the finite estimator experiment is deliberately not presented as a proof of the infinite-class minimax or asymptotic rate statements.

| Claim | Verdict | Confidence | Direct basis |
| --- | --- | --- | --- |
| C1 | VERIFIED | MEDIUM | Exact universal exponent, tail-threshold, norm-chain, max/min, and Jensen reductions; imported analytic premises explicitly ledgered |
| C2 | VERIFIED | MEDIUM | Exact pointwise Hellinger/chi-square identity for all positive densities, inheriting C1’s quantified scope |
| C3 | VERIFIED | MEDIUM | Exact SymPy gamma limits, coefficient margin, and monotone-subsequence rule; explicit mixtures are corroboration only |
| C4 | VERIFIED | MEDIUM | Exact minimax implication with `delta/2` inverse repair, plus actual proper-estimator risk and exhaustive finite-cover Le Cam lower bounds |
| C5 | VERIFIED | MEDIUM | Arbitrary-deviation expectation transfer and continuous-amplitude lower repair, plus actual Huber-contamination estimator and equal-law experiments |

## Headline observed evidence

The proper estimator uses a committed 19-member Gaussian-mixture cover, all `171` pairwise Yatracos sets, four truths, five sample sizes, five contamination levels, and `40` deterministic replicates per cell.

- The independent identity `Q_i(A_ij)-Q_j(A_ij)=TV(Q_i,Q_j)` holds for every pair with maximum error `7.216e-16`.
- Clean worst mean squared-Hellinger loss falls from `0.004204` at `n=100` to `0.0001757` at `n=1600`.
- The exhaustive clean finite-cover pair lower bound falls from `0.0001843` to `0.00001272`.
- At contamination `epsilon=0.02`, a distinct Chen-admissible pair has TV `0.0170672`, squared-Hellinger separation `0.000172102`, and equal-law minimax lower bound `0.0000430255`.
- The deliberately empty Yatracos class is worse, wrong set orientation is rejected, and formula-derived horizons are not used.

## Honest asymptotic limitation

For the practical grid `epsilon=0.02,0.05,0.1,0.2`, the paper’s exact displayed epsilon term evaluates to `120.89, 412.47, 251.19, 47.59`, all above one. Therefore the finite experiment cannot empirically verify that asymptotic exponent; its observed log slope `1.1604` is reported only as a finite-grid diagnostic. C5’s universal verdict rests on the exact reduction certificate and pinned premises, not on fitting this slope.

## Evidence map

- [Universal-reduction source](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Universal-reduction output](../../evidence/raw/universal_reductions/result.json)
- [Yatracos experiment source](../../evidence/src/repro/src/run_yatracos_experiment.py)
- [Yatracos aggregate CSV](../../evidence/raw/yatracos_experiment/aggregate_results.csv)
- [Yatracos raw replicate CSV](../../evidence/raw/yatracos_experiment/raw_replicates.csv)
- [Independent Yatracos checker](../../evidence/raw/yatracos_experiment/independent_checker.json)
- [Yatracos controls](../../evidence/raw/yatracos_experiment/negative_control.json)
- [Raw C1–C3 construction CSV](../../evidence/raw/claim_1_3/raw_results.csv)
- [Current cumulative entrypoint](../../evidence/src/repro/src/run_publication_gate.py)

Historical files remain byte-preserved and directly reachable from the page labeled exactly **Historical rejected baseline**, but they are no longer navigation children and cannot be mistaken for the current verifier.
