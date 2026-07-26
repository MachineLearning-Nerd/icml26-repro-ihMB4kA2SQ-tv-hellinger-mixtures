"""Build the five evidence figures from committed formal-run outputs."""
from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "release" / "space" / "evidence" / "raw"
IMAGES = Path(__file__).resolve().parent / "images"
IMAGES.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 180,
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)

primary = json.loads((RAW / "claim_1_3" / "result.json").read_text())
independent = json.loads((RAW / "claim_1_3" / "independent_checker.json").read_text())
analytic = json.loads((RAW / "analytic_certificate" / "result.json").read_text())
yatracos = json.loads((RAW / "yatracos_experiment" / "result.json").read_text())

rows = primary["rows"]
independent_rows = independent["rows"]
orders = np.array([row["n"] for row in rows])

# 1. Headline sharpness inequality.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ratios = np.array([row["sharpness_ratio"] for row in rows])
wrong = np.array([row["wrong_sharpness_ratio"] for row in rows])
ax.semilogy(orders, ratios, "o-", label="paper coefficient 0.33", linewidth=2)
ax.semilogy(orders, wrong, "s--", label="negative control 0.50", linewidth=1.5)
ax.axhline(1, color="black", linewidth=1, label="required threshold")
for x, y in zip(orders, ratios):
    ax.annotate(f"{y:.2f}", (x, y), xytext=(0, 7), textcoords="offset points", ha="center")
ax.set(xlabel="odd construction order n", ylabel="H / claimed lower-bound RHS")
ax.set_title("Explicit Gaussian mixtures satisfy the sharpness inequality")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "headline-sharpness.png")
plt.close(fig)

# 2. Independent integration agreement.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
metrics = {
    "TV (nonsmooth)": "tv_pi1_eta1",
    "Hellinger": "hellinger_pi2_eta2",
    "sqrt chi-square": "sqrt_chi2_pi1_eta1",
}
for label, key in metrics.items():
    errors = [
        abs(a[key] - b[key]) / max(abs(a[key]), abs(b[key]))
        for a, b in zip(rows, independent_rows)
    ]
    ax.semilogy(orders, errors, "o-", label=label)
ax.set(xlabel="odd construction order n", ylabel="relative disagreement")
ax.set_title("Adaptive and fixed-node quadrature agree independently")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "quadrature-agreement.png")
plt.close(fig)

# 3. Exact gamma-norm asymptotics.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
asymptotic_rows = analytic["c3_asymptotic_rows"]
ns = np.array([row["n"] for row in asymptotic_rows])
l1 = np.array([row["normalized_L1_rate"] for row in asymptotic_rows])
l2 = np.array([row["normalized_L2_rate"] for row in asymptotic_rows])
ax.plot(ns, l1, label="exact L1 gamma formula")
ax.plot(ns, l2, label="exact L2 gamma formula")
ax.axhline(0.5, color="black", linewidth=1, linestyle=":", label="proved limit 1/2")
probe = analytic["asymptotic_probe"]
ax.text(
    0.98,
    0.05,
    "n=10^50+1 probe\n"
    f"L1={probe['normalized_L1_rate']:.6f}\n"
    f"L2={probe['normalized_L2_rate']:.6f}",
    transform=ax.transAxes,
    ha="right",
    va="bottom",
)
ax.set(xlabel="odd order n", ylabel="-log(norm)/(n log n)", ylim=(0.25, 0.53))
ax.set_title("Exact norm formulas approach the hyper-exponential rate")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "norm-asymptotics.png")
plt.close(fig)

# 4. C4 inverse repair: show the two exact scaled asymptotic limits.
fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.7))
delta = 1.0
target_c = 2 + delta
ls = np.linspace(5, 200, 240)
lx = ls + np.log1p(target_c / ls)
same_power = (1 - target_c / lx) * (1 + target_c / ls)
slack_power = (1 - (2 + delta / 2) / lx) * (1 + target_c / ls)
axes[0].plot(ls, ls**2 * (same_power - 1), linewidth=2)
axes[0].axhline(-(2 + delta) ** 2, color="black", linestyle=":", label="limit = -9")
axes[0].axhline(0, color="black", linewidth=1)
axes[0].set(
    xlabel="L",
    ylabel="L² × (power - 1)",
    title="same delta: wrong sign",
)
axes[0].legend(frameon=False)
axes[1].plot(ls, ls * (slack_power - 1), color="#e76f51", linewidth=2)
axes[1].axhline(delta / 2, color="black", linestyle=":", label="limit = +0.5")
axes[1].axhline(0, color="black", linewidth=1)
axes[1].set(
    xlabel="L = log log(1/y)",
    ylabel="L × (power - 1)",
    title="delta/2: proving sign",
)
axes[1].legend(frameon=False)
fig.suptitle("The minimax inverse needs the quantified delta slack")
fig.tight_layout()
fig.savefig(IMAGES / "c4-inverse-repair.png")
plt.close(fig)

# 5. C5 lower-bound coefficient budget.
fig, ax = plt.subplots(figsize=(7.2, 3.3))
available = math.log(2) - 2 / 5.53
after_rho = available * (1 - 0.002)
labels = ["available", "after uniform-epsilon repair", "paper target", "rejected 0.34"]
values = [available, after_rho, 0.33, 0.34]
colors = ["#2a6f97", "#2a9d8f", "#6c757d", "#c44536"]
ax.barh(labels, values, color=colors)
ax.set_xlim(0.329, 0.341)
ax.axvline(0.33, color="black", linewidth=1, linestyle=":")
for index, value in enumerate(values):
    ax.text(value + 0.00008, index, f"{value:.6f}", va="center")
ax.set(xlabel="coefficient multiplying 1/log log(1/epsilon)")
ax.set_title("The continuous-amplitude repair retains margin above 0.33")
fig.tight_layout()
fig.savefig(IMAGES / "c5-coefficient-budget.png")
plt.close(fig)

# 6. Actual proper-estimator clean risk and exhaustive finite-cover lower bound.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
clean = yatracos["clean_minimax_rows"]
clean_n = np.array([row["n"] for row in clean])
clean_risk = np.array([row["observed_worst_yatracos_h2"] for row in clean])
clean_lower = np.array(
    [row["exhaustive_pair_tv2_lower_bound"] for row in clean]
)
ax.loglog(clean_n, clean_risk, "o-", linewidth=2, label="worst observed proper-estimator H²")
ax.loglog(clean_n, clean_lower, "s--", linewidth=1.8, label="exhaustive finite-cover TV² lower")
ax.set(
    xlabel="sample size n",
    ylabel="risk / certified lower bound",
    title="Clean proper-estimator risk falls across independent horizons",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "yatracos-clean-risk.png")
plt.close(fig)

# 7. Huber contamination: actual estimator risk and complete finite-cover lower.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
rate_rows = yatracos["huber_rate_rows"]
lower_rows = yatracos["huber_equal_law_rows"]
eps = np.array([row["epsilon"] for row in rate_rows])
observed = np.array([row["observed_worst_mean_h2"] for row in rate_rows])
lower = np.array([row["equal_law_minimax_h2_lower"] for row in lower_rows])
ax.loglog(eps, observed, "o-", linewidth=2, label="observed worst mean H² at n=1600")
ax.loglog(eps, lower, "s--", linewidth=1.8, label="equal-law finite-cover lower")
for x, y in zip(eps, observed):
    ax.annotate(f"{y:.2g}", (x, y), xytext=(0, 6), textcoords="offset points", ha="center")
ax.set(
    xlabel="Huber contamination epsilon",
    ylabel="squared-Hellinger loss",
    title="Actual Huber experiment and all-estimator finite-cover lower",
)
ax.legend(frameon=False)
ax.text(
    0.02,
    0.03,
    "Paper asymptotic term > 1 at every plotted epsilon;\n"
    "these points do not verify its exponent.",
    transform=ax.transAxes,
)
fig.tight_layout()
fig.savefig(IMAGES / "yatracos-huber-risk.png")
plt.close(fig)
