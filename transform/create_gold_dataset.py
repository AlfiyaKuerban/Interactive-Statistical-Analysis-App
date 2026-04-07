import pandas as pd
from pathlib import Path

btc = pd.read_csv("data/silver/btc_daily_clean.csv")
fear_greed = pd.read_csv("data/silver/fear_greed_clean.csv")

gold = pd.merge(btc, fear_greed, on="date", how="inner")

gold["btc_daily_return"] = gold["btc_close"].pct_change()
gold["positive_return"] = (gold["btc_daily_return"] > 0).astype(int)

# set logical order for sentiment categories
order = ["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"]

gold["value_classification"] = pd.Categorical(
    gold["value_classification"],
    categories=order,
    ordered=True
)

gold = gold.dropna()

# optional: sort by date
gold = gold.sort_values("date")

output_path = Path("data/gold") / "btc_sentiment_gold.csv"
gold.to_csv(output_path, index=False)

print(f"Saved {output_path}")
