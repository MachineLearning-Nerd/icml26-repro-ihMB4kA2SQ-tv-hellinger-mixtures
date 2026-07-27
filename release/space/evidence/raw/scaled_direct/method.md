# Method

The parameter grids, horizons, and contamination locations are committed independently of the target formulas. C1/C2 use direct density integration and a denser-grid checker. C3 uses the paper's high-precision Chebyshev construction and an independent quadrature engine. C4 combines a sample-based NNLS density fit with a Le Cam two-point search. C5 maximizes sample risk over a fixed Q grid and separately searches Chen-admissible equal-law pairs. All gates and negative controls are fail-closed.
