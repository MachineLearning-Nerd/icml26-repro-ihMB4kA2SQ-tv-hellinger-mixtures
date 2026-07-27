# Exact universal-reduction method

This route is separate from the finite Gaussian-mixture sweep. It hashes the
pinned arXiv source, locates every theorem and proof dependency, and checks the
universal algebraic/asymptotic reductions with exact SymPy expressions.

The checker covers the C1 exponent and norm chain, the pointwise C2
Hellinger/chi-square implication, exact C3 gamma-function limits and the
decreasing-subsequence repair, C4's delta/2 inverse-map repair, and both the C5
expectation transfer and continuous-amplitude lower-bound repair.

The fixed command is:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

The checker exits nonzero if a source anchor, identity, exact limit, strict
coefficient margin, or negative control fails.
