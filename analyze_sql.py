
import sqlite3
from pathlib import Path

db_path = Path("data/ireland_inflation.db")

with sqlite3.connect(db_path) as connection:
    query = """
        SELECT
            "Commodity Group",
            VALUE
        FROM annual_inflation
        WHERE date(Date) = '2025-12-01'
        ORDER BY VALUE DESC;
    """

    rows = connection.execute(query).fetchall()

    print("Annual inflation by category — December 2025")
    for category, rate in rows:
        print(f"{category}: {rate:.1f}%")
