
import os
import pandas as pd
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "ai_capex_by_region.csv")
OUT = os.path.join(ROOT, "outputs")
os.makedirs(OUT, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    for col in ["region", "capex_usd_billion"]:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    plt.figure(figsize=(9, 5))
    plt.bar(df["region"], df["capex_usd_billion"])
    plt.title("AI Infrastructure CapEx by Region (approx. 2025)")
    plt.xlabel("Region")
    plt.ylabel("CapEx (USD billions)")
    for i, v in enumerate(df["capex_usd_billion"]):
        plt.text(i, v, f"{v:.0f}", ha="center", va="bottom")
    out_path = os.path.join(OUT, "ai_capex_by_region_plot.png")
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print("Saved:", out_path)

if __name__ == "__main__":
    main()
