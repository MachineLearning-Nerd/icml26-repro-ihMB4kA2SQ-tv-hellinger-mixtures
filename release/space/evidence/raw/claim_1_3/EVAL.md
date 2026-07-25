# Evaluation contract

Run the inherited fixed command:

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

The historical rejected baseline runs first as a regression check. The current
verifier is `repro/src/verify_claims_1_3.py`. Its complete JSON, independent
checker, controls, runtime, CPU visibility, seed, and Git SHA are printed to the
OpenResearch log and written below this directory.
