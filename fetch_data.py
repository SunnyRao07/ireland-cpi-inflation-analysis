
import requests
from pathlib import Path

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CPM01/CSV/1.0/en"

# Create the folder for our raw data
output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

# Request the dataset from the CSO
response = requests.get(url, timeout=30)
response.raise_for_status()

# Save the response as a CSV file
output_file = output_folder / "cso_cpi.csv"
output_file.write_text(response.text, encoding="utf-8-sig")

print("Download successful!")
print(f"Status code: {response.status_code}")
print(f"File saved to: {output_file.resolve()}")
print(f"File size: {output_file.stat().st_size:,} bytes")
