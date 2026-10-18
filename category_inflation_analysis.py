import sqlite3
from pathlib import Path

db_path = Path("data/ireland_inflation.db")

query = """
SELECT
    "Commodity Group",
    ROUND(AVG(VALUE), 2) AS Average_Inflation,
    ROUND(MAX(VALUE), 2) AS Highest_Monthly_Rate,
    ROUND(MIN(VALUE), 2) AS Lowest_Monthly_Rate,
    COUNT(*) AS Months_Analysed
FROM annual_inflation
WHERE "Commodity Group" != 'All items'
  AND date(Date) >= '2021-01-01'
  AND date(Date) < '2026-01-01'
GROUP BY "Commodity Group"
ORDER BY Average_Inflation DESC;
"""

with sqlite3.connect(db_path) as connection:
    results = connection.execute(query).fetchall()

print("Category inflation analysis: 2021–2025\n")

print(
    f"{'Category':<55} "
    f"{'Average':>10} "
    f"{'Highest':>10} "
    f"{'Lowest':>10} "
    f"{'Months':>8}"
)

print("-" * 100)

for category, avg_rate, max_rate, min_rate, months in results:
    print(
        f"{category:<55} "
        f"{avg_rate:>9.2f}% "
        f"{max_rate:>9.2f}% "
        f"{min_rate:>9.2f}% "
        f"{months:>8}"
    )
