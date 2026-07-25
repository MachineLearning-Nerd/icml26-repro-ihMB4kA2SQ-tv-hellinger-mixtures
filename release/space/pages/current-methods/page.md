# Methods and reproducibility

## Fixed command and environment

The command was set once and inherited unchanged by the baseline and every child:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Environment: Python `3.12`, repository-level `.venv`, `uv` lockfile, NumPy `2.5.1`, SciPy `1.18.0`, mpmath `1.3.0`, SymPy `1.14.0`. See [`pyproject.toml`](../../evidence/src/pyproject.toml) and [`uv.lock`](../../evidence/src/uv.lock).

The paper archive was retrieved with User-Agent `OpenResearch-Reproduction/1.0 (contact: research-audit)` and has SHA-256 `dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d`. Jia and Chen–Gao–Ren retrieval URLs, date `2026-07-25`, and hashes are in the [source audit](../../evidence/raw/primary_dependencies/source_audit.md).

## Experiment lineage and compute

| Experiment | Backend | Estimate | Actual allocation | Runtime | Result |
| --- | --- | --- | --- | ---: | --- |
| Historical judged baseline | local | 1 effective core, <1m | local CPU | `5s` | Reproduced weak 0/10 baseline; rejected |
| Fixed-node Gauss–Hermite | HF `cpu-upgrade` | uncertain, so remote | 64 logical CPUs visible; one effective core | `13.104s` verifier | Independent C1–C3 route passed |
| Adaptive Gauss–Kronrod | HF `cpu-upgrade` | uncertain, so remote | 64 logical CPUs visible; one effective core | `29.722s` verifier | Independent C1–C3 route passed |
| Proof/dependency/application chain | local | 1 effective core, <5m | 8 logical CPUs visible | final cumulative `1m35s` | All scientific checkpoints passed |

HF billing cost was not exposed in `orx` logs; no cost is invented. No GPU was used. Seed: `260203202`. Evidence-generating Git SHA: `de2c3a8fba29e433c552ce82c194196fefaaa4d8`.

## Non-circular design

The six mixture orders were not selected by fitting the claimed slope. They instantiate the paper's explicit construction and are evaluated by two independent integration algorithms. Universal/minimax claims are concluded from reconstructed analytic implications and pinned primary-source theorems, not from the finite sweep. Formula-derived sample sizes or tolerances are not used as proof.

## Fail-closed suite

The cumulative entrypoint reruns the historical regression, unit tests, direct mixture construction, independent quadrature, proof obligations, primary dependencies, C1–C3 analytic certificate, C4–C5 application certificate, and release visibility gate. Any failed assertion exits nonzero.

- [Cumulative entrypoint](../../evidence/src/repro/src/run_publication_gate.py)
- [Unit tests](../../evidence/src/repro/tests/test_certificate.py)
- [Raw gate output from scientific checkpoint](../../evidence/raw/outputs/publication_gate.json)

That raw checkpoint intentionally says publication was false before candidate curation. The current release gate supersedes it; historical checkpoint states are preserved rather than rewritten.
