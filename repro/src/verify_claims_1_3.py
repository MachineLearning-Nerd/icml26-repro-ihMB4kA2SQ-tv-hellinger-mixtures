"""Direct, fail-closed checks of the paper's C1--C3 substantive formulas.

This does not pretend that finitely many instances prove universal theorems.
It instantiates the exact Section 3 construction and evaluates both sides of
the exact inequalities. The primary engine is adaptive Gauss--Kronrod
quadrature split at independently located sign changes; a fixed-node
Gauss--Hermite calculation is the checker.
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
from scipy.integrate import quad
from scipy.optimize import brentq
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


def construction(
    order: int, dps: int
) -> tuple[np.ndarray, np.ndarray, float, list[mp.mpf], list[mp.mpf]]:
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
    return nodes, u, scale, nodes_mp, list(scaled_weights)


def signed_value(
    x_value: float, nodes_mp: list[mp.mpf], weights_mp: list[mp.mpf]
) -> float:
    x_mp = mp.mpf(x_value)
    return float(
        mp.fsum(
            weight * mp.exp(x_mp * node - node**2 / 2)
            for node, weight in zip(nodes_mp, weights_mp)
        )
    )


def find_sign_changes(
    nodes_mp: list[mp.mpf], weights_mp: list[mp.mpf], extent: float = 14.0
) -> list[float]:
    grid = np.linspace(-extent, extent, 2801)
    values = [signed_value(float(x), nodes_mp, weights_mp) for x in grid]
    roots: list[float] = []
    for left, right, f_left, f_right in zip(
        grid[:-1], grid[1:], values[:-1], values[1:]
    ):
        if f_left == 0:
            roots.append(float(left))
        elif f_left * f_right < 0:
            roots.append(
                brentq(
                    lambda value: signed_value(value, nodes_mp, weights_mp),
                    float(left),
                    float(right),
                    xtol=1e-13,
                )
            )
    return sorted(set(round(root, 12) for root in roots))


def expectation_grid(
    nodes_mp: list[mp.mpf], scaled_weights_mp: list[mp.mpf], order: int
) -> tuple[np.ndarray, np.ndarray]:
    x, weights = roots_hermitenorm(order)
    signed = np.array(
        [
            signed_value(float(x_value), nodes_mp, scaled_weights_mp)
            for x_value in x
        ]
    )
    probability_weights = weights / math.sqrt(2 * math.pi)
    return signed, probability_weights


def finish_row(
    n: int,
    engine: str,
    delta: float,
    nodes: np.ndarray,
    u: np.ndarray,
    scale: float,
    expected_abs: float,
    expected_chi_scaled: float,
    expected_hellinger_scaled: float,
    root_count: int,
    integration_error: float,
) -> dict[str, float | int | str]:
    lambda_n = math.exp(-math.sqrt(8 * n + 4))
    tv1 = 0.5 * lambda_n * scale * expected_abs
    sqrt_chi1 = lambda_n * scale * math.sqrt(expected_chi_scaled)
    tv2 = 0.125 * lambda_n * scale * expected_abs
    hellinger2 = (
        0.25 * lambda_n * scale * math.sqrt(0.5 * expected_hellinger_scaled)
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
    return {
        "n": n,
        "engine": engine,
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
        "chebyshev_residual": float(
            np.max(np.abs(np.cos((n + 1) * np.arccos(nodes))))
        ),
        "moment_residual": moment_residual,
        "min_probability_weight": float(np.min(1 / (n + 1) + weights)),
        "root_count": root_count,
        "reported_integration_error": integration_error,
    }


def evaluate_adaptive(
    n: int, delta: float, dps: int
) -> dict[str, float | int | str]:
    nodes, u, scale, nodes_mp, u_mp = construction(n, dps)
    lambda_n = math.exp(-math.sqrt(8 * n + 4))
    roots = find_sign_changes(nodes_mp, u_mp)

    def components(x_value: float) -> tuple[float, float, float]:
        signed = signed_value(x_value, nodes_mp, u_mp)
        exponent_mean = math.fsum(
            math.exp(x_value * float(node) - 0.5 * float(node) ** 2)
            for node in nodes_mp
        ) / len(nodes_mp)
        base = (1 - lambda_n) + lambda_n * exponent_mean
        p2 = base + 0.25 * lambda_n * scale * signed
        if base <= 0 or p2 <= 0:
            raise AssertionError("constructed density ratio is not positive")
        normal = math.exp(-0.5 * x_value**2) / math.sqrt(2 * math.pi)
        return signed, base, normal

    intervals = [-math.inf, *roots, math.inf]
    abs_total = 0.0
    abs_error = 0.0

    def absolute_integrand(x_value: float) -> float:
        signed, _, normal = components(x_value)
        return normal * abs(signed)

    for left, right in zip(intervals[:-1], intervals[1:]):
        value, error = quad(
            absolute_integrand,
            left,
            right,
            epsabs=1e-48,
            epsrel=2e-10,
            limit=300,
        )
        abs_total += value
        abs_error += error

    def chi_integrand(x_value: float) -> float:
        signed, base, normal = components(x_value)
        return normal * signed**2 / base

    chi_total, chi_error = quad(
        chi_integrand,
        -math.inf,
        math.inf,
        epsabs=1e-70,
        epsrel=2e-10,
        limit=300,
    )

    def hellinger_integrand(x_value: float) -> float:
        signed, base, normal = components(x_value)
        p2 = base + 0.25 * lambda_n * scale * signed
        return normal * (
            signed / (math.sqrt(p2) + math.sqrt(base))
        ) ** 2

    hellinger_total, hellinger_error = quad(
        hellinger_integrand,
        -math.inf,
        math.inf,
        epsabs=1e-70,
        epsrel=2e-10,
        limit=300,
    )
    return finish_row(
        n,
        "adaptive_gauss_kronrod",
        delta,
        nodes,
        u,
        scale,
        abs_total,
        chi_total,
        hellinger_total,
        len(roots),
        abs_error + chi_error + hellinger_error,
    )


def evaluate_gauss_hermite(
    n: int, quadrature_order: int, delta: float, dps: int
) -> dict[str, float | int | str]:
    nodes, u, scale, nodes_mp, u_mp = construction(n, dps)
    signed, probability_weights = expectation_grid(nodes_mp, u_mp, quadrature_order)
    x, _ = roots_hermitenorm(quadrature_order)
    exponent = np.exp(x[:, None] * nodes[None, :] - 0.5 * nodes[None, :] ** 2)
    lambda_n = math.exp(-math.sqrt(8 * n + 4))
    base = (1 - lambda_n) + lambda_n * np.mean(exponent, axis=1)
    p2 = base + 0.25 * lambda_n * scale * signed
    return finish_row(
        n,
        f"gauss_hermite_{quadrature_order}",
        delta,
        nodes,
        u,
        scale,
        float(np.dot(probability_weights, np.abs(signed))),
        float(np.dot(probability_weights, signed**2 / base)),
        float(
            np.dot(
                probability_weights,
                (signed / (np.sqrt(p2) + np.sqrt(base))) ** 2,
            )
        ),
        -1,
        0.0,
    )


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
    rows: list[dict[str, float | int | str]] = []
    independent_rows: list[dict[str, float | int | str]] = []
    for n in config["odd_orders"]:
        primary = evaluate_adaptive(n, config["delta"], config["mp_dps"])
        checker_row = evaluate_gauss_hermite(
            n,
            config["independent_order"],
            config["delta"],
            config["mp_dps"] + 20,
        )
        rows.append(primary)
        independent_rows.append(checker_row)
        print(
            "ADAPTIVE_ROW",
            json.dumps(
                {
                    "n": n,
                    "root_count": primary["root_count"],
                    "tv": primary["tv_pi1_eta1"],
                    "sqrt_chi2": primary["sqrt_chi2_pi1_eta1"],
                    "hellinger": primary["hellinger_pi2_eta2"],
                    "integration_error": primary["reported_integration_error"],
                },
                sort_keys=True,
            ),
            flush=True,
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
            disagreement = abs(primary_value - independent_value) / max(
                abs(primary_value), abs(independent_value), 1e-300
            )
            print(
                "CROSS_ENGINE",
                json.dumps(
                    {
                        "n": primary["n"],
                        "quantity": key,
                        "adaptive": primary_value,
                        "gauss_hermite": independent_value,
                        "relative_disagreement": disagreement,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if not close_enough(primary_value, independent_value):
                raise AssertionError(
                    "independent cross-engine checker disagrees: "
                    f"n={primary['n']} quantity={key} "
                    f"relative_disagreement={disagreement:.6g}"
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
        "engine": "independent fixed-node Gauss-Hermite with +20 mpmath digits",
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
