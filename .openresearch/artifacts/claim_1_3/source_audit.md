# Source audit

- Primary source: `https://export.arxiv.org/e-print/2602.03202`
- Retrieved with an explicit browser User-Agent at `2026-07-25T04:48:56Z`.
- SHA-256: `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`.
- C1 anchor: `main.tex`, Theorem `theorem:uniformTV` (paper Theorem 2.1).
- C2 anchor: `main.tex`, Corollary `corollary:uniformTV` (paper Corollary 2.4).
- C3 anchors: `main.tex`, Theorem `theorem:sharp`, Lemma
  `lemma:construction`, and definitions `pi0`, `pi1`, `pi2`.

The source bounds **the square root** of chi-squared divergence in C1. The
finite verifier preserves that square root and does not silently test chi-square
itself. C1 and C2 quantify over arbitrary bounded-support mixing measures and an
unknown distribution-independent constant. C3 is existential and asymptotic,
with its displayed all-index sequence obtained only after relabelling beyond an
unspecified universal `N0`.
