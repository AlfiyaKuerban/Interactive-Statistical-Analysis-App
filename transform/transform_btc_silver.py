
import json
import pandas as pd
from pathlib import Path

# find all json files in bronze/binance
files = list(Path("data/bronze/binance").glob("*.json"))

# pick the first file
file_path = files[0]

# load json
with open(file_path, "r") as f:
    raw = json.load(f)

    df = pd.DataFrame(raw, columns=[
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "num_trades",
    "taker_buy_base", "taker_buy_quote", "ignore"
])
    
df["date"] = pd.to_datetime(df["open_time"], unit="ms").dt.date

df["btc_close"] = df["close"].astype(float)
df["btc_volume"] = df["volume"].astype(float)

silver = df[["date", "btc_close", "btc_volume"]]

output_path = Path("data/silver") / "btc_daily_clean.csv"

silver.to_csv(output_path, index=False)

print(f"Saved {output_path}")