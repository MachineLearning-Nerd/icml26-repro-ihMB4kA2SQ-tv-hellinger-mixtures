# Method

For each configured odd order, solve the exact Vandermonde moment system from
Lemma 3.2 at 100 decimal digits. Build `pi0/eta0`, then the paper's `lambda_n`
mixture `pi1/eta1`, then `pi2 = pi1/4 + 3 eta1/4`.

All distances are evaluated from density ratios relative to the standard normal,
which avoids subtracting nearly equal tiny densities. The primary integration is
768-point Gauss-Hermite quadrature. The independent checker reconstructs the
weights with 20 extra decimal digits and repeats every distance at 1536 points.

The run exits nonzero for an invalid probability measure, a failed Chebyshev or
moment identity, checker disagreement, failure of either upper-bound exponent
term, fewer than two observed sharpness cases, or a control that does not fail.
