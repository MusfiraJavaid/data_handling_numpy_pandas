# Data Handling with NumPy & Pandas — Advanced (Colab-ready)

This repo contains advanced, Colab-ready notebooks for NumPy and Pandas, with real-world case studies and visualizations (Matplotlib & Seaborn).

## Files
- `NumPy_Advanced.ipynb` — advanced NumPy techniques, memmap, broadcasting, Numba examples.
- `Pandas_Advanced.ipynb` — I/O at scale, groupby/window, time-series, categorical, performance tips, and visualizations.
- `advanced_case_studies.ipynb` — ETL, feature engineering, large-join optimization examples.
- `scripts/generate_datasets.py` — regenerate datasets.
- `datasets/sample_data.csv`, `datasets/timeseries.csv` — sample CSVs used by notebooks.
- `requirements.txt` — packages to install (if running locally).

## Open in Colab
To open any notebook directly in Colab, click the **Open in Colab** badge for the notebook in the GitHub repo (badge template is included in notebooks).

### Quick Colab tips
- Mount Google Drive if you want to save outputs: `from google.colab import drive; drive.mount('/content/drive')`
- Install extras in Colab if needed: `!pip install -r requirements.txt`
- Use the provided `scripts/generate_datasets.py` to recreate sample datasets in the runtime.

