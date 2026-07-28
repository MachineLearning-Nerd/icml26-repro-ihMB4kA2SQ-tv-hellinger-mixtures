# Source-complete theorem proof replay

This artifact supersedes the earlier dependency-ledger kernel. It does not infer a universal theorem from finite numerical cells. Instead it replays the paper's proof chain, expands every internal dependency, pins each external theorem to its primary source, checks the assumption map, and machine-checks the decisive algebraic and asymptotic reductions.

## Pinned sources

| Source | SHA-256 | Role |
| --- | --- | --- |
| paper | `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d` | five theorem statements and all internal proofs |
| jia | `463b2b1e68d964f65c3ae4a0687ed88563d37e9508fbb92cb21a3f974ad9b56a` | C4 compact Hellinger local-entropy minimax theorem |
| chen | `7a166a8042adc601c39da0f178fe1ec941d1ed0750e2ad3ecf079c43f1395f88` | C5 equal-contamination lower-bound lemma |
| ma | `9ee096868b49068b4322243b6ff6e8f14f6f77c18db393843698f2731564ecbd` | C5 compact finite-mixture approximation/entropy input |

## Closed proof graph

| Claim | Internal proof nodes expanded | External primary theorem imports | Unresolved |
| --- | --- | --- | --- |
| C1 | Hermite expansion; Mehler formula; Christoffel-Darboux bounds; restricted-range inequality; Nikolskii inequality; Lambert tail lemma; weighted L1-L2 theorem; translation/Jensen reduction | none | **0** |
| C2 | C1; pointwise Hellinger/chi-square identity | none | **0** |
| C3 | Chebyshev inverse-Vandermonde lemma; moment recurrence; Poisson tail; Gaussian norm asymptotics; two mixture transformations; monotone subsequence | none | **0** |
| C4 | C2; proper projection; inverse-map repair; tail-to-risk | Jia et al. compact Hellinger local-entropy minimax theorem | **0** |
| C5 | C2; C3 continuous-amplitude construction; Yatracos deterministic inequality; integrated empirical-process tail; subadditive transfer; two-point metric risk | Ma-Wu-Yang compact finite-mixture approximation theorem; Chen-Gao-Ren equal-contamination lemma | **0** |

## Machine-checked replay

### C1 — DISCHARGED

Proof route: Hermite expansion -> Mehler/CD -> restricted range and Nikolskii -> Lambert/tail -> weighted L2 -> Jensen.

Checked witnesses:

- Mehler Gaussian determinant
- 66 complete multinomial cells
- Lambert monotonicity
- tail/norm constants
- mixture-denominator Jensen identity
- exact exponent substitution

### C2 — DISCHARGED

Proof route: C1 plus pointwise Hellinger/chi-square integrand identity.

Checked witnesses:

- (chi integrand)/(H integrand)=(sqrt(p/q)+1)^2

### C3 — DISCHARGED

Proof route: Chebyshev/Vandermonde construction -> recurrence tail -> Gaussian norms -> lambda transforms -> monotone subsequence.

Checked witnesses:

- two gamma log limits
- sharp coefficient 0.331483527757052000 > 0.33
- recursive monotone-subsequence rule

### C4 — DISCHARGED

Proof route: Jia local-entropy theorem -> projection -> C2 inverse -> Fano tail-to-risk.

Checked witnesses:

- cube-to-ball assumption map
- delta/2 inverse repair
- same-delta mutation has limit -delta**2 - 4*delta - 4

### C5 — DISCHARGED

Proof route: Ma entropy -> proper Yatracos upper; C3 continuous amplitude -> Chen equal-law lower.

Checked witnesses:

- J monotonicity/concavity
- integrated Hoeffding union tail
- tensor/parametric entropy exponent
- Chen boundary
- continuous-amplitude sharpness margin

## What this certificate does and does not claim

It is an independently executable replay of the proof transcript and its quantifier-carrying reductions. Primary theorems from Jia et al., Ma–Wu–Yang, and Chen–Gao–Ren are imported exactly as cited, with their source hashes and assumptions exposed; they are not silently treated as numerical facts. This is not a Lean/Coq formalization of measure theory.
