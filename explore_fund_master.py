import pandas as pd

# Load fund master dataset
file_path = "data/raw/fund_master.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# --------------------------------------------------
# UNIQUE FUND HOUSES
# --------------------------------------------------

print("\n" + "=" * 70)
print("UNIQUE FUND HOUSES")
print("=" * 70)

fund_houses = df["fund_house"].dropna().unique()

print(fund_houses)
print("Total Fund Houses:", len(fund_houses))


# --------------------------------------------------
# UNIQUE CATEGORIES
# --------------------------------------------------

print("\n" + "=" * 70)
print("UNIQUE CATEGORIES")
print("=" * 70)

categories = df["category"].dropna().unique()

print(categories)
print("Total Categories:", len(categories))


# --------------------------------------------------
# UNIQUE SUB-CATEGORIES
# --------------------------------------------------

print("\n" + "=" * 70)
print("UNIQUE SUB-CATEGORIES")
print("=" * 70)

sub_categories = df["sub_category"].dropna().unique()

print(sub_categories)
print("Total Sub-Categories:", len(sub_categories))


# --------------------------------------------------
# UNIQUE RISK CATEGORIES
# --------------------------------------------------

print("\n" + "=" * 70)
print("UNIQUE RISK CATEGORIES")
print("=" * 70)

risk_categories = df["risk_category"].dropna().unique()

print(risk_categories)
print("Total Risk Categories:", len(risk_categories))


# --------------------------------------------------
# AMFI SCHEME CODES
# --------------------------------------------------

print("\n" + "=" * 70)
print("AMFI SCHEME CODES")
print("=" * 70)

print(df["amfi_code"].head(20).to_string(index=False))

print("\nTotal AMFI Codes:", df["amfi_code"].nunique())


# --------------------------------------------------
# PLAN TYPES
# --------------------------------------------------

print("\n" + "=" * 70)
print("PLAN TYPES")
print("=" * 70)

print(df["plan"].value_counts())


# --------------------------------------------------
# SEBI CATEGORY CODES
# --------------------------------------------------

print("\n" + "=" * 70)
print("SEBI CATEGORY CODES")
print("=" * 70)

print(df["sebi_category_code"].value_counts())


print("\n" + "=" * 70)
print("FUND MASTER EXPLORATION COMPLETED")
print("=" * 70)