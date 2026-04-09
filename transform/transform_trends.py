import pandas as pd

# Load Google Trends
trends = pd.read_csv('data/silver/google_trends_bitcoin.csv', skiprows=2)

# Rename columns
trends.columns = ['date', 'search_interest']

# Convert date
trends['date'] = pd.to_datetime(trends['date'])

# Check data
print(trends.head())
print(trends.info())