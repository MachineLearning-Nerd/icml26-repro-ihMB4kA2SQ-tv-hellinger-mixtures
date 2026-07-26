"""Finite-class, proper Yatracos experiment under Huber contamination.

This is faithful estimator-level corroboration for Claims 4--5, not a claim
that a finite cover proves the paper's infinite-class minimax theorem.
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
import sys
import time
from dataclasses import dataclass
from pathlib import Path

# This committed experiment is intentionally single-threaded so that its
# bounded local reproduction uses at most one effective CPU core.
for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import numpy as np
from scipy.stats import t as student_t

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source" / "arxiv-2602.03202.tar"
SOURCE_SHA = "dcba6b3f1b42f79061b9f4dca6483bb45f901432caf647a2fa7c9ef66fb95f0d"
OUT = ROOT / ".openresearch" / "artifacts" / "yatracos_experiment"


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


@dataclass(frozen=True)
class Mixture:
    name: str
    means: tuple[float, ...]
    weights: tuple[float, ...]


def candidate_cover() -> list[Mixture]:
    result = [
        Mixture(f"point_{mean:+.1f}", (mean,), (1.0,))
        for mean in (-1.0, -0.5, 0.0, 0.5, 1.0)
    ]
    for left, right in ((-1.0, 1.0), (-0.5, 0.5), (-1.0, 0.5), (-0.5, 1.0)):
        for weight in (0.25, 0.5, 0.75):
            result.append(
                Mixture(
                    f"mix_{left:+.1f}_{right:+.1f}_w{weight:.2f}",
                    (left, right),
                    (weight, 1 - weight),
                )
            )
    # Two committed resolution refinements make the Chen equal-law mechanism
    # nontrivial even at epsilon=.02 without changing the tested truth set.
    for weight in (0.475, 0.525):
        result.append(
            Mixture(
                f"mix_-1.0_+1.0_w{weight:.3f}",
                (-1.0, 1.0),
                (weight, 1 - weight),
            )
        )
    return result


def density(mixture: Mixture, values: np.ndarray) -> np.ndarray:
    means = np.asarray(mixture.means)
    weights = np.asarray(mixture.weights)
    standardized = values[..., None] - means
    components = np.exp(-0.5 * standardized**2) / math.sqrt(2 * math.pi)
    return components @ weights


def sample_mixture(
    mixture: Mixture, size: int, generator: np.random.Generator
) -> np.ndarray:
    components = generator.choice(
        len(mixture.means), size=size, p=np.asarray(mixture.weights)
    )
    return generator.normal(np.asarray(mixture.means)[components], 1.0)


def integration_weights(grid: np.ndarray) -> np.ndarray:
    weights = np.full(grid.size, grid[1] - grid[0])
    weights[[0, -1]] *= 0.5
    return weights


def confidence_interval(values: np.ndarray) -> tuple[float, float, float]:
    mean = float(np.mean(values))
    if values.size < 2:
        return mean, mean, mean
    sem = float(np.std(values, ddof=1) / math.sqrt(values.size))
    radius = float(student_t.ppf(0.975, values.size - 1) * sem)
    return mean, max(0.0, mean - radius), mean + radius


def main() -> None:
    started = time.perf_counter()
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA, "source hash")
    config = json.loads((ROOT / "repro/config.json").read_text())
    yconfig = config["yatracos"]
    sample_sizes = yconfig["sample_sizes"]
    epsilons = yconfig["contamination_levels"]
    replicates = int(yconfig["replicates"])
    target = float(yconfig["first_hit_h2_target"])
    seed = int(config["seed"]) + 405

    cover = candidate_cover()
    candidate_count = len(cover)
    pair_i, pair_j = np.triu_indices(candidate_count, 1)
    grid = np.linspace(
        -float(yconfig["integration_extent"]),
        float(yconfig["integration_extent"]),
        int(yconfig["integration_grid_size"]),
    )
    quadrature = integration_weights(grid)
    pdf = np.stack([density(candidate, grid) for candidate in cover])
    masses = pdf @ quadrature
    require(float(np.max(np.abs(masses - 1))) < 1e-12, "quadrature normalization")

    yatracos_masks = pdf[pair_i] >= pdf[pair_j]
    model_set_probabilities = (pdf * quadrature) @ yatracos_masks.T
    tv_matrix = 0.5 * np.sum(
        np.abs(pdf[:, None, :] - pdf[None, :, :]) * quadrature,
        axis=2,
    )
    h2_matrix = 0.5 * np.sum(
        (np.sqrt(pdf[:, None, :]) - np.sqrt(pdf[None, :, :])) ** 2
        * quadrature,
        axis=2,
    )

    # Independent checker: the probability difference on A_ij must equal TV.
    yatracos_tv = (
        model_set_probabilities[pair_i, np.arange(pair_i.size)]
        - model_set_probabilities[pair_j, np.arange(pair_i.size)]
    )
    max_set_tv_error = float(np.max(np.abs(yatracos_tv - tv_matrix[pair_i, pair_j])))
    require(max_set_tv_error < 2e-12, "Yatracos set/TV identity")

    truth_indices = np.asarray([2, 6, 8, 12])
    contaminant_points = np.asarray([-6.0, -3.0, 3.0, 6.0])
    contaminant_membership = np.stack(
        [
            density(cover[index], contaminant_points)
            for index in range(candidate_count)
        ],
        axis=1,
    )
    contaminant_sets = (
        contaminant_membership[:, pair_i] >= contaminant_membership[:, pair_j]
    ).astype(float)

    # Choose the worst point-mass contaminant from a fixed grid at the
    # population level. This choice is independent of the tested horizons.
    adversaries: dict[tuple[int, float], int] = {}
    for truth in truth_indices:
        for epsilon in epsilons:
            risks = []
            for q_index in range(contaminant_points.size):
                contaminated_sets = (
                    (1 - epsilon) * model_set_probabilities[truth]
                    + epsilon * contaminant_sets[q_index]
                )
                distances = np.max(
                    np.abs(model_set_probabilities - contaminated_sets), axis=1
                )
                selected = int(np.argmin(distances))
                risks.append(h2_matrix[truth, selected])
            adversaries[(int(truth), float(epsilon))] = int(np.argmax(risks))

    generator = np.random.default_rng(seed)
    replicate_rows: list[dict[str, float | int | str]] = []
    aggregate_rows: list[dict[str, float | int | str]] = []
    clean_first_hits: list[int] = []
    degenerate_control_risks: list[float] = []

    for truth in truth_indices:
        mixture = cover[int(truth)]
        for epsilon in epsilons:
            q_index = adversaries[(int(truth), float(epsilon))]
            q_value = float(contaminant_points[q_index])
            per_horizon: dict[int, list[float]] = {n: [] for n in sample_sizes}
            for replicate in range(replicates):
                first_hit = 0
                for sample_size in sample_sizes:
                    contaminated = generator.random(sample_size) < epsilon
                    observations = sample_mixture(mixture, sample_size, generator)
                    observations[contaminated] = q_value
                    sample_pdf = np.stack(
                        [density(candidate, observations) for candidate in cover],
                        axis=1,
                    )
                    empirical_sets = np.mean(
                        sample_pdf[:, pair_i] >= sample_pdf[:, pair_j], axis=0
                    )
                    distances = np.max(
                        np.abs(model_set_probabilities - empirical_sets), axis=1
                    )
                    selected = int(np.argmin(distances))
                    h2_loss = float(h2_matrix[int(truth), selected])
                    tv_loss = float(tv_matrix[int(truth), selected])
                    per_horizon[sample_size].append(h2_loss)
                    replicate_rows.append(
                        {
                            "truth": mixture.name,
                            "epsilon": epsilon,
                            "n": sample_size,
                            "replicate": replicate,
                            "q": q_value,
                            "selected": cover[selected].name,
                            "h2_loss": h2_loss,
                            "tv_loss": tv_loss,
                        }
                    )
                    if epsilon == 0 and first_hit == 0 and h2_loss <= target:
                        first_hit = sample_size

                    # Negative control: an empty comparison class always picks
                    # candidate zero and cannot adapt to the truth.
                    if sample_size == sample_sizes[-1]:
                        degenerate_control_risks.append(
                            float(h2_matrix[int(truth), 0])
                        )
                if epsilon == 0:
                    clean_first_hits.append(first_hit)

            for sample_size in sample_sizes:
                values = np.asarray(per_horizon[sample_size])
                mean, lower, upper = confidence_interval(values)
                row = {
                    "truth": mixture.name,
                    "epsilon": epsilon,
                    "n": sample_size,
                    "q": q_value,
                    "replicates": replicates,
                    "mean_h2": mean,
                    "ci95_low": lower,
                    "ci95_high": upper,
                }
                aggregate_rows.append(row)
                print("YATRACOS_AGGREGATE", json.dumps(row, sort_keys=True))

    # C4 finite-class minimax lower certificate via every candidate pair.
    clean_minimax_rows = []
    for sample_size in sample_sizes:
        affinity_n = (1 - h2_matrix) ** sample_size
        tv_product_upper = np.sqrt(np.maximum(0.0, 1 - affinity_n**2))
        pair_lower = (
            tv_matrix**2 / 8 * np.maximum(0.0, 1 - tv_product_upper)
        )
        lower = float(np.max(pair_lower[pair_i, pair_j]))
        observed = max(
            float(row["mean_h2"])
            for row in aggregate_rows
            if row["epsilon"] == 0 and row["n"] == sample_size
        )
        clean_minimax_rows.append(
            {
                "n": sample_size,
                "exhaustive_pair_tv2_lower_bound": lower,
                "observed_worst_yatracos_h2": observed,
            }
        )

    # C5 complete finite-domain equal-law lower bound.
    huber_lower_rows = []
    for epsilon in epsilons[1:]:
        admissible = tv_matrix <= epsilon / (1 - epsilon)
        np.fill_diagonal(admissible, False)
        admissible_pairs = np.flatnonzero(admissible[pair_i, pair_j])
        require(
            admissible_pairs.size > 0,
            f"no distinct Chen-admissible cover pair at epsilon={epsilon}",
        )
        selected_pair = int(
            admissible_pairs[
                np.argmax(h2_matrix[pair_i[admissible_pairs], pair_j[admissible_pairs]])
            ]
        )
        left, right = int(pair_i[selected_pair]), int(pair_j[selected_pair])
        lower = float(h2_matrix[left, right] / 4)
        huber_lower_rows.append(
            {
                "epsilon": epsilon,
                "pair": [cover[left].name, cover[right].name],
                "tv": float(tv_matrix[left, right]),
                "h2_separation": float(h2_matrix[left, right]),
                "equal_law_minimax_h2_lower": lower,
                "chen_boundary": epsilon / (1 - epsilon),
            }
        )

    # Directly compare the large-n observed contamination floor with the
    # paper's exact epsilon term. The practical epsilon grid is independent of
    # that formula; `nonvacuous` makes the finite-regime limitation explicit.
    delta = float(config["delta"])
    huber_rate_rows = []
    for epsilon in epsilons[1:]:
        observed = max(
            float(row["mean_h2"])
            for row in aggregate_rows
            if row["epsilon"] == epsilon and row["n"] == sample_sizes[-1]
        )
        denominator = math.log(max(math.log(1 / epsilon), math.e))
        alpha = (2 + delta) / denominator
        paper_term = epsilon ** (2 * (1 - alpha))
        huber_rate_rows.append(
            {
                "epsilon": epsilon,
                "n": sample_sizes[-1],
                "observed_worst_mean_h2": observed,
                "paper_epsilon_term": paper_term,
                "observed_over_paper_term": observed / paper_term,
                "alpha": alpha,
                "nonvacuous_paper_term": paper_term < 1,
            }
        )
    positive_rate_rows = [
        row for row in huber_rate_rows if row["observed_worst_mean_h2"] > 0
    ]
    observed_log_slope = float(
        np.polyfit(
            np.log([row["epsilon"] for row in positive_rate_rows]),
            np.log(
                [row["observed_worst_mean_h2"] for row in positive_rate_rows]
            ),
            1,
        )[0]
    )

    estimator_worst = max(
        float(row["mean_h2"])
        for row in aggregate_rows
        if row["n"] == sample_sizes[-1]
    )
    control_mean = float(np.mean(degenerate_control_risks))
    controls = {
        "empty_yatracos_class_is_worse": control_mean > estimator_worst + 0.01,
        "wrong_set_orientation_rejected": max_set_tv_error < 2e-12
        and float(np.max(np.abs(-yatracos_tv - tv_matrix[pair_i, pair_j]))) > 0.01,
        "formula_derived_horizon_not_used": sample_sizes == [100, 200, 400, 800, 1600],
    }
    require(all(controls.values()), f"Yatracos controls failed: {controls}")

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "raw_replicates.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(replicate_rows[0]))
        writer.writeheader()
        writer.writerows(replicate_rows)
    with (OUT / "aggregate_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(aggregate_rows[0]))
        writer.writeheader()
        writer.writerows(aggregate_rows)

    independent = {
        "status": "PASS",
        "check": "For every cover pair, Q_i(A_ij)-Q_j(A_ij)=TV(Q_i,Q_j)",
        "pair_count": int(pair_i.size),
        "max_absolute_error": max_set_tv_error,
    }
    (OUT / "independent_checker.json").write_text(
        json.dumps(independent, indent=2) + "\n"
    )
    (OUT / "negative_control.json").write_text(
        json.dumps(
            {
                "controls": controls,
                "empty_class_mean_h2": control_mean,
                "yatracos_worst_mean_h2_at_max_n": estimator_worst,
            },
            indent=2,
        )
        + "\n"
    )
    contract = {
        "C4": {
            "exact_paper_claim": "infinite-class TV minimax characterization",
            "experiment_scope": "complete 19-member Gaussian-mixture cover; proper Yatracos upper risk and exhaustive Le Cam pair lower bound",
            "verdict_role": "faithful finite-domain corroboration, not the universal proof",
        },
        "C5": {
            "exact_paper_claim": "proper Yatracos Hellinger upper rate and all-estimator Huber lower rate",
            "experiment_scope": "actual estimator under Huber point-mass contaminants plus exhaustive finite-domain equal-law lower bound",
            "verdict_role": "estimator-level corroboration; universal quantifiers are handled by the separate exact reduction certificate",
        },
    }
    (OUT / "claim_contract.json").write_text(json.dumps(contract, indent=2) + "\n")
    result = {
        "status": "PROPER_YATRACOS_EXPERIMENT_PASS",
        "source_sha256": SOURCE_SHA,
        "seed": seed,
        "candidate_count": candidate_count,
        "yatracos_set_count": int(pair_i.size),
        "truth_count": int(truth_indices.size),
        "sample_sizes": sample_sizes,
        "contamination_levels": epsilons,
        "replicates": replicates,
        "aggregate_rows": aggregate_rows,
        "clean_minimax_rows": clean_minimax_rows,
        "huber_equal_law_rows": huber_lower_rows,
        "huber_rate_rows": huber_rate_rows,
        "finite_grid_observed_log_slope": observed_log_slope,
        "clean_first_hit_target_h2": target,
        "clean_first_hits": {
            "successes": sum(value > 0 for value in clean_first_hits),
            "total": len(clean_first_hits),
            "median_n_among_successes": float(
                np.median([value for value in clean_first_hits if value > 0])
            ),
        },
        "independent_checker": independent,
        "negative_controls": controls,
        "limitations": (
            "Complete only for the committed finite cover and contaminant grid; "
            "does not empirically prove the paper's infinite-class minimax theorem."
        ),
        "git_sha": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "cpu_estimate": "uncertain runtime; route to Hugging Face cpu-upgrade",
        "actual_logical_cpus_visible": os.cpu_count(),
        "platform": platform.platform(),
        "max_rss_reported": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "max_rss_unit": "bytes" if sys.platform == "darwin" else "KiB",
        "runtime_seconds": time.perf_counter() - started,
    }
    (OUT / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print("=== PROPER YATRACOS HUBER RESULT ===")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
