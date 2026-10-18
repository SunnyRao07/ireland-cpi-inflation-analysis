import pandas as pd

df = pd.read_csv("data/raw/cso_cpi.csv", encoding="utf-8-sig")

df["Month"] = pd.to_datetime(
    df["TLIST(M1)"].astype(str),
    format="%Y%m"
)

print("Earliest month:", df["Month"].min())
print("Latest month:", df["Month"].max())
print("Total rows:", len(df))