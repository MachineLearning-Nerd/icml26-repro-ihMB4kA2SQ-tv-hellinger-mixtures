# Evaluation

Required pass conditions:

- the proper finite-cover Yatracos estimator runs at every committed horizon,
  contamination level, truth, and seed;
- all 171 comparison sets independently recover pairwise TV to `2e-12`;
- clean and contaminated risks have 95% intervals;
- the finite-class clean and Huber lower bounds exhaust the complete cover;
- an empty-comparison-class estimator is rejected as a negative control.

The result is estimator-level corroboration for C4--C5. It does not replace
the proof-level universal-reduction certificate.
