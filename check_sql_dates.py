import sqlite3
from pathlib import Path

db_path = Path("data/ireland_inflation.db")

with sqlite3.connect(db_path) as connection:
    rows = connection.execute("""
        SELECT Date, "Commodity Group", VALUE
        FROM annual_inflation
        ORDER BY Date DESC
        LIMIT 5;
    """).fetchall()

    for row in rows:
        print(row)