# Ireland CPI Inflation Analysis

A data analytics project exploring historical inflation trends in Ireland using official Consumer Price Index (CPI) data from the Central Statistics Office (CSO).

## Project Overview

This project demonstrates a complete data analytics workflow, from retrieving and cleaning official data to storing it in SQLite, analysing it using SQL, and visualising trends with Matplotlib.

## Objectives

- Retrieve official CPI data programmatically from the CSO.
- Clean and prepare the dataset using Python and Pandas.
- Store the processed data in an SQLite database.
- Analyse inflation across different commodity groups using SQL.
- Visualise historical inflation trends.
- Communicate findings through charts and documentation.

## Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- CSO PxStat API

## Data Source

Central Statistics Office (Ireland)

[CSO CPI dataset API](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CPM01/CSV/1.0/en)

The processed dataset contains 4,646 observations across 13 commodity groups, covering November 1976 to December 2025.

## Key Findings

- Housing and energy experienced substantial inflation increases during 2021–2023.
- Food inflation accelerated during 2022–2023 before easing.
- Overall inflation slowed after increasing during 2021–2022.
- Lower inflation does not necessarily mean lower prices; it can mean prices are rising more slowly.

See [project_insights.md](project_insights.md) for further findings and limitations.

## Project Structure

- `data/raw/` — downloaded CSO data
- `data/processed/` — cleaned inflation data
- `data/ireland_inflation.db` — SQLite database
- `outputs/` — generated visualisations
- `fetch_data.py` — retrieves the source data
- `clean_data.py` — cleans and prepares the data
- `database.py` — loads the processed data into SQLite
- `analyze_sql.py` — analyses inflation by category and date
- `food_inflation_trend.py` — analyses food inflation trends
- `category_inflation_analysis.py` — compares category-level inflation
- `visualize_trends.py` — creates inflation charts
- `project_insights.md` — documents findings and limitations

## How to Run

Install the required Python packages:

```bash
python -m pip install pandas requests matplotlib
```

Run the scripts from the project root directory in this order:

```bash
python fetch_data.py
python clean_data.py
python database.py
python analyze_sql.py
python food_inflation_trend.py
python category_inflation_analysis.py
python visualize_trends.py
```

## Limitations

This project describes historical inflation trends. It does not establish the causes of inflation, measure individual household spending, or forecast future inflation.

The downloaded dataset currently ends in December 2025.

## Conclusion

This project demonstrates practical skills in data retrieval, data cleaning, SQL analysis, database storage, and data visualisation using official Irish statistics.
