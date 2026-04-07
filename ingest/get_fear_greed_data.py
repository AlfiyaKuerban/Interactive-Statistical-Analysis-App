
import requests
import json
from datetime import datetime
from pathlib import Path

url = "https://api.alternative.me/fng/"

params = {
    "limit": 30,
    "format": "json"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

output_path = Path("data/bronze/alternative_me") / f"fear_greed_{timestamp}.json"

with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {output_path}")
