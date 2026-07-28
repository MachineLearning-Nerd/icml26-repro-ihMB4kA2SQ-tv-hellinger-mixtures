# Proof-kernel method

The generator pins the exact arXiv source, locates every theorem anchor, recomputes exact symbolic identities and limits, closes the dependency graph for each theorem conclusion, and rejects one mutated proof object per claim. `check_kernel_certificate.py` independently replays the saved certificate and exits nonzero on any mismatch.
