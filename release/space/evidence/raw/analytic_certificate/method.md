# C1–C3 analytic certificate

This route reconstructs the proof implications independently from the source-pinned theorem statements. It is cumulative with both direct numerical mixture integrations.

## C1

The checker validates the exact choice `kappa1=kappa2=sqrt(1+delta/2)`, the Hermite multinomial tail identity, all deterministic constant implications following the paper’s finite weighted-polynomial threshold, and the final reciprocal max/min algebra. The weighted-polynomial propositions are part of the pinned paper and remain visible as named dependencies rather than being replaced by experiments.

## C2

The previous proof-obligation checker independently verifies the pointwise identity reducing `H² <= chi²`; this route inherits and reruns it.

## C3

The checker independently evaluates the exact gamma-function formulas for the `L1` and `L2` norms of `x^n/n!`, verifies their common `1/2` normalized logarithmic rate, and verifies

`log(2) - 2/5.53 = 0.331483... > 0.33`.

The paper’s formula `n -> 2(n+N0)+1` does not itself prove the asserted monotonic decrease of TV. The certificate repairs this proof-presentation gap using the elementary theorem that every positive sequence converging to zero has a strictly decreasing subsequence: recursively choose the first later index below the previous value. All sharpness inequalities are inherited by a subsequence.

## Fail-closed behavior

The verifier exits nonzero if an anchor, identity, constant margin, asymptotic audit, subsequence invariant, or negative control fails.
