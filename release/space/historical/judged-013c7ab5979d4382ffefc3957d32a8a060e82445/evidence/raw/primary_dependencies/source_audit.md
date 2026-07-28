# Primary-source audit for Claims 4 and 5

Retrieved 2026-07-25 with User-Agent `OpenResearch-Reproduction/1.0 (contact: research-audit)`.

| Dependency | URL | SHA-256 | Exact anchor |
|---|---|---|---|
| Jia, Polyanskiy, Wu (2023) | `https://export.arxiv.org/e-print/2306.12308` | `463b2b1e68d964f65c3ae4a0687ed88563d37e9508fbb92cb21a3f974ad9b56a` | `colt2023-sample.tex`, Corollary `cor-1` and “Proof of Corollary cor-1” |
| Chen, Gao, Ren (2018) | `https://export.arxiv.org/e-print/1506.00691` | `7a166a8042adc601c39da0f178fe1ec941d1ed0750e2ad3ecf079c43f1395f88` | `lower_R2.tex`, equation `eq:mod`, theorem `thm:lower`; supplementary equal-contamination construction |

## Claim 4 mapping

Jia Corollary 11 quantifies over any Hellinger-compact subclass of Gaussian mixtures whose mixing laws are supported on a Euclidean ball. The paper’s class is explicitly Hellinger-compact, and `[-M,M]^d` is contained in `B_2(M sqrt(d))`. Its local covering-number definition and squared-Hellinger minimax characterization match Proposition 4.2 in the target paper. The cited proof explicitly invokes Fano on a local Hellinger ball.

## Claim 5 lower-bound mapping

Chen–Gao–Ren define the Huber modulus using `TV(P1,P2) <= epsilon/(1-epsilon)` and construct contaminations producing identical observed laws. The target paper’s sharp pair satisfies this condition after selecting/relabeling the sequence. Metric triangle inequality then gives squared-Hellinger loss at least one quarter of the pairwise squared Hellinger distance for one of the two parameters.

## Limitations

This certificate resolves the exact imported statements and assumption maps. It does not by itself discharge the target paper’s internal C1/C3 analytic construction, on which the final exponents still depend.
