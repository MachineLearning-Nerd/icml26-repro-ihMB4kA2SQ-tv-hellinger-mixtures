# C4–C5 application theorem certificate

This route reconstructs the application proofs from the pinned paper and the already pinned Jia and Chen–Gao–Ren primary sources. It contains no formula-derived simulation budget and does not claim that a finite estimator experiment proves a minimax theorem.

## Claim 4

The upper bound follows from `TV² <= 2 H²` and Jia et al.’s local-entropy characterization. The lower bound converts Jia’s Fano event through the monotone map

`J(t) = max(C0 t, t^(1-alpha(t)))`.

The source proof reuses the same `delta` when inverting `J`. An exact expansion shows that route has a negative second-order term and cannot yield the displayed constant-factor lower bound. The repaired derivation invokes Corollary 2.4 with `delta/2`; since the theorem asks for every target `delta>0`, this supplies the necessary slack and yields the advertised exponent.

## Claim 5 upper bound

The checker reconstructs the proper Yatracos estimator, integrates its Hoeffding/union tail exactly, checks the entropy-scale substitution, proves eventual monotonicity and concavity of `G(t)=t^(1-alpha(t))`, and audits the expectation transfer. The latter uses an explicit `n^o(1)` envelope rather than treating a pointwise inequality as if it automatically commuted with expectation. Specifically, with `a_n=2c/log log n`, split `U=log(1/t)` at `U=sqrt(log n)`: above the split the envelope exponent is nonpositive, while below it the log-envelope is at most `c sqrt(log n)=o(log n)`.

## Claim 5 lower bound

The paper moves directly from a discrete sharpness sequence to every contamination level. Monotone convergence alone does not justify that step. The repaired route returns to the explicit construction and varies its mixing amplitude continuously. For order

`m(epsilon) ~ 2(1-rho) log(1/epsilon)/log log(1/epsilon)`, with `rho=0.002`,

the maximum admissible TV is asymptotically larger than `epsilon`, so the amplitude can set TV exactly to `epsilon`. The likelihood-ratio bound and Hellinger lower bound remain valid for every smaller amplitude. The available coefficient

`(log(2)-2/5.53)(1-rho) = 0.330820...`

is still strictly above `0.33`. Chen’s equal-contamination construction then makes the two observation laws identical, and the metric two-point argument gives the squared-Hellinger lower bound. Tensoring with common standard-Gaussian coordinates preserves TV and Hellinger exactly.

## Fail-closed behavior

The verifier exits nonzero if a source anchor, symbolic limit, empirical-process integral, entropy asymptotic, sharpness margin, primary-source condition, or negative control fails.
