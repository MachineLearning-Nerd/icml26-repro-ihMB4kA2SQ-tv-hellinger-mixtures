# C5 — robust Hellinger upper and lower rates

**Verdict: VERIFIED. Confidence: MEDIUM.**

## Exact claim contract

Under `epsilon`-Huber contamination

`(1-epsilon) P_{f_pi} + epsilon Q`,

where `pi` is supported on `[-M,M]^d` and `Q` is arbitrary, Theorem 4.5 bounds the proper Yatracos estimator's expected squared-Hellinger error by

`epsilon^(2(1-(2+delta)/log(max(log(1/epsilon),e)))) + n^(-1+o_d(1))`

for every `delta>0`. Theorem 4.6 lower-bounds every estimator by the analogous contamination term with coefficient `0.33`.

## Upper bound reconstruction

The Yatracos class has at most `N²` sets. Integrating the exact Hoeffding/union tail

`min(1,2|A| exp(-n s²/2))`

gives `2(1+log(2|A|))/n`. With the paper's TV entropy bound and `eta=log(n)^(d/2)/sqrt(n)`, this yields TV squared risk `epsilon²+log(n)^(d+1)/n`.

For `G(t)=t^(1-alpha(t))`, exact derivatives show eventual increase and concavity. Hence `J(t)=max(C0t,G(t))` is subadditive. The expectation step is not assumed: an explicit envelope with `a_n=2c/log log n` is split at `log(1/t)=sqrt(log n)`, producing only an `n^o(1)` multiplier. This yields the claimed `n^(-1+o_d(1))` term.

## Lower bound reconstruction and repair

The Chen–Gao–Ren primary source is pinned at SHA-256 `7a166a8042adc601c39da0f178fe1ec941d1ed0750e2ad3ecf079c43f1395f88`. It proves that if `TV(P1,P2)<=epsilon/(1-epsilon)`, contamination laws can be chosen to make the two observed distributions identical. Metric triangle inequality then forces squared-Hellinger risk at least one quarter of the separation.

The paper jumps from C3's discrete sequence to every `epsilon`; monotone convergence alone does not justify that. The repair varies the explicit construction's mixing amplitude continuously. Choosing order

`m(epsilon) ~ 2(1-0.002) log(1/epsilon)/log log(1/epsilon)`

makes its admissible maximum TV asymptotically larger than `epsilon`, so the amplitude sets TV exactly to `epsilon`. The Hellinger/TV ratio is amplitude-invariant. Its coefficient budget is

`(log(2)-2/5.53)(1-0.002) = 0.3308205607 > 0.33`.

Tensoring with common standard-Gaussian coordinates preserves both distances exactly, covering every fixed dimension.

## Controls

The checker rejects the discrete-sequence-only inference, coefficient `0.34`, omission of the Yatracos union factor, and the incorrect stronger Chen threshold `TV<=epsilon` as an equivalence. All primary assumptions are explicit.

## Reproduce and download

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Formal evidence SHA `de2c3a8fba29e433c552ce82c194196fefaaa4d8`; application checker runtime `2.116s`; one-effective-core estimate; 8 logical CPUs visible. This symbolic route is deterministic and uses no stochastic seed; cumulative numerical seed `260203202` is retained for the direct construction regression.

- [Application verifier](../../evidence/src/repro/src/verify_application_certificate.py)
- [Raw application output](../../evidence/raw/application_certificate/result.json)
- [Exact claim contract](../../evidence/raw/application_certificate/claim_contract.json)
- [Primary dependency output](../../evidence/raw/primary_dependencies/result.json)
- [Method](../../evidence/raw/application_certificate/method.md)
- [Limitations](../../evidence/raw/application_certificate/limitations.md)
