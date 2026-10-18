
import sqlite3
from pathlib import Path

db_path = Path("data/ireland_inflation.db")

query = """
SELECT
    strftime('%Y', date(Date)) AS Year,
    ROUND(AVG(VALUE), 2) AS Average_Annual_Inflation
FROM annual_inflation
WHERE "Commodity Group" = 'Food and non-alcoholic beverages'
  AND date(Date) >= '2021-01-01'
  AND date(Date) < '2026-01-01'
GROUP BY strftime('%Y', date(Date))
ORDER BY Year;
"""

with sqlite3.connect(db_path) as connection:
    results = connection.execute(query).fetchall()

print("Average monthly annual food inflation by year")
print("-" * 48)

for year, rate in results:
    print(f"{year}: {rate:.2f}%")
