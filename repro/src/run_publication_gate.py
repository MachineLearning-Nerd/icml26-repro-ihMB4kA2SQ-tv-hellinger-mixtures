"""Fail closed unless the pinned five-claim certificate and tests pass."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    # Preserve the historical judged checks as a cumulative regression suite.
    verification = ROOT / "outputs" / "verification.json"
    subprocess.run(
        [sys.executable, "repro/src/verify_tv_hellinger.py", "--output", str(verification)],
        cwd=ROOT,
        check=True,
    )
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "repro/tests", "-v"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "repro/src/verify_claims_1_3.py"], cwd=ROOT, check=True)
    certificate = json.loads(verification.read_text())
    assert certificate["verified_claims"] == 5
    assert certificate["falsified_claims"] == 0
    assert all(certificate["negative_controls"].values())
    gate = {
        "paper": "ihMB4kA2SQ",
        "gate": "passed",
        "tests_passed": True,
        "publication_gate_passed": True,
        "verified_claims": 5,
        "falsified_claims": 0,
        "verification": "outputs/verification.json",
        "tests": "repro/tests",
        "scope": certificate["scope"],
        "current_claim_suite": ".openresearch/artifacts/claim_1_3/result.json",
    }
    (ROOT / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2) + "\n")
    print(json.dumps(gate, indent=2))


if __name__ == "__main__":
    main()
