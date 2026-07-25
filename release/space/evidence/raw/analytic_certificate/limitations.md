# Limitations and deviations

- This is an independently reconstructed analytic certificate, not a Lean/Coq formalization.
- The source’s weighted-polynomial propositions are audited as named internal lemmas. Their full proofs remain in the pinned source.
- Finite gamma-function rows are diagnostics for the exact formulas; the asymptotic conclusion comes from Stirling’s formula in the reconstructed derivation, not extrapolation from those rows.
- The monotone-subsequence selection is an explicit correction to the source’s insufficient direct relabeling step. It does not alter the existential theorem statement or any distance inequality.
