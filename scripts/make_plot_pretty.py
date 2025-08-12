import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSV = os.path.join(ROOT, "data", "ai_capex_by_region.csv")
OUT = os.path.join(ROOT, "outputs")
os.makedirs(OUT, exist_ok=True)

def make_pretty_plot(csv_in, out_png, title, subtitle, source_note):
    df = pd.read_csv(csv_in).sort_values("capex_usd_billion", ascending=False).reset_index(drop=True)
    fig = plt.figure(figsize=(16, 9), dpi=180)
    ax = fig.add_axes([0.08, 0.22, 0.88, 0.68])
    bars = ax.bar(df["region"], df["capex_usd_billion"])
    for rect, val in zip(bars, df["capex_usd_billion"]):
        ax.text(rect.get_x() + rect.get_width()/2, rect.get_height(), f"{val:.0f}", ha="center", va="bottom", fontsize=16)
    ax.set_title(title, fontsize=24, pad=16)
    ax.set_xlabel("Region", fontsize=16, labelpad=10)
    ax.set_ylabel("USD billions", fontsize=16, labelpad=10)
    ax.tick_params(axis="x", labelsize=16)
    ax.tick_params(axis="y", labelsize=14)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
    fig.text(0.08, 0.12, subtitle, fontsize=13)
    fig.text(0.08, 0.08, source_note, fontsize=11, alpha=0.8)
    ax.grid(True, axis="y", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.set_axisbelow(True)
    fig.savefig(out_png, bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    make_pretty_plot(
        CSV,
        os.path.join(OUT, "ai_capex_by_region_pretty.png"),
        title="AI Infrastructure CapEx by Region (approx. 2025)",
        subtitle="Order-of-magnitude view for discussion; see repo for sources.",
        source_note="Source: public company guidance and announcements; EU proposal; compiled by author"
    )
