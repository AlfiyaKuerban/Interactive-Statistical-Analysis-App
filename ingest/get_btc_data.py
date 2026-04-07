
import requests
import json
from datetime import datetime
from pathlib import Path

url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",
    "interval": "1d",
    "limit": 30
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

output_path = Path("data/bronze/binance") / f"btc_{timestamp}.json"

with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {output_path}")
