import pandas as pd
from pathlib import Path

# Location of raw datasets
DATA_DIR = Path("data/raw")

# All 10 datasets
files = [
    "fund_master.csv",
    "benchmark_indices.csv",
    "portfolio_holdings.csv",
    "aum_by_fund_house.csv",
    "industry_folio_count.csv",
    "category_inflows.csv",
    "monthly_sip_inflows.csv",
    "scheme_performance.csv",
    "investor_transactions.csv",
    "nav_history.csv"
]

for file in files:
    file_path = DATA_DIR / file

    print("\n" + "=" * 80)
    print(f"DATASET: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)

        # Shape
        print("\nSHAPE:")
        print(df.shape)

        # Data types
        print("\nDATA TYPES:")
        print(df.dtypes)

        # First five rows
        print("\nFIRST 5 ROWS:")
        print(df.head())

        # Basic anomaly checks
        print("\nANOMALY CHECK:")

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) > 0:
            print("Missing values:")
            print(missing)
        else:
            print("No missing values found.")

        duplicates = df.duplicated().sum()
        print(f"Duplicate rows: {duplicates}")

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")

    except Exception as e:
        print(f"ERROR while reading {file}: {e}")