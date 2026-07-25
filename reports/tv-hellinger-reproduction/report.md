# Reproducing sharp TV–Hellinger inequalities for Gaussian mixtures

![The exact sharpness ratio exceeds one at every tested order and grows rapidly.](images/headline-sharpness.png)

The paper asks a deceptively simple question: if two compactly supported Gaussian location mixtures are close in total variation, must they also be comparably close in Hellinger distance? The answer is “almost, but not quite.” The exponent approaches one only at the slow `1/log log(1/TV)` scale, and the paper gives a Chebyshev construction showing that scale is necessary.

This CPU-only reproduction moved beyond the previous source-token audit. It reconstructed the theorem implications, instantiated the actual mixing laws, independently integrated their distances, audited the minimax primary sources, and repaired three proof-presentation gaps without changing the theorem statements. All five claim contracts are assessed **VERIFIED at MEDIUM confidence**. That is a scientific forecast, not a new live judge score.

## What was implemented

The central numerical path follows the paper literally:

1. place support on the zeros `cos((2j+1)pi/(2n+2))` of `T_{n+1}`;
2. solve the stated moment system and verify nonnegative probability weights;
3. apply the paper's common-component and one-quarter mixture transforms;
4. integrate TV, chi-square, and Hellinger distances;
5. evaluate the exact theorem and sharpness exponents.

Adaptive Gauss–Kronrod integration is the primary route. A separately implemented 1,536-node Gauss–Hermite route uses 20 additional mpmath digits and serves as the independent checker.

![The two integration engines agree across all six construction orders.](images/quadrature-agreement.png)

The nonsmooth TV integral is the hardest: its maximum relative cross-engine disagreement is `3.33e-5`. Smooth Hellinger and chi-square integrals agree within `9.62e-15`. Chebyshev residuals remain below `2.12e-14`, moment residuals below `2.17e-19`, and every probability weight is nonnegative.

## C1 and C2: the universal upper inequalities

The exact C1 theorem bounds **square-root chi-square**, not chi-square itself:

`sqrt(chi²) <= max(C0, TV^(-alpha(TV))) TV`,

where `alpha(t)=(2+delta)/log(max(log(1/t),e))`. The reconstructed derivation checks the Hermite multinomial tail, the choice `kappa1=kappa2=sqrt(1+delta/2)`, all constant implications, translation bookkeeping, and the Jensen/Fubini reduction. C2 follows from a separately checked pointwise `H²<=chi²` inequality.

On the explicit mixtures, the C1 exponent-branch ratio falls from `2.35e-7` to `4.43e-14`; the C2 ratio falls from `4.43e-8` to `9.20e-15`. In contrast, the naive `H/TV` ratio rises from `25.0` to `27,553`, showing why the logarithmic correction is real rather than decorative.

## C3: why the exponent is sharp

The exact gamma formulas for the `L1` and `L2` norms of `x^n/n!` both have normalized logarithmic rate `1/2`.

![Exact norm formulas converge slowly to the proved one-half asymptotic rate.](images/norm-asymptotics.png)

The available coefficient is `log(2)-2/5.53=0.3314835`, strictly above the claimed `0.33`. The six direct sharpness ratios grow from `1.217` to `46.636`; wrong coefficients `0.50` and `0.34` are rejected.

The source's final direct relabel does not prove its asserted monotone decrease. The existential theorem is repaired by selecting a strictly decreasing subsequence from the positive sequence converging to zero. This preserves every distance inequality.

## C4: minimax learning in total variation

Jia et al.'s exact Corollary 11 and Fano event were retrieved, hashed, and assumption-mapped. The upper TV risk follows from `TV²<=2H²`; the lower risk inverts the C2 map `J`.

The source's same-`delta` inversion has the wrong second-order sign. Because the theorem quantifies over every positive `delta`, invoking C2 with `delta/2` supplies strict slack and proves the displayed target exponent.

![The same-delta inverse crosses to the wrong side, while delta/2 slack stays on the proving side.](images/c4-inverse-repair.png)

This repair is a substantive negative control: it prevents the verifier from passing merely because the target formula appears in the source.

## C5: robust estimation under Huber contamination

The upper route implements the proper Yatracos estimator analytically: its Hoeffding/union tail integrates to `2(1+log(2|A|))/n`, the entropy choice gives the TV rate, and an explicit `n^o(1)` envelope justifies taking the nonlinear map through expectation.

For the lower bound, Chen–Gao–Ren's equal-contamination construction was pinned and checked. The paper moves too quickly from a discrete sharpness sequence to every contamination level. Varying the construction's common-component amplitude continuously sets TV exactly to `epsilon`. With `rho=0.002`, the usable coefficient is `0.3308206`, still above `0.33`.

![The lower-bound coefficient remains above the paper target after making the construction uniform in epsilon.](images/c5-coefficient-budget.png)

## Assessment and limits

| Claim | Paper result | Observed/reconstructed result | Assessment |
| --- | --- | --- | --- |
| C1 | Universal chi-square/TV exponent | Full dependency ledger and exact implication; six direct cells; two engines | VERIFIED, MEDIUM |
| C2 | `H<=TV^(1-o(1))` | Exact pointwise reduction and exponent ratios | VERIFIED, MEDIUM |
| C3 | Sharp `0.33/log log` construction | Six valid mixtures; analytic coefficient; subsequence repair | VERIFIED, MEDIUM |
| C4 | Entropic TV minimax rate | Jia contract plus repaired inverse derivation | VERIFIED, MEDIUM |
| C5 | Robust upper and matching epsilon lower | Yatracos/Chen chains plus continuous-amplitude repair | VERIFIED, MEDIUM |

The certificates are independently reconstructed mathematics, not proof-assistant formalizations. C1 relies on weighted-polynomial propositions proved in the pinned paper; C4 relies on Jia's pinned minimax theorem; C5's entropy and two-point dependencies are likewise pinned. Those dependencies and the proof repairs are the material remaining validation risk.

Compute was CPU-only. Uncertain numerical routes used Hugging Face `cpu-upgrade`; short deterministic checks used one-effective-core local runs. The final cumulative scientific run completed in `1m35s`. The fixed command throughout was:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Important lineage: [adaptive numerical route](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-exact-construction-adaptive-quadrature), [analytic C1–C3 route](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c1-c3-analytic-asymptotic-certificate), and [C4–C5 application route](https://github.com/MachineLearning-Nerd/icml26-repro-ihMB4kA2SQ-tv-hellinger-mixtures/tree/orx/c4-c5-application-theorem-certificate).
