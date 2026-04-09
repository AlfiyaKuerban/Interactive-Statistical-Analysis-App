import pandas as pd

# Load GOLD dataset
gold = pd.read_csv('data/gold/btc_sentiment_gold.csv')
gold['date'] = pd.to_datetime(gold['date'])

# Load Google Trends
trends = pd.read_csv('data/silver/google_trends_bitcoin.csv', skiprows=2)
trends.columns = ['date', 'search_interest']
trends['date'] = pd.to_datetime(trends['date'])

# Merge datasets
merged = pd.merge(gold, trends, on='date', how='left')

# Create new variable
median_value = merged['search_interest'].median()

merged['high_interest'] = (merged['search_interest'] > median_value).astype(int)

# Check result
print(merged.head())
print(merged[['search_interest', 'high_interest']].describe())

# Save final dataset
merged.to_csv('data/gold/final_dataset.csv', index=False)

print("✅ Final dataset saved!")


print("Missing search_interest values:", merged['search_interest'].isna().sum())
print("Total rows:", len(merged))
print(merged[['date', 'search_interest', 'high_interest']].head(10))

print(trends.head(10))