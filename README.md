# AI Infrastructure CapEx by Region (approx. 2025)

This repo contains the dataset and code behind a simple comparison of **AI/data‑center capital expenditure** across regions: **US, Europe, China**.  
It is designed to support a short LinkedIn post and show basic data/visualization skills.

## What’s inside
- `data/ai_capex_by_region.csv` — small dataset used for the chart.
- `data/ai_capex_by_region_sources.md` — source notes and caveats.
- `notebooks/capex_analysis.ipynb` — notebook to load and plot the data.
- `scripts/make_plot.py` — script to recreate the PNG in `outputs/`.
- `outputs/ai_capex_by_region_plot.png` — pre‑rendered chart.

## Quickstart
```bash
# 1) create and activate a venv (optional)
python -m venv .venv
# Windows PowerShell
. .venv/Scripts/Activate.ps1
# macOS/Linux
source .venv/bin/activate

# 2) install deps
pip install -r requirements.txt

# 3) run the script to generate the chart
python scripts/make_plot.py
```

The PNG will be saved to `outputs/ai_capex_by_region_plot.png`.

## Methodology (brief)
- **US**: aggregated 2025 AI/data‑center CapEx guidance from major hyperscalers (Amazon, Microsoft, Alphabet, Meta).  
- **Europe**: EU‑level AI “gigafactory” funding proposal converted to USD (used as a near‑term proxy).  
- **China**: combined announcements from Baidu, Alibaba, Tencent related to AI chips and DC investment (H1 2024 baseline).  

> These are **order‑of‑magnitude** figures. Some numbers reflect guidance/announcements rather than realized spend. Replace with sourced figures as you refine.

## License
MIT — see `LICENSE`.