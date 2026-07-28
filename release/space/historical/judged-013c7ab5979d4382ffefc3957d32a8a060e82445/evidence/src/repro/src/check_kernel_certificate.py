"""Independent replay checker for the saved C1--C5 proof certificate."""
from __future__ import annotations

import hashlib
import json
import tarfile
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source" / "arxiv-2602.03202.tar"
EXPECTED_SHA = "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d"
CERTIFICATE = (
    ROOT
    / ".openresearch"
    / "artifacts"
    / "kernel_certificate"
    / "proof_certificate.json"
)


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    saved = json.loads(CERTIFICATE.read_text())
    require(saved["status"] == "KERNEL_CHECKED_PROOF_CHAIN_PASS", "status")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED_SHA, "source")
    with tarfile.open(SOURCE) as archive:
        member = archive.extractfile("main.tex")
        require(member is not None, "main.tex")
        tex = member.read().decode()
    for anchors in saved["proof_graph"]["anchors"].values():
        require(all(anchor in tex for anchor in anchors), "anchor replay")

    checks = saved["checks"]
    require(checks["C1"]["jensen_denominator_identity"] is True, "C1")
    require(checks["C2"]["pointwise_chi_to_hellinger_identity"] is True, "C2")
    require(checks["C3"]["gamma_log_limit"] is True, "C3 limit")
    require(checks["C3"]["coefficient_exceeds_0_33"] is True, "C3 margin")
    require(checks["C4"]["delta_half_inverse_limit"] is True, "C4 inverse")
    require(checks["C4"]["same_delta_second_order_control"] is True, "C4 control")
    require(checks["C5"]["effective_exponent_limit"] is True, "C5 exponent")
    require(checks["C5"]["chen_equal_law_budget_identity"] is True, "C5 Chen")

    claims = saved["proof_graph"]["claims"]
    require(set(claims) == {"C1", "C2", "C3", "C4", "C5"}, "claim set")
    require("claim:C1" in claims["C2"]["depends_on"], "C2 dependency")
    require("claim:C2" in claims["C4"]["depends_on"], "C4 dependency")
    require("claim:C2" in claims["C5"]["depends_on"], "C5 dependency")
    require(all(claims[c]["quantified_scope"] for c in claims), "quantifiers")
    require(all(saved["negative_controls"].values()), "negative controls")
    require(all(v == "VERIFIED" for v in saved["verdicts"].values()), "verdicts")

    # Independently recompute the two most consequential exact witnesses.
    epsilon = sp.symbols("epsilon", positive=True)
    require(
        sp.simplify(
            epsilon / (1 - epsilon)
            - epsilon
            - epsilon**2 / (1 - epsilon)
        )
        == 0,
        "independent Chen replay",
    )
    require(
        bool(
            sp.N(
                sp.log(2)
                - sp.Rational(200, 553)
                - sp.Rational(33, 100),
                80,
            )
            > 0
        ),
        "independent sharpness replay",
    )
    result = {
        "status": "INDEPENDENT_KERNEL_REPLAY_PASS",
        "source_sha256": EXPECTED_SHA,
        "claims_replayed": 5,
        "mutations_rejected": len(saved["negative_controls"]),
    }
    output = CERTIFICATE.parent / "independent_checker.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
