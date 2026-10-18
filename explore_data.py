
import pandas as pd

df = pd.read_csv("data/raw/cso_cpi.csv", encoding="utf-8-sig")

# Clean column names
df.columns = (
    df.columns
    .str.replace("ï»¿", "", regex=False)
    .str.replace('"', "", regex=False)
    .str.strip()
)

# Convert VALUE to numeric format
df["VALUE"] = pd.to_numeric(df["VALUE"], errors="coerce")

print("\n--- Clean column names ---")
print(df.columns.tolist())

print("\n--- Missing values by statistical series ---")
print(
    df.groupby("Statistic Label")["VALUE"]
    .agg(total_rows="size", missing_values=lambda s: s.isna().sum())
)

print("\n--- Latest annual inflation observations ---")
annual = df[
    df["Statistic Label"]
    == "Percentage Change over 12 months for Consumer Price Index"
]

print(
    annual.sort_values("TLIST(M1)")
    [["Month", "Commodity Group", "VALUE"]]
    .tail(15)
    .to_string(index=False)
)
