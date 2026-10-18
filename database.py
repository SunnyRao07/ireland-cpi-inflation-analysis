
import sqlite3
import pandas as pd
from pathlib import Path

# Paths to our input data and output database
csv_path = Path("data/processed/annual_inflation.csv")
db_path = Path("data/ireland_inflation.db")

# Create the data folder if needed
db_path.parent.mkdir(parents=True, exist_ok=True)

# Read the cleaned CSV
df = pd.read_csv(csv_path, parse_dates=["Date"])

# Open (or create) the SQLite database
with sqlite3.connect(db_path) as connection:

    # Load the data into a SQL table
    df.to_sql(
        "annual_inflation",
        connection,
        if_exists="replace",
        index=False
    )

    # Verify how many records were loaded
    result = connection.execute(
        "SELECT COUNT(*) FROM annual_inflation"
    ).fetchone()

    print("Rows loaded:", result[0])

print("Database saved to:", db_path.resolve())
