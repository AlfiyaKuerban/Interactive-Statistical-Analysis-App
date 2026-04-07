import json
import pandas as pd
from pathlib import Path

files = list(Path("data/bronze/alternative_me").glob("*.json"))

file_path = files[0]

with open(file_path, "r") as f:
    raw = json.load(f)

df = pd.DataFrame(raw["data"])
df["date"] = pd.to_datetime(df["timestamp"].astype(int), unit="s").dt.date
df["fear_greed_value"] = df["value"].astype(int)
silver = df[["date", "fear_greed_value", "value_classification"]]

output_path = Path("data/silver") / "fear_greed_clean.csv"

silver.to_csv(output_path, index=False)

print(f"Saved {output_path}")
