import pandas as pd
from pathlib import Path

# ============================================================
# POWER BI DATA PREPARATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Create processed folder
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

print("Preparing Power BI datasets...")
print("=" * 60)

# ============================================================
# 1. FUND MASTER + FUND SCORECARD
# ============================================================

fund_master = pd.read_csv(
    RAW_DIR / "fund_master.csv"
)

# Load the Day 2 fund scorecard
scorecard_path = BASE_DIR / "fund_scorecard.csv"

if scorecard_path.exists():

    fund_scorecard = pd.read_csv(
        scorecard_path
    )

    # Keep only performance columns that are not already
    # present in fund_master
    scorecard_columns = [
        "amfi_code",
        "cagr_3y",
        "sharpe_ratio",
        "alpha",
        "beta",
        "max_drawdown",
        "cagr_score",
        "sharpe_score",
        "alpha_score",
        "expense_score",
        "drawdown_score",
        "fund_score",
        "rank"
    ]

    fund_scorecard = fund_scorecard[
        [
            col for col in scorecard_columns
            if col in fund_scorecard.columns
        ]
    ]

    # Merge performance data using AMFI code
    fund_master = fund_master.merge(
        fund_scorecard,
        on="amfi_code",
        how="left"
    )

fund_master.to_csv(
    PROCESSED_DIR / "fund_master.csv",
    index=False
)

print("1/8 fund_master.csv + scorecard created")
# ============================================================
# 2. NAV HISTORY
# ============================================================

nav_history = pd.read_csv(
    RAW_DIR / "nav_history.csv"
)

nav_history["date"] = pd.to_datetime(
    nav_history["date"],
    errors="coerce"
)

nav_history["nav"] = pd.to_numeric(
    nav_history["nav"],
    errors="coerce"
)

nav_history = nav_history.dropna(
    subset=["amfi_code", "date", "nav"]
)

nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)

nav_history.to_csv(
    PROCESSED_DIR / "nav_history.csv",
    index=False
)

print("2/8 nav_history.csv created")


# ============================================================
# 3. BENCHMARK INDICES
# ============================================================

benchmark = pd.read_csv(
    RAW_DIR / "benchmark_indices.csv"
)

if "date" in benchmark.columns:
    benchmark["date"] = pd.to_datetime(
        benchmark["date"],
        errors="coerce"
    )

benchmark.to_csv(
    PROCESSED_DIR / "benchmark_indices.csv",
    index=False
)

print("3/8 benchmark_indices.csv created")


# ============================================================
# 4. AUM BY FUND HOUSE
# ============================================================

aum = pd.read_csv(
    RAW_DIR / "aum_by_fund_house.csv"
)

if "date" in aum.columns:
    aum["date"] = pd.to_datetime(
        aum["date"],
        errors="coerce"
    )

aum.to_csv(
    PROCESSED_DIR / "aum_by_fund_house.csv",
    index=False
)

print("4/8 aum_by_fund_house.csv created")


# ============================================================
# 5. INDUSTRY FOLIO COUNT
# ============================================================

# Automatically find the folio-count CSV
folio_files = list(RAW_DIR.glob("*folio_count*.csv"))

print("Folio files found:", [f.name for f in folio_files])

if len(folio_files) == 0:
    raise FileNotFoundError(
        "No folio count CSV was found inside data/raw"
    )

folio_path = folio_files[0]

print("Using folio file:", folio_path.name)

folio = pd.read_csv(folio_path)

folio["month"] = pd.to_datetime(
    folio["month"],
    errors="coerce"
)

folio.to_csv(
    PROCESSED_DIR / "industry_folio_count.csv",
    index=False
)

print("5/8 industry_folio_count.csv created")

# ============================================================
# 6. MONTHLY SIP INFLOWS
# ============================================================

sip = pd.read_csv(
    RAW_DIR / "monthly_sip_inflows.csv"
)

sip["month"] = pd.to_datetime(
    sip["month"],
    errors="coerce"
)

sip.to_csv(
    PROCESSED_DIR / "monthly_sip_inflows.csv",
    index=False
)

print("6/8 monthly_sip_inflows.csv created")


# ============================================================
# 7. INVESTOR TRANSACTIONS
# ============================================================

investor = pd.read_csv(
    RAW_DIR / "investor_transactions.csv"
)

investor["transaction_date"] = pd.to_datetime(
    investor["transaction_date"],
    errors="coerce"
)

investor["amount_inr"] = pd.to_numeric(
    investor["amount_inr"],
    errors="coerce"
)

investor.to_csv(
    PROCESSED_DIR / "investor_transactions.csv",
    index=False
)

print("7/8 investor_transactions.csv created")


# ============================================================
# 8. CATEGORY INFLOWS
# ============================================================

category = pd.read_csv(
    RAW_DIR / "category_inflows.csv"
)

category["month"] = pd.to_datetime(
    category["month"],
    errors="coerce"
)

category["net_inflow_crore"] = pd.to_numeric(
    category["net_inflow_crore"],
    errors="coerce"
)

category.to_csv(
    PROCESSED_DIR / "category_inflows.csv",
    index=False
)

print("8/8 category_inflows.csv created")


# ============================================================
# FINAL VERIFICATION
# ============================================================

print()
print("=" * 60)
print("POWER BI DATA PREPARATION COMPLETE")
print("=" * 60)

files = [
    "fund_master.csv",
    "nav_history.csv",
    "benchmark_indices.csv",
    "aum_by_fund_house.csv",
    "industry_folio_count.csv",
    "monthly_sip_inflows.csv",
    "investor_transactions.csv",
    "category_inflows.csv"
]

for i, filename in enumerate(files, start=1):

    path = PROCESSED_DIR / filename

    if path.exists():

        df = pd.read_csv(path)

        print(
            f"{i}. {filename:<30} "
            f"OK | Rows: {len(df):,}"
        )

    else:

        print(
            f"{i}. {filename:<30} "
            f"MISSING"
        )