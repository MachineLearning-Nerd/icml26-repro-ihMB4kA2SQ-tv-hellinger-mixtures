"""Direct, fail-closed checks of the paper's C1--C3 substantive formulas.

This does not pretend that finitely many instances prove universal theorems.
It instantiates the exact Section 3 construction and evaluates both sides of
the exact inequalities, using two independently sized quadrature rules.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import platform
import resource
import subprocess
import time
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.special import roots_hermitenorm

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source" / "arxiv-2602.03202.tar"
SOURCE_SHA256 = "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d"
ARTIFACTS = ROOT / ".openresearch" / "artifacts" / "claim_1_3"


def double_factorial(value: int) -> int:
    if value <= 0:
        return 1
    result = 1
    for item in range(value, 0, -2):
        result *= item
    return result


def construction(order: int, dps: int) -> tuple[np.ndarray, np.ndarray, float]:
    """Return nodes, scaled weights u=w/s, and s from Lemma 3.2 (M=1)."""
    mp.mp.dps = dps
    nodes_mp = [
        mp.cos((2 * j + 1) * mp.pi / (2 * order + 2))
        for j in range(order + 1)
    ]
    vandermonde = mp.matrix(
        [[nodes_mp[j] ** k for j in range(order + 1)] for k in range(order + 1)]
    )
    scaled_moments = mp.matrix(
        [
            mp.mpf(1) / double_factorial(order - k) if k % 2 else mp.mpf(0)
            for k in range(order + 1)
        ]
    )
    scaled_weights = mp.lu_solve(vandermonde, scaled_moments)
    scale = float((mp.sqrt(2) - 1) ** (order + 1))
    nodes = np.array([float(value) for value in nodes_mp])
    u = np.array([float(value) for value in scaled_weights])
    return nodes, u, scale


def expectation_grid(
    nodes: np.ndarray, scaled_weights: np.ndarray, order: int
) -> tuple[np.ndarray, np.ndarray]:
    x, weights = roots_hermitenorm(order)
    exponent = np.exp(
        x[:, None] * nodes[None, :] - 0.5 * nodes[None, :] ** 2
    )
    signed = exponent @ scaled_weights
    probability_weights = weights / math.sqrt(2 * math.pi)
    return signed, probability_weights


def evaluate_one(
    n: int, quadrature_order: int, delta: float, dps: int
) -> dict[str, float | int | bool]:
    nodes, u, scale = construction(n, dps)
    signed, probability_weights = expectation_grid(nodes, u, quadrature_order)
    x, _ = roots_hermitenorm(quadrature_order)
    exponent = np.exp(
        x[:, None] * nodes[None, :] - 0.5 * nodes[None, :] ** 2
    )
    lambda_n = math.exp(-math.sqrt(8 * n + 4))
    base_ratio = (1 - lambda_n) + lambda_n * np.mean(exponent, axis=1)
    scaled_difference = lambda_n * scale * signed
    p2_ratio = base_ratio + 0.25 * scaled_difference
    if np.min(base_ratio) <= 0 or np.min(p2_ratio) <= 0:
        raise AssertionError("constructed density ratio is not positive")

    expected_abs = float(np.dot(probability_weights, np.abs(signed)))
    expected_chi_scaled = float(
        np.dot(probability_weights, signed**2 / base_ratio)
    )
    stable_hellinger_integrand = (
        signed
        / (np.sqrt(p2_ratio) + np.sqrt(base_ratio))
    ) ** 2
    expected_hellinger_scaled = float(
        np.dot(probability_weights, stable_hellinger_integrand)
    )

    tv1 = 0.5 * lambda_n * scale * expected_abs
    sqrt_chi1 = lambda_n * scale * math.sqrt(expected_chi_scaled)
    tv2 = 0.125 * lambda_n * scale * expected_abs
    hellinger2 = (
        0.25
        * lambda_n
        * scale
        * math.sqrt(0.5 * expected_hellinger_scaled)
    )
    alpha1 = (2 + delta) / math.log(max(math.log(1 / tv1), math.e))
    alpha2 = (2 + delta) / math.log(max(math.log(1 / tv2), math.e))
    alpha_star = 0.33 / math.log(math.log(1 / tv2))
    theorem1_term = tv1 ** (1 - alpha1)
    corollary2_term = tv2 ** (1 - alpha2)
    sharpness_term = tv2 ** (1 - alpha_star)

    weights = scale * u
    moment_residual = 0.0
    for k in range(n + 1):
        target = scale / double_factorial(n - k) if k % 2 else 0.0
        actual = float(np.dot(weights, nodes**k))
        moment_residual = max(moment_residual, abs(actual - target))
    chebyshev_residual = float(
        np.max(np.abs(np.cos((n + 1) * np.arccos(nodes))))
    )
    min_probability_weight = float(np.min(1 / (n + 1) + weights))
    return {
        "n": n,
        "quadrature_order": quadrature_order,
        "scale": scale,
        "lambda_n": lambda_n,
        "tv_pi1_eta1": tv1,
        "sqrt_chi2_pi1_eta1": sqrt_chi1,
        "theorem_2_1_exponent_term": theorem1_term,
        "theorem_2_1_ratio": sqrt_chi1 / theorem1_term,
        "tv_pi2_eta2": tv2,
        "hellinger_pi2_eta2": hellinger2,
        "corollary_2_4_exponent_term": corollary2_term,
        "corollary_2_4_ratio": hellinger2 / corollary2_term,
        "sharpness_exponent_term": sharpness_term,
        "sharpness_ratio": hellinger2 / sharpness_term,
        "sqrt_chi_over_tv_control": sqrt_chi1 / tv1,
        "hellinger_over_tv_control": hellinger2 / tv2,
        "wrong_sharpness_ratio": hellinger2
        / (tv2 ** (1 - 0.50 / math.log(math.log(1 / tv2)))),
        "chebyshev_residual": chebyshev_residual,
        "moment_residual": moment_residual,
        "min_probability_weight": min_probability_weight,
    }


def close_enough(primary: float, independent: float, relative: float = 8e-3) -> bool:
    return abs(primary - independent) <= relative * max(
        abs(primary), abs(independent), 1e-300
    )


def write_contracts() -> None:
    contracts = {
        "source_sha256": SOURCE_SHA256,
        "source_retrieved_utc": "2026-07-25T04:48:56Z",
        "source_url": "https://export.arxiv.org/e-print/2602.03202",
        "claims": {
            "C1": {
                "anchor": "Theorem 2.1 / theorem:uniformTV",
                "quantifiers": "all d,M,delta>0 and all probability measures pi,eta supported on [-M,M]^d; exists C0(delta,M,d), independent of pi,eta",
                "tested_expression": "sqrt(chi2(f_pi||f_eta)) <= TV^(1-alpha(TV)) (a stronger finite-instance check than the theorem's max(C0,TV^-alpha)*TV)",
                "alpha": "(2+delta)/log(max(log(1/t),e))",
            },
            "C2": {
                "anchor": "Corollary 2.4 / corollary:uniformTV",
                "quantifiers": "same support and delta quantifiers as C1",
                "tested_expression": "H(f_pi,f_eta) <= TV^(1-alpha(TV))",
            },
            "C3": {
                "anchor": "Theorem 3.1 and Lemma 3.2",
                "quantifiers": "there exist sequences supported on [-M,M], relabelled after an unspecified universal N0",
                "tested_expression": "H_n >= TV_n^(1-0.33/log(log(1/TV_n))) on directly constructed finite orders",
            },
        },
        "scope": "Direct finite construction; not by itself a proof of universal or asymptotic quantifiers.",
    }
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS / "claim_contract.json").write_text(
        json.dumps(contracts, indent=2) + "\n"
    )


def main() -> None:
    started = time.perf_counter()
    config = json.loads((ROOT / "repro" / "config.json").read_text())
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise AssertionError("primary-source hash mismatch")
    write_contracts()
    rows: list[dict[str, float | int | bool]] = []
    independent_rows: list[dict[str, float | int | bool]] = []
    for n in config["odd_orders"]:
        rows.append(
            evaluate_one(
                n,
                config["gauss_hermite_order"],
                config["delta"],
                config["mp_dps"],
            )
        )
        independent_rows.append(
            evaluate_one(
                n,
                config["independent_order"],
                config["delta"],
                config["mp_dps"] + 20,
            )
        )

    for primary, independent in zip(rows, independent_rows):
        for key in (
            "tv_pi1_eta1",
            "sqrt_chi2_pi1_eta1",
            "tv_pi2_eta2",
            "hellinger_pi2_eta2",
        ):
            primary_value = float(primary[key])
            independent_value = float(independent[key])
            relative_disagreement = abs(primary_value - independent_value) / max(
                abs(primary_value), abs(independent_value), 1e-300
            )
            print(
                "CONVERGENCE",
                json.dumps(
                    {
                        "n": primary["n"],
                        "quantity": key,
                        "primary": primary_value,
                        "doubled_order": independent_value,
                        "relative_disagreement": relative_disagreement,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if not close_enough(primary_value, independent_value):
                raise AssertionError(
                    "resolution checker disagrees: "
                    f"n={primary['n']} quantity={key} "
                    f"primary={primary_value:.17g} "
                    f"doubled_order={independent_value:.17g} "
                    f"relative_disagreement={relative_disagreement:.6g}"
                )
        if primary["chebyshev_residual"] >= 2e-13:
            raise AssertionError("Chebyshev node identity failed")
        if primary["moment_residual"] >= 2e-12:
            raise AssertionError("moment system failed")
        if primary["min_probability_weight"] < -2e-14:
            raise AssertionError("invalid mixing probability")
        if primary["theorem_2_1_ratio"] > 1.0 + 1e-10:
            raise AssertionError("exact Theorem 2.1 exponent term failed")
        if primary["corollary_2_4_ratio"] > 1.0 + 1e-10:
            raise AssertionError("exact Corollary 2.4 exponent term failed")

    sharp_rows = [row for row in rows if float(row["sharpness_ratio"]) >= 1]
    if len(sharp_rows) < 2:
        raise AssertionError("sharpness inequality not observed on at least two constructed orders")

    controls = {
        "C1_alpha_zero_rejected": max(
            float(row["sqrt_chi_over_tv_control"]) for row in rows
        )
        > 1.05,
        "C2_alpha_zero_rejected": max(
            float(row["hellinger_over_tv_control"]) for row in rows
        )
        > 1.05,
        "C3_too_large_0_50_coefficient_rejected": min(
            float(row["wrong_sharpness_ratio"]) for row in sharp_rows
        )
        < 1.0,
    }
    if not all(controls.values()):
        raise AssertionError(f"negative control did not fail as intended: {controls}")

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    with (ARTIFACTS / "raw_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    checker = {
        "engine": "independent doubled-order Gauss-Hermite with +20 mpmath digits",
        "all_close": True,
        "rows": independent_rows,
    }
    (ARTIFACTS / "independent_checker.json").write_text(
        json.dumps(checker, indent=2) + "\n"
    )
    (ARTIFACTS / "negative_control.json").write_text(
        json.dumps(controls, indent=2) + "\n"
    )
    runtime = time.perf_counter() - started
    result = {
        "claim_scope": "finite direct corroboration of exact formulas; universal proof certificate pending",
        "source_sha256": SOURCE_SHA256,
        "git_sha": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "seed": config["seed"],
        "primary_engine": config["primary_engine"],
        "cpu_estimate": "1 effective core",
        "actual_logical_cpus_visible": os.cpu_count(),
        "platform": platform.platform(),
        "runtime_seconds": runtime,
        "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "sharpness_orders_passing": [int(row["n"]) for row in sharp_rows],
        "controls": controls,
        "rows": rows,
    }
    (ARTIFACTS / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print("=== EXACT CLAIM 1-3 RESULT ===")
    print(json.dumps(result, indent=2))
    print("=== INDEPENDENT CHECKER ===")
    print(json.dumps(checker, indent=2))
    print("=== NEGATIVE CONTROLS ===")
    print(json.dumps(controls, indent=2))


if __name__ == "__main__":
    main()
