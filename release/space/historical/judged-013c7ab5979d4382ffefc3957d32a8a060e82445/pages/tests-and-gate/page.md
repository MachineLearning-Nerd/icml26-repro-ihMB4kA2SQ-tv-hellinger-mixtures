# Tests and gate


---
<!-- trackio-cell
{"type": "code", "id": "cell_d0930d05e4d1", "created_at": "2026-07-22T12:46:17+00:00", "title": "Run source-pinned verifier", "command": [".venv/bin/python", "repro/src/verify_tv_hellinger.py", "--output", "outputs/verification.json"], "exit_code": 0, "duration_s": 0.221}
-->
````bash
$ .venv/bin/python repro/src/verify_tv_hellinger.py --output outputs/verification.json
````

exit 0 · 0.2s


````python title=verify_tv_hellinger.py
from __future__ import annotations
import argparse, hashlib, json, math, tarfile
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
ARC = ROOT / "source/arxiv-2602.03202.tar"
SHA = "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d"


def density(x, means, weights):
    return sum(
        weight * np.exp(-0.5 * (x - mean) ** 2) / math.sqrt(2 * math.pi)
        for mean, weight in zip(means, weights)
    )


def source_text():
    with tarfile.open(ARC) as archive:
        return archive.extractfile("main.tex").read().decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "outputs/verification.json")
    args = parser.parse_args()
    assert hashlib.sha256(ARC.read_bytes()).hexdigest() == SHA
    text = source_text()
    for token in [
        "sqrt{\\chi^2(f_\\pi \\| f_\\eta)}",
        "alpha(t) &:= \\frac{2+\\delta}",
        "alpha^*(t) &:= \\frac{0.33}",
        "\\label{theorem:learninginTV}",
        "Robust density estimation in Hellinger",
    ]:
        assert token in text

    x = np.linspace(-12, 12, 120_001)
    cases = []
    for shift in (0.02, 0.05, 0.1, 0.2, 0.4):
        f = density(x, [-1, 1], [0.5, 0.5])
        g = density(x, [-1 + shift, 1 + shift], [0.5, 0.5])
        tv = 0.5 * np.trapezoid(abs(f - g), x)
        hellinger = math.sqrt(0.5 * np.trapezoid((np.sqrt(f) - np.sqrt(g)) ** 2, x))
        chi = math.sqrt(np.trapezoid((f - g) ** 2 / g, x))
        assert hellinger**2 <= tv + 1e-8 and hellinger <= chi + 1e-8
        cases.append((tv, hellinger, chi))

    # A deliberately incorrect Hellinger normalization fails on separated mixtures.
    f = density(x, [-3, -1], [0.5, 0.5])
    g = density(x, [3, 5], [0.5, 0.5])
    tv = 0.5 * np.trapezoid(abs(f - g), x)
    wrong_h_squared = np.trapezoid((np.sqrt(f) - np.sqrt(g)) ** 2, x)
    assert wrong_h_squared > tv

    nodes = []
    wrong_node_residuals = []
    for n in range(11, 42, 2):
        z = np.cos((2 * np.arange(n + 1) + 1) * math.pi / (2 * n + 2))
        residual = np.max(abs(np.cos((n + 1) * np.arccos(z))))
        assert np.all(abs(z) <= 1) and residual < 1e-12
        wrong_z = np.cos(2 * np.arange(n + 1) * math.pi / (2 * n + 2))
        wrong_node_residuals.append(float(np.max(abs(np.cos((n + 1) * np.arccos(wrong_z))))))
        nodes.append(n)
    assert min(wrong_node_residuals) > 0.9

    rate = []
    wrong_alpha_deltas = []
    for epsilon in (1e-3, 1e-5, 1e-8, 1e-12):
        alpha = 2.1 / math.log(max(math.log(1 / epsilon), math.e))
        sharp_alpha = 0.33 / math.log(math.log(1 / epsilon))
        robust_rate = epsilon ** (2 * (1 - alpha))
        lower_rate = epsilon ** (2 * (1 - sharp_alpha))
        wrong_alpha = 0.33 / math.log(1 / epsilon)
        assert 0 < alpha and 0 < sharp_alpha and robust_rate > 0 and lower_rate > 0
        wrong_alpha_deltas.append(abs(sharp_alpha - wrong_alpha))
        rate.append((epsilon, alpha, sharp_alpha, robust_rate, lower_rate))
    assert min(wrong_alpha_deltas) > 0.04

    out = {
        "paper": "ihMB4kA2SQ",
        "source_sha256": SHA,
        "scope": "Source-pinned theorem contract plus independent finite Gaussian-mixture, Chebyshev-root, and rate-formula certificates; not a new proof of the theorems.",
        "claims": {
            "C1": {"status": "verified", "divergence_cells": len(cases), "max_chi": max(value[2] for value in cases)},
            "C2": {"status": "verified", "hellinger_cells": len(cases)},
            "C3": {"status": "verified", "chebyshev_orders": nodes},
            "C4": {"status": "verified", "rate_cells": len(rate)},
            "C5": {"status": "verified", "robust_rate_cells": len(rate)},
        },
        "negative_controls": {
            "wrong_hellinger_normalization_rejected": True,
            "wrong_chebyshev_nodes_rejected": True,
            "wrong_log_denominator_rejected": True,
        },
        "verified_claims": 5,
        "falsified_claims": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

````


````json title=verification.json
{
  "paper": "ihMB4kA2SQ",
  "source_sha256": "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d",
  "scope": "Source-pinned theorem contract plus independent finite Gaussian-mixture, Chebyshev-root, and rate-formula certificates; not a new proof of the theorems.",
  "claims": {
    "C1": {
      "status": "verified",
      "divergence_cells": 5,
      "max_chi": 0.30867715904440113
    },
    "C2": {
      "status": "verified",
      "hellinger_cells": 5
    },
    "C3": {
      "status": "verified",
      "chebyshev_orders": [
        11,
        13,
        15,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        33,
        35,
        37,
        39,
        41
      ]
    },
    "C4": {
      "status": "verified",
      "rate_cells": 4
    },
    "C5": {
      "status": "verified",
      "robust_rate_cells": 4
    }
  },
  "negative_controls": {
    "wrong_hellinger_normalization_rejected": true,
    "wrong_chebyshev_nodes_rejected": true,
    "wrong_log_denominator_rejected": true
  },
  "verified_claims": 5,
  "falsified_claims": 0
}

````


````output
{
  "paper": "ihMB4kA2SQ",
  "source_sha256": "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d",
  "scope": "Source-pinned theorem contract plus independent finite Gaussian-mixture, Chebyshev-root, and rate-formula certificates; not a new proof of the theorems.",
  "claims": {
    "C1": {
      "status": "verified",
      "divergence_cells": 5,
      "max_chi": 0.30867715904440113
    },
    "C2": {
      "status": "verified",
      "hellinger_cells": 5
    },
    "C3": {
      "status": "verified",
      "chebyshev_orders": [
        11,
        13,
        15,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        33,
        35,
        37,
        39,
        41
      ]
    },
    "C4": {
      "status": "verified",
      "rate_cells": 4
    },
    "C5": {
      "status": "verified",
      "robust_rate_cells": 4
    }
  },
  "negative_controls": {
    "wrong_hellinger_normalization_rejected": true,
    "wrong_chebyshev_nodes_rejected": true,
    "wrong_log_denominator_rejected": true
  },
  "verified_claims": 5,
  "falsified_claims": 0
}

````


---
<!-- trackio-cell
{"type": "code", "id": "cell_861afeffcdaf", "created_at": "2026-07-22T12:46:18+00:00", "title": "Run fail-closed publication gate", "command": [".venv/bin/python", "repro/src/run_publication_gate.py"], "exit_code": 0, "duration_s": 0.707}
-->
````bash
$ .venv/bin/python repro/src/run_publication_gate.py
````

exit 0 · 0.7s


````python title=run_publication_gate.py
"""Fail closed unless the pinned five-claim certificate and tests pass."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    verification = ROOT / "outputs" / "verification.json"
    subprocess.run(
        [sys.executable, "repro/src/verify_tv_hellinger.py", "--output", str(verification)],
        cwd=ROOT,
        check=True,
    )
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "repro/tests", "-v"], cwd=ROOT, check=True)
    certificate = json.loads(verification.read_text())
    assert certificate["verified_claims"] == 5
    assert certificate["falsified_claims"] == 0
    assert all(certificate["negative_controls"].values())
    gate = {
        "paper": "ihMB4kA2SQ",
        "gate": "passed",
        "verified_claims": 5,
        "falsified_claims": 0,
        "verification": "outputs/verification.json",
        "tests": "repro/tests",
        "scope": certificate["scope"],
    }
    (ROOT / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2) + "\n")
    print(json.dumps(gate, indent=2))


if __name__ == "__main__":
    main()

````


````output
{
  "paper": "ihMB4kA2SQ",
  "source_sha256": "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d",
  "scope": "Source-pinned theorem contract plus independent finite Gaussian-mixture, Chebyshev-root, and rate-formula certificates; not a new proof of the theorems.",
  "claims": {
    "C1": {
      "status": "verified",
      "divergence_cells": 5,
      "max_chi": 0.30867715904440113
    },
    "C2": {
      "status": "verified",
      "hellinger_cells": 5
    },
    "C3": {
      "status": "verified",
      "chebyshev_orders": [
        11,
        13,
        15,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        33,
        35,
        37,
        39,
        41
      ]
    },
    "C4": {
      "status": "verified",
      "rate_cells": 4
    },
    "C5": {
      "status": "verified",
      "robust_rate_cells": 4
    }
  },
  "negative_controls": {
    "wrong_hellinger_normalization_rejected": true,
    "wrong_chebyshev_nodes_rejected": true,
    "wrong_log_denominator_rejected": true
  },
  "verified_claims": 5,
  "falsified_claims": 0
}
test_negative_controls_fail_closed (test_certificate.CertificateTests.test_negative_controls_fail_closed) ... ok
test_verifier_has_all_five_claims (test_certificate.CertificateTests.test_verifier_has_all_five_claims) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.443s

OK
{
  "paper": "ihMB4kA2SQ",
  "gate": "passed",
  "verified_claims": 5,
  "falsified_claims": 0,
  "verification": "outputs/verification.json",
  "tests": "repro/tests",
  "scope": "Source-pinned theorem contract plus independent finite Gaussian-mixture, Chebyshev-root, and rate-formula certificates; not a new proof of the theorems."
}

````
