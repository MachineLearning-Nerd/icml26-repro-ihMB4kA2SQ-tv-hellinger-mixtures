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
    subprocess.run([sys.executable, "repro/src/verify_proof_obligations.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "repro/src/verify_primary_dependencies.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "repro/src/verify_analytic_certificate.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "repro/src/verify_application_certificate.py"], cwd=ROOT, check=True)
    subprocess.run(
        [sys.executable, "reports/tv-hellinger-reproduction/build_figures.py"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "marimo", "check", "notebooks/tv_hellinger_reproduction.py"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run([sys.executable, "repro/src/verify_release_candidate.py"], cwd=ROOT, check=True)
    certificate = json.loads(verification.read_text())
    release = json.loads(
        (ROOT / "release" / "space" / "evidence" / "release" / "release_check.json").read_text()
    )
    assert certificate["verified_claims"] == 5
    assert certificate["falsified_claims"] == 0
    assert all(certificate["negative_controls"].values())
    assert release["status"] == "RELEASE_CANDIDATE_PASS"
    assert all(value == "VERIFIED" for value in release["claim_verdicts"].values())
    gate = {
        "paper": "ihMB4kA2SQ",
        "gate": "release_candidate_passed",
        "tests_passed": True,
        "publication_gate_passed": True,
        "publication_blocker": None,
        "current_claim_verdicts": {
            "C1": "VERIFIED",
            "C2": "VERIFIED",
            "C3": "VERIFIED",
            "C4": "VERIFIED",
            "C5": "VERIFIED",
        },
        "claim_confidence": {
            "C1": "MEDIUM",
            "C2": "MEDIUM",
            "C3": "MEDIUM",
            "C4": "MEDIUM",
            "C5": "MEDIUM",
        },
        "verified_claims": 5,
        "falsified_claims": 0,
        "historical_rejected_baseline_regression_passed": True,
        "verification": "outputs/verification.json",
        "tests": "repro/tests",
        "scope": "Source-pinned exact claim contracts, reconstructed analytic theorem implications, direct Gaussian-mixture constructions, independent numerical checkers, and negative controls; not a proof-assistant formalization.",
        "current_claim_suite": ".openresearch/artifacts/claim_1_3/result.json",
        "proof_obligations": ".openresearch/artifacts/proof_obligations/result.json",
        "primary_dependencies": ".openresearch/artifacts/primary_dependencies/result.json",
        "analytic_certificate": ".openresearch/artifacts/analytic_certificate/result.json",
        "application_certificate": ".openresearch/artifacts/application_certificate/result.json",
        "release_candidate": "release/space/evidence/release/release_check.json",
    }
    serialized_gate = json.dumps(gate, indent=2) + "\n"
    (ROOT / "outputs" / "publication_gate.json").write_text(serialized_gate)
    (
        ROOT
        / "release"
        / "space"
        / "evidence"
        / "raw"
        / "outputs"
        / "publication_gate.json"
    ).write_text(serialized_gate)
    subprocess.run([sys.executable, "repro/src/verify_release_candidate.py"], cwd=ROOT, check=True)
    print(json.dumps(gate, indent=2))


if __name__ == "__main__":
    main()
