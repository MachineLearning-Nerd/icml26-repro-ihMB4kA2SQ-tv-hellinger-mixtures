# C4 — minimax TV characterization

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

For every `delta>0` and every Hellinger-compact class `P` contained in the bounded-support Gaussian-mixture class `P_{M,d}`, Theorem 4.3 states

`epsilon_n^(2(1+(2+delta)/log(max(log(1/epsilon_n),e))))`

is a lower bound, up to constants, for the total-variation minimax squared risk, while `epsilon_n²` is an upper bound. Arbitrary and proper estimators agree up to constants. Here `epsilon_n` is the local-Hellinger-entropy rate defined by Jia et al.

## Primary-source assumptions

The exact source archive for Jia et al. (arXiv `2306.12308`) is pinned at SHA-256 `463b2b1e68d964f65c3ae4a0687ed88563d37e9508fbb92cb21a3f974ad9b56a`. Its Corollary 11, Hellinger compactness assumption, local covering number, and Fano proof event were located. The support map is exact:

`[-M,M]^d subset B_2(M sqrt(d))`.

## Reconstructed upper and lower bounds

The upper bound is `TV²<=2H²` plus Jia's entropy characterization. Projecting an arbitrary estimator back into `P` increases TV by at most a factor two, proving equivalence with proper estimators.

For the lower bound, Jia's Fano event has probability at least `1/2` at Hellinger threshold `epsilon_n/4`. C2 gives `H<=J(TV)`, where

`J(t)=max(C0 t,t^(1-alpha(t)))`.

Monotonic inversion and `E[X²]>=a² P(X>=a)` transfer that event to TV risk.

## Negative control and necessary repair

The source text appears to reuse the same `delta` when deriving the displayed inverse power. Exact asymptotic expansion rejects that step:

`L²[(1-(2+delta)/(L+log(1+(2+delta)/L)))(1+(2+delta)/L)-1]`

tends to `-(2+delta)²`, so the required constant-factor inequality has the wrong sign.

The theorem itself remains valid: for a target `delta>0`, invoke C2 with `delta/2`. The repaired first-order limit is `delta/2>0`, providing strict slack and exactly the theorem's target exponent. This is permitted by the theorem's “for every delta>0” quantifier.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Formal evidence SHA `de2c3a8fba29e433c552ce82c194196fefaaa4d8`; application checker runtime `2.116s`; one-effective-core estimate; 8 logical CPUs visible. This symbolic route is deterministic and uses no stochastic seed; cumulative numerical seed `260203202` is retained for the direct construction regression.

- [Application verifier](../../evidence/src/repro/src/verify_application_certificate.py)
- [Application certificate](../../evidence/raw/application_certificate/result.json)
- [Exact claim contract](../../evidence/raw/application_certificate/claim_contract.json)
- [Jia primary-source audit](../../evidence/raw/primary_dependencies/source_audit.md)
- [Primary dependency output](../../evidence/raw/primary_dependencies/result.json)
- [Limitations](../../evidence/raw/application_certificate/limitations.md)
