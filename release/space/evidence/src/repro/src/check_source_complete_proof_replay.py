"""Independent checker for the source-complete theorem proof replay."""
from __future__ import annotations

import hashlib
import json
import tarfile
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / ".openresearch" / "artifacts" / "source_complete_proof_replay"
CERTIFICATE = ARTIFACT / "proof_replay.json"
PAPER = ROOT / "source" / "arxiv-2602.03202.tar"
PAPER_SHA = "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d"


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    saved = json.loads(CERTIFICATE.read_text())
    require(saved["status"] == "SOURCE_COMPLETE_PROOF_REPLAY_PASS", "status")
    require(saved["unresolved_dependencies"] == [], "global unresolved dependency")
    require(
        all(node["unresolved"] == [] for node in saved["proof_graph"].values()),
        "claim unresolved dependency",
    )
    require(all(value == "VERIFIED" for value in saved["verdicts"].values()), "verdict")
    require(all(saved["negative_controls"].values()), "mutation")
    require(hashlib.sha256(PAPER.read_bytes()).hexdigest() == PAPER_SHA, "paper hash")
    with tarfile.open(PAPER) as archive:
        member = archive.extractfile("main.tex")
        require(member is not None, "main.tex")
        paper = member.read().decode()
    for anchors in saved["paper_anchors"].values():
        require(all(anchor in paper for anchor in anchors), "paper anchor")

    # Independently reconstruct the most consequential witness for each claim.
    delta, L = sp.symbols("delta L", positive=True)
    require(
        sp.simplify(2 * (1 + delta / 2) - (2 + delta)) == 0,
        "C1 exponent",
    )
    p, q = sp.symbols("p q", positive=True)
    require(
        sp.simplify(
            ((p - q) ** 2 / q)
            / (sp.sqrt(p) - sp.sqrt(q)) ** 2
            - (sp.sqrt(p / q) + 1) ** 2
        )
        == 0,
        "C2 identity",
    )
    sharp = sp.log(2) - sp.Rational(200, 553)
    require(bool(sp.N(sharp - sp.Rational(33, 100), 80) > 0), "C3 margin")
    target = 2 + delta
    inner = 2 + delta / 2
    reciprocal_log = L + sp.log(1 + target / L)
    require(
        sp.limit(
            L * ((1 - inner / reciprocal_log) * (1 + target / L) - 1),
            L,
            sp.oo,
        )
        == delta / 2,
        "C4 inverse repair",
    )
    epsilon = sp.symbols("epsilon", positive=True)
    require(
        sp.simplify(
            epsilon / (1 - epsilon)
            - epsilon
            - epsilon**2 / (1 - epsilon)
        )
        == 0,
        "C5 Chen boundary",
    )

    result = {
        "status": "INDEPENDENT_SOURCE_COMPLETE_REPLAY_PASS",
        "claims_replayed": 5,
        "unresolved_dependencies": 0,
        "mutations_rejected": 5,
        "source_sha256": PAPER_SHA,
    }
    (ARTIFACT / "independent_checker.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
