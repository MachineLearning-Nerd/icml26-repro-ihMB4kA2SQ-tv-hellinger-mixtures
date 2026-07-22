from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class CertificateTests(unittest.TestCase):
    def test_verifier_has_all_five_claims(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "certificate.json"
            subprocess.run(
                [sys.executable, "repro/src/verify_tv_hellinger.py", "--output", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            result = json.loads(output.read_text())
        self.assertEqual(result["verified_claims"], 5)
        self.assertEqual(result["falsified_claims"], 0)
        self.assertEqual(set(result["claims"]), {"C1", "C2", "C3", "C4", "C5"})

    def test_negative_controls_fail_closed(self) -> None:
        subprocess.run(
            [sys.executable, "repro/src/verify_tv_hellinger.py", "--output", "outputs/test_certificate.json"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads((ROOT / "outputs/test_certificate.json").read_text())
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertGreater(result["claims"]["C1"]["max_chi"], 0)


if __name__ == "__main__":
    unittest.main()
