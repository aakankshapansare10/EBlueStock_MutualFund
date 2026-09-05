import pandas as pd

# Load fund master dataset
file_path = "data/raw/fund_master.csv"
df = pd.read_csv(file_path)

print("=" * 70)
print("AMFI CODE VALIDATION & DATA QUALITY SUMMARY")
print("=" * 70)

# --------------------------------------------------
# 1. CHECK TOTAL RECORDS
# --------------------------------------------------

print("\n1. TOTAL RECORDS")
print("Total rows:", len(df))


# --------------------------------------------------
# 2. CHECK AMFI CODE MISSING VALUES
# --------------------------------------------------

print("\n2. MISSING AMFI CODES")

missing_amfi = df["amfi_code"].isna().sum()

print("Missing AMFI codes:", missing_amfi)


# --------------------------------------------------
# 3. CHECK DUPLICATE AMFI CODES
# --------------------------------------------------

print("\n3. DUPLICATE AMFI CODES")

duplicate_amfi = df["amfi_code"].duplicated().sum()

print("Duplicate AMFI codes:", duplicate_amfi)


# --------------------------------------------------
# 4. CHECK AMFI CODE DATA TYPE
# --------------------------------------------------

print("\n4. AMFI CODE DATA TYPE")

print(df["amfi_code"].dtype)


# --------------------------------------------------
# 5. CHECK MISSING VALUES IN ALL COLUMNS
# --------------------------------------------------

print("\n5. MISSING VALUES BY COLUMN")

missing_values = df.isnull().sum()

print(missing_values)


# --------------------------------------------------
# 6. CHECK DUPLICATE ROWS
# --------------------------------------------------

print("\n6. DUPLICATE ROWS")

duplicate_rows = df.duplicated().sum()

print("Duplicate rows:", duplicate_rows)


# --------------------------------------------------
# 7. CHECK UNIQUE AMFI CODES
# --------------------------------------------------

print("\n7. UNIQUE AMFI CODES")

unique_amfi = df["amfi_code"].nunique()

print("Unique AMFI codes:", unique_amfi)


# --------------------------------------------------
# 8. AMFI CODE RANGE
# --------------------------------------------------

print("\n8. AMFI CODE RANGE")

print("Minimum AMFI code:", df["amfi_code"].min())
print("Maximum AMFI code:", df["amfi_code"].max())


# --------------------------------------------------
# 9. FINAL DATA QUALITY SUMMARY
# --------------------------------------------------

print("\n" + "=" * 70)
print("FINAL DATA QUALITY SUMMARY")
print("=" * 70)

print("Total records:", len(df))
print("Missing AMFI codes:", missing_amfi)
print("Duplicate AMFI codes:", duplicate_amfi)
print("Duplicate rows:", duplicate_rows)
print("Unique AMFI codes:", unique_amfi)

if missing_amfi == 0 and duplicate_amfi == 0:
    print("\nAMFI CODE VALIDATION: PASSED")
else:
    print("\nAMFI CODE VALIDATION: CHECK REQUIRED")

print("\nData quality validation completed.")

# --------------------------------------------------
# 10. VALIDATE AMFI CODES AGAINST NAV HISTORY
# --------------------------------------------------

print("\n" + "=" * 70)
print("AMFI CODE CROSS-DATASET VALIDATION")
print("=" * 70)

# Load NAV history
nav_df = pd.read_csv("data/raw/nav_history.csv")

# Convert both columns to the same data type
fund_master_codes = set(df["amfi_code"].dropna().astype(int))
nav_history_codes = set(nav_df["amfi_code"].dropna().astype(int))

# Find codes present in fund_master but missing from nav_history
missing_in_nav_history = fund_master_codes - nav_history_codes

print("AMFI codes in fund_master:", len(fund_master_codes))
print("AMFI codes in nav_history:", len(nav_history_codes))

print("\nCodes from fund_master missing in nav_history:")

if len(missing_in_nav_history) == 0:
    print("None")
    print("\nAMFI CROSS-DATASET VALIDATION: PASSED")
else:
    print(missing_in_nav_history)
    print("\nAMFI CROSS-DATASET VALIDATION: FAILED")