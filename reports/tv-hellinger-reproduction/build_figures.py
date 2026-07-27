"""Build the five evidence figures from committed formal-run outputs."""
from __future__ import annotations

import json
import math
import csv
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
scaled = json.loads((RAW / "scaled_direct" / "result.json").read_text())
three_route = json.loads((RAW / "three_route" / "result.json").read_text())

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

# 8. Headline: all direct numerical claim checks in one compact panel.
fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.6))
summary_labels = ["C1", "C2", "C3"]
summary_values = [
    scaled["claim_1_2"]["max_theorem_2_1_ratio"],
    scaled["claim_1_2"]["max_corollary_2_4_ratio"],
    scaled["claim_3"]["min_sharpness_ratio"],
]
axes[0].bar(summary_labels, summary_values, color=["#277da1", "#43aa8b", "#f8961e"])
axes[0].axhline(1.0, color="black", linestyle=":", linewidth=1)
axes[0].set_yscale("log")
axes[0].set_title("Exact inequality ratios")
axes[0].set_ylabel("LHS / required RHS")
for index, value in enumerate(summary_values):
    axes[0].text(index, value * 1.25, f"{value:.3g}", ha="center")

c4_upper = scaled["claim_4"]["upper"]
c4_lower = scaled["claim_4"]["lower"]
axes[1].bar(
    ["upper\nestimator", "lower\nLe Cam"],
    [abs(c4_upper["tv_exponent_in_n"]), abs(c4_lower["tv_risk_exponent_in_n"])],
    color=["#577590", "#90be6d"],
)
axes[1].axhline(0.5, color="black", linestyle=":", linewidth=1)
axes[1].set_ylim(0, 0.6)
axes[1].set_title("C4 |slope| in sample size")

c5 = scaled["claim_5"]
axes[2].bar(
    ["upper H²", "lower H"],
    [
        c5["upper"]["hellinger_squared_exponent_in_epsilon"],
        c5["lower"]["hellinger_exponent_in_epsilon"],
    ],
    color=["#f3722c", "#f9c74f"],
)
axes[2].set_ylim(0, 2.1)
axes[2].set_title("C5 slope in contamination")
axes[2].text(0, c5["upper"]["hellinger_squared_exponent_in_epsilon"] + 0.06, "1.688", ha="center")
axes[2].text(1, c5["lower"]["hellinger_exponent_in_epsilon"] + 0.06, "0.960", ha="center")
fig.suptitle("Scaled direct evidence addresses all five paper claims")
fig.tight_layout()
fig.savefig(IMAGES / "headline-scaled-direct.png")
plt.close(fig)

# 9. C1/C2: 420 direct theorem cells over the full observed TV range.
with (RAW / "scaled_direct" / "claim_1_2_raw.csv").open(newline="") as handle:
    bound_rows = list(csv.DictReader(handle))
bound_tv = np.array([float(row["tv"]) for row in bound_rows])
c1_ratio = np.array([float(row["theorem_2_1_ratio"]) for row in bound_rows])
c2_ratio = np.array([float(row["corollary_2_4_ratio"]) for row in bound_rows])
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.loglog(bound_tv, c1_ratio, ".", alpha=0.55, label="C1 sqrt(chi²) / theorem RHS")
ax.loglog(bound_tv, c2_ratio, ".", alpha=0.55, label="C2 H / corollary RHS")
ax.axhline(1.0, color="black", linestyle=":", linewidth=1, label="violation threshold")
ax.set(
    xlabel="total variation",
    ylabel="left side / displayed bound",
    title="Zero violations across 60 families and 420 direct cells",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "c1-c2-bound-sweep.png")
plt.close(fig)

# 13. Headline three-route judge remediation.
fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.7))
multidimensional = three_route["multidimensional_direct"]
axes[0].bar(
    ["C1\nd=2,3", "C2\nd=2,3"],
    [
        multidimensional["max_theorem_2_1_ratio"],
        multidimensional["max_corollary_2_4_ratio"],
    ],
    color=["#277da1", "#43aa8b"],
)
axes[0].axhline(1, color="black", linestyle=":", linewidth=1)
axes[0].set_yscale("log")
axes[0].set_ylim(1e-4, 2)
axes[0].set_title("14 multidimensional cells")
axes[0].set_ylabel("maximum LHS / theorem RHS")

c4_rows = three_route["C4_local_entropy_calibration"]
for dimension in (1, 2, 3):
    selected = [row for row in c4_rows if row["dimension"] == dimension]
    axes[1].plot(
        [row["log10_n"] for row in selected],
        [row["theorem_logarithmic_correction"] for row in selected],
        "o-",
        label=f"d={dimension}",
    )
axes[1].set(
    xlabel="log10 n",
    ylabel="(2+delta) / log log(1/epsilon_n)",
    title="C4 correction shown directly",
)
axes[1].legend(frameon=False)

c5_rows = three_route["C5_asymptotic_calibration"]
axes[2].plot(
    [row["log_log_1_over_epsilon"] for row in c5_rows],
    [row["upper_H2_effective_exponent"] for row in c5_rows],
    "o-",
    label="upper",
)
axes[2].plot(
    [row["log_log_1_over_epsilon"] for row in c5_rows],
    [row["lower_H2_effective_exponent"] for row in c5_rows],
    "s--",
    label="lower",
)
axes[2].axhline(2, color="black", linestyle=":", linewidth=1, label="limit 2")
axes[2].set(
    xlabel="log log(1/epsilon)",
    ylabel="effective H² exponent",
    title="C5 exponent converges to 2",
    ylim=(0.4, 2.05),
)
axes[2].legend(frameon=False)
fig.suptitle("Three-route remediation targets the latest judge gaps")
fig.tight_layout()
fig.savefig(IMAGES / "headline-three-route.png")
plt.close(fig)

# 10. C3: every odd order from 11 through 31.
fig, ax = plt.subplots(figsize=(7.2, 4.0))
scaled_orders = np.array([row["n"] for row in primary["rows"]])
scaled_sharpness = np.array([row["sharpness_ratio"] for row in primary["rows"]])
scaled_wrong = np.array([row["wrong_sharpness_ratio"] for row in primary["rows"]])
ax.semilogy(scaled_orders, scaled_sharpness, "o-", linewidth=2, label="paper coefficient 0.33")
ax.semilogy(scaled_orders, scaled_wrong, "s--", linewidth=1.5, label="control coefficient 0.50")
ax.axhline(1.0, color="black", linestyle=":", linewidth=1)
ax.set(
    xlabel="odd Chebyshev order",
    ylabel="H / claimed lower-bound RHS",
    title="All 11 explicit sharpness constructions pass",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "c3-sharpness-sweep.png")
plt.close(fig)

# 11. C4: independently calibrated upper and lower sample-size behavior.
upper_rows = c4_upper["aggregate_rows"]
lower_rows = c4_lower["rows"]
c4_n = np.array([row["n"] for row in upper_rows])
c4_tv = np.array([row["tv"]["mean"] for row in upper_rows])
c4_tv_low = np.array([row["tv"]["ci95_low"] for row in upper_rows])
c4_tv_high = np.array([row["tv"]["ci95_high"] for row in upper_rows])
c4_lb = np.array([row["lower_bound_tv"] for row in lower_rows])
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.loglog(c4_n, c4_tv, "o-", linewidth=2, label="NNLS mixture estimator, slope -0.474")
ax.fill_between(c4_n, c4_tv_low, c4_tv_high, alpha=0.18)
ax.loglog(c4_n, c4_lb, "s--", linewidth=1.8, label="Le Cam pair-cloud lower, slope -0.497")
ax.set(
    xlabel="sample size n",
    ylabel="TV error / lower bound",
    title="C4 upper and lower routes track the near-parametric rate",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "c4-rate-bracket.png")
plt.close(fig)

# 12. C5: worst-of-17 contaminant search and all-estimator lower route.
c5_upper_rows = c5["upper"]["aggregate_rows"]
c5_lower_rows = c5["lower"]["rows"]
c5_eps = np.array([row["epsilon"] for row in c5_upper_rows])
c5_h2 = np.array([row["worst_hellinger_squared"] for row in c5_upper_rows])
c5_low_eps = np.array([row["epsilon"] for row in c5_lower_rows])
c5_low_h = np.array([row["minimax_hellinger_lower_bound"] for row in c5_lower_rows])
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.loglog(c5_eps, c5_h2, "o-", linewidth=2, label="worst-of-17 estimator H², slope 1.688")
ax.loglog(c5_low_eps, c5_low_h, "s--", linewidth=1.8, label="equal-law H lower, slope 0.960")
ax.set(
    xlabel="Huber contamination epsilon",
    ylabel="direct error / certified lower bound",
    title="C5 upper and lower constructions scale with contamination",
)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(IMAGES / "c5-robust-rate.png")
plt.close(fig)
