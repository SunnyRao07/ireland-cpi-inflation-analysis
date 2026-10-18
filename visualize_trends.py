
import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Locate the SQLite database
db_path = Path("data/ireland_inflation.db")

# Read monthly inflation data for three categories
query = """
SELECT
    Date,
    "Commodity Group",
    VALUE
FROM annual_inflation
WHERE "Commodity Group" IN (
    'All items',
    'Food and non-alcoholic beverages',
    'Housing, water, electricity, gas and other fuels'
)
ORDER BY Date;
"""

with sqlite3.connect(db_path) as connection:
    df = pd.read_sql_query(query, connection)

# Convert dates into proper datetime values
df["Date"] = pd.to_datetime(df["Date"])

# Keep only the recent period: 2020–2025
df = df[df["Date"] >= "2020-01-01"]

# Reshape the data
chart_data = df.pivot(
    index="Date",
    columns="Commodity Group",
    values="VALUE"
)

# Create the line chart
chart_data.plot(figsize=(12, 6), linewidth=1.8)

plt.title("Ireland: Annual Inflation Rate by Category")
plt.xlabel("Year")
plt.ylabel("Inflation rate (%)")
plt.grid(True, alpha=0.3)
plt.legend(title="Category")
plt.tight_layout()

# Save the chart
output_path = Path("outputs")
output_path.mkdir(parents=True, exist_ok=True)

plt.savefig(output_path / "inflation_trends.png", dpi=300)
plt.show()

print("Chart saved to outputs/inflation_trends.png")
