
import pandas as pd

df = pd.read_csv("data/raw/cso_cpi.csv", encoding="utf-8-sig")

print("\n--- Dataset shape ---")
print(df.shape)

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- First five rows ---")
print(df.head())

print("\n--- Commodity groups ---")
print(df["Commodity Group"].value_counts().head(15))

print("\n--- Statistical series ---")
print(df["Statistic Label"].value_counts())
