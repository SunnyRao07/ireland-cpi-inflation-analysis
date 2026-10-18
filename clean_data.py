
import pandas as pd
from pathlib import Path

# 1. Load the original CSO data
df = pd.read_csv("data/raw/cso_cpi.csv", encoding="utf-8-sig")

# 2. Clean column names
df.columns = (
    df.columns
    .str.replace("ï»¿", "", regex=False)
    .str.replace('"', "", regex=False)
    .str.strip()
)

# 3. Convert values to numbers
df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")

# 4. Keep only the annual inflation series
annual = df[
    df["Statistic Label"]
    == "Percentage Change over 12 months for Consumer Price Index"
].copy()

# 5. Convert the month identifier into a proper date
annual["Date"] = pd.to_datetime(
    annual["TLIST(M1)"].astype(str),
    format="%Y%m"
)

# 6. Keep useful columns and remove rows without a value
annual = annual[
    ["Date", "Commodity Group", "VALUE", "UNIT"]
].dropna(subset=["VALUE"])

# 7. Check for duplicate month-category records
duplicates = annual.duplicated(
    subset=["Date", "Commodity Group"]
).sum()

print("Valid annual inflation rows:", len(annual))
print("Duplicate month-category records:", duplicates)
print("Date range:", annual["Date"].min(), "to", annual["Date"].max())

# 8. Save the cleaned dataset
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "annual_inflation.csv"
annual.to_csv(output_file, index=False)

print("Clean dataset saved to:", output_file.resolve())

# 9. Display all categories for the latest available month
latest_date = annual["Date"].max()

latest = annual[annual["Date"] == latest_date].sort_values(
    "VALUE", ascending=False
)

print("\nLatest available month:", latest_date.strftime("%B %Y"))
print(latest[["Commodity Group", "VALUE"]].to_string(index=False))
