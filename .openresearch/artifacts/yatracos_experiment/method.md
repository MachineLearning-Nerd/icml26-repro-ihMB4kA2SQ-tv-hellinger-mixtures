# Proper Yatracos Huber experiment

The experiment constructs a committed 17-member cover of one-dimensional
Gaussian location mixtures supported in `[-1,1]`. For all 136 density pairs it
builds the exact Yatracos comparison set on a fixed quadrature grid. The proper
estimator minimizes the maximum empirical discrepancy over those sets.

The calibration grid uses sample sizes `100, 200, 400, 800, 1600` and
contamination levels `0, .02, .05, .10, .20`, chosen independently of the
paper's formulas. Four truth mixtures and 40 deterministic replicates are
used. For each truth and contamination level, a worst point-mass contaminant
is selected from `{-6,-3,3,6}` at the population level, independent of sample
horizon.

Clean finite-class minimax lower bounds exhaust all cover pairs using a Le Cam
two-point certificate. Huber lower bounds exhaust all pairs satisfying the
Chen equal-law condition. Student-t 95% intervals quantify Monte Carlo
uncertainty.
