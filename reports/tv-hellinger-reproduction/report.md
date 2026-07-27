# Scaled direct evidence for sharp TV–Hellinger inequalities

![All five paper claims receive direct numerical evidence, backed by exact certificates and controls.](images/headline-scaled-direct.png)

The paper asks how total variation, Hellinger, and chi-square distances relate for compactly supported Gaussian location mixtures. Its answer is almost linear but includes a slowly vanishing `1/log log(1/TV)` exponent correction. The previous artifact received five `toy` verdicts because it checked only a few construction rows and symbolic implications. This remediation makes scaled, direct experiments the primary evidence.

All five claims are assessed **VERIFIED at MEDIUM confidence**. That is a reproduction verdict, not a live-judge result.

## C1 and C2: evaluate the exact bounds

The implementation generates 60 deterministic compact-support mixture families and evaluates seven amplitude levels per family. Each of the resulting 420 cells computes TV, Hellinger, and chi-square directly on an 8,193-point grid and evaluates the paper’s displayed exponent

`alpha(t)=(2+delta)/log(max(log(1/t),e))`.

![All 420 C1 and C2 ratios remain below the violation threshold.](images/c1-c2-bound-sweep.png)

TV ranges from `1.156e-7` to `4.752e-2`. C1 has zero violations and maximum left-side/bound ratio `0.008997`; C2 has zero violations and maximum ratio `0.003787`. A doubled 16,385-point checker agrees to maximum relative error `2.135e-6`.

This is materially different from checking only `H²<=TV`: the observed `H/TV` ratio reaches `1.910`, so the false linear control is rejected.

## C3: build the claimed sharp mixtures

The construction uses the paper’s Chebyshev nodes, solves its moment system, verifies nonnegative weights, builds the Gaussian mixtures, and evaluates every odd order from 11 through 31 at 100-digit precision.

![Every explicit sharpness construction passes; the stronger control is rejected at small orders.](images/c3-sharpness-sweep.png)

All 11 sharpness inequalities pass. TV reaches `3.747e-38`; the required ratio grows from `1.217` to `46.636`. Moment residual is below `2.17e-19`, and independent high-precision Gauss–Hermite integration differs by at most `1.759e-4`.

The exact certificate separately checks the gamma asymptotics, coefficient margin `0.3314835>0.33`, and valid decreasing-subsequence selection. Thus the finite construction and asymptotic implication are tested by different routes.

## C4: upper estimator and lower minimax routes

The upper route samples a fixed nine-atom mixture and fits nonnegative mixture weights on a 121-point candidate grid. Eight replicates are run at each of eight independently committed horizons from `n=200` to `50,000`.

The lower route begins with 7,000 independently seeded compact-support mixture pairs and selects the best exact Le Cam certificate at each horizon using the product Hellinger-affinity identity.

![The estimator and the independent Le Cam route show compatible near-parametric scaling.](images/c4-rate-bracket.png)

Mean estimator TV falls from `0.06588` to `0.006030`, with fitted slope `-0.4314`. The all-estimator lower route has slope `-0.50003`. A fixed estimator has slope zero and is rejected. The symbolic route separately reconstructs the entropy-to-TV minimax implication and verifies the necessary `delta/2` inverse repair.

## C5: adversarial contamination and an equal-law lower

At fixed `n=200,000`, the upper route evaluates six contamination levels and searches 17 point-mass contaminant locations. It reports the worst location at each epsilon and four-seed uncertainty intervals. The lower route filters the independent 7,000-pair cloud at the exact Chen boundary `TV<=epsilon/(1-epsilon)` and constructs indistinguishable contaminated laws.

![Worst-location estimator error and the independent equal-law lower both scale with contamination.](images/c5-robust-rate.png)

Worst-case Hellinger-squared has fitted epsilon exponent `1.6712`. The all-estimator lower Hellinger bound has exponent `0.92916` (H² exponent `1.85833`) over nine epsilon levels from `1e-5` to `0.1`, with no saturated search steps. A benign-contaminant control is rejected.

The proof-level route checks the Yatracos expectation transfer, continuous-amplitude extension, coefficient budget `0.3308206>0.33`, exact equal-law condition, and dimension-preserving tensorization.

## Evidence and limits

| Claim | Paper result | Direct observed evidence | Assessment |
| --- | --- | --- | --- |
| C1 | chi-square/TV bound with exact logarithmic exponent | 420 exact cells, zero violations, max ratio `0.008997` | VERIFIED, MEDIUM |
| C2 | `H<=TV^(1-o(1))` | 420 exact cells, zero violations, max ratio `0.003787` | VERIFIED, MEDIUM |
| C3 | explicit sharp `0.33/log log` sequence | 11 orders, all pass, ratio `1.217`–`46.636` | VERIFIED, MEDIUM |
| C4 | TV minimax characterization | upper slope `-0.431`, Le Cam lower `-0.500` | VERIFIED, MEDIUM |
| C5 | robust H² upper and matching lower | upper H² slope `1.671`, lower H slope `0.929` | VERIFIED, MEDIUM |

The sweeps cover explicit one-dimensional compact-support submodels; they do not mechanically enumerate every mixture in the universal theorem domains. The verdict combines these direct experiments with independently reconstructed symbolic certificates and pinned primary-source premises. The absence of proof-assistant formalization is the principal remaining validation risk.

The successful scaled run used Hugging Face `cpu-upgrade`, exposed 64 logical CPUs, and pinned every numerical library to one thread. Its scaled stage ran in `7.999s`; no GPU was used. The fixed cumulative command is:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Important lineage: [scaled direct evidence](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/scaled-direct-evidence-judge-remediation), [universal certificate](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/universal-proof-certificate-remediation), and [proper Yatracos audit](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/yatracos-lower-pair-and-rate-audit).
