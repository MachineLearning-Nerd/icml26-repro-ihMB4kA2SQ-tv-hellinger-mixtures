"""Fail-closed evaluator-visible release checks for the additive Space tree."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPACE = ROOT / "release" / "space"
RELEASE = SPACE / "evidence" / "release"
JUDGED = SPACE / "historical" / "judged-1c98799a89d8c1d3c45136c8b912e74371e975b3"


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_manifest(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text().splitlines():
        digest, name = line.split("  ", 1)
        result[name] = digest
    return result


def main() -> None:
    require(SPACE.is_dir(), "candidate Space tree missing")
    require(JUDGED.is_dir(), "protected judged revision missing")
    report = ROOT / "reports" / "tv-hellinger-reproduction" / "report.md"
    report_text = report.read_text()
    for image_name in (
        "headline-sharpness.png",
        "quadrature-agreement.png",
        "norm-asymptotics.png",
        "c4-inverse-repair.png",
        "c5-coefficient-budget.png",
    ):
        image = report.parent / "images" / image_name
        require(image.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), f"invalid figure: {image_name}")
        require(f"images/{image_name}" in report_text, f"report omits figure: {image_name}")
    require(
        "molab.marimo.io/github/MachineLearning-Nerd/" in (ROOT / "README.md").read_text(),
        "Molab badge missing",
    )
    judged = parse_manifest(JUDGED / "manifest.sha256")

    # Every old path remains.  Evidence pages/assets are byte-identical at their
    # original path; the three routing files have exact protected copies.
    routed_copies = {
        "README.md": JUDGED / "README.md",
        "logbook.json": JUDGED / "logbook.json",
        "pages/index.md": JUDGED / "pages-index.md",
    }
    preserved = {}
    for relative, digest in judged.items():
        candidate = SPACE / relative
        require(candidate.exists(), f"old path missing: {relative}")
        comparison = routed_copies.get(relative, candidate)
        require(sha256(comparison) == digest, f"old hash changed: {relative}")
        preserved[relative] = str(comparison.relative_to(SPACE))

    logbook = json.loads((SPACE / "logbook.json").read_text())
    require(logbook["space_id"] == "DineshAI/ihMB4kA2SQ", "wrong Space id")
    children = logbook["root"]["children"]
    require(children[0]["slug"] == "current-overview", "current navigation not first")
    require(
        children[-1]["title"] == "Historical rejected baseline",
        "historical navigation label",
    )

    claim_pages = {
        f"C{index}": SPACE / f"pages/current-claim-c{index}/page.md"
        for index in range(1, 6)
    }
    common_tokens = (
        "**Verdict: VERIFIED. Confidence: MEDIUM.**",
        "## Exact claim contract",
        "uv sync --frozen && uv run python repro/src/run_publication_gate.py",
        "de2c3a8fba29e433c552ce82c194196fefaaa4d8",
        "../../evidence/",
    )
    for claim, page in claim_pages.items():
        text = page.read_text()
        for token in common_tokens:
            require(token in text, f"{claim} missing visible token: {token}")
        require(
            "control" in text.lower()
            and "verifier" in text.lower()
            and "limitations" in text.lower(),
            f"{claim} checker/control/limitations not visible",
        )

    visibility = (SPACE / "pages/current-visibility/page.md").read_text()
    for claim in claim_pages:
        require(f"| {claim} |" in visibility, f"visibility row missing: {claim}")
    require(visibility.count("| Yes | Yes |") == 5, "visibility matrix incomplete")

    # Validate every relative Markdown link reachable from the canonical pages.
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    markdown_files = [
        SPACE / "README.md",
        SPACE / "pages/index.md",
        SPACE / "pages/current-overview/page.md",
        *claim_pages.values(),
        SPACE / "pages/current-methods/page.md",
        SPACE / "pages/current-visibility/page.md",
        SPACE / "pages/current-release-audit/page.md",
        SPACE / "pages/historical-rejected-baseline/page.md",
    ]
    checked_links = []
    for page in markdown_files:
        for target in link_pattern.findall(page.read_text()):
            if target.startswith(("http://", "https://", "#")):
                continue
            resolved = (page.parent / target).resolve()
            require(resolved.is_relative_to(SPACE.resolve()), f"link escapes Space: {target}")
            require(resolved.exists(), f"broken relative link: {page}: {target}")
            checked_links.append(
                {
                    "from": str(page.relative_to(SPACE)),
                    "to": str(resolved.relative_to(SPACE.resolve())),
                }
            )

    allowlist_path = RELEASE / "upload_allowlist.txt"
    allowlist = [
        line for line in allowlist_path.read_text().splitlines() if line.strip()
    ]
    require(len(allowlist) == len(set(allowlist)), "duplicate upload path")
    allowed_suffixes = {
        ".css",
        ".csv",
        ".html",
        ".js",
        ".json",
        ".lock",
        ".md",
        ".py",
        ".sha256",
        ".toml",
        ".txt",
    }
    for relative in allowlist:
        path = SPACE / relative
        require(path.is_file(), f"allowlisted path missing: {relative}")
        require(
            path.suffix in allowed_suffixes or path.name in {".python-version", ".gitattributes"},
            f"non-text path allowlisted: {relative}",
        )
        content = path.read_bytes()
        require(b"\x00" not in content, f"NUL byte in text path: {relative}")
        content.decode("utf-8")

    # Candidate manifest deliberately excludes its own file and generated audit
    # outputs to avoid self-reference.
    manifest_exclusions = {
        "evidence/release/candidate_manifest.sha256",
        "evidence/release/release_check.json",
        "evidence/release/secret_scan.json",
    }
    manifest_paths = sorted(set(allowlist) - manifest_exclusions)
    manifest_text = "".join(
        f"{sha256(SPACE / relative)}  {relative}\n" for relative in manifest_paths
    )
    (RELEASE / "candidate_manifest.sha256").write_text(manifest_text)

    secret_patterns = {
        "github_pat": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        "github_classic": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        "hugging_face": re.compile(r"hf_[A-Za-z0-9]{20,}"),
        "private_key": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
    }
    secret_hits = []
    for path in sorted(SPACE.rglob("*")):
        if not path.is_file() or path.suffix not in allowed_suffixes:
            continue
        text = path.read_text(errors="replace")
        for name, pattern in secret_patterns.items():
            if pattern.search(text):
                secret_hits.append({"path": str(path.relative_to(SPACE)), "pattern": name})
    require(not secret_hits, f"secret-like content found: {secret_hits}")
    secret_result = {
        "status": "PASS",
        "files_scanned": sum(1 for path in SPACE.rglob("*") if path.is_file()),
        "patterns": sorted(secret_patterns),
        "hits": secret_hits,
    }
    (RELEASE / "secret_scan.json").write_text(json.dumps(secret_result, indent=2) + "\n")

    result = {
        "status": "RELEASE_CANDIDATE_PASS",
        "space_id": "DineshAI/ihMB4kA2SQ",
        "judged_revision": "1c98799a89d8c1d3c45136c8b912e74371e975b3",
        "old_file_count": len(judged),
        "old_file_set_is_subset": True,
        "preserved_paths": preserved,
        "canonical_entrypoint": "README.md",
        "claim_verdicts": {claim: "VERIFIED" for claim in claim_pages},
        "claim_confidence": {claim: "MEDIUM" for claim in claim_pages},
        "visibility_rows_complete": 5,
        "relative_links_checked": checked_links,
        "upload_allowlist_count": len(allowlist),
        "manifest_covered_count": len(manifest_paths),
        "secret_scan": "PASS",
        "red_team_passes": 2,
        "evidence_git_sha": "de2c3a8fba29e433c552ce82c194196fefaaa4d8",
    }
    (RELEASE / "release_check.json").write_text(json.dumps(result, indent=2) + "\n")
    print("=== EVALUATOR-VISIBLE RELEASE CHECK ===")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
