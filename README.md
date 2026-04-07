# Data Pipeline for BTC and Sentiment Analysis

## Project Overview

This project builds a small data pipeline using a medallion architecture (Bronze → Silver → Gold).

The pipeline collects Bitcoin market data and Fear & Greed sentiment data from public APIs, cleans and transforms the data, and produces a final dataset that is ready for statistical analysis.

This dataset will be used in Part 2 for hypothesis testing such as t-tests and proportion tests.

---

## Data Sources

* Binance API — daily BTC price (OHLCV data)
* Alternative.me API — Fear & Greed Index (market sentiment)

---

## Pipeline Structure

### Bronze Layer

* Raw API data is collected and saved as JSON files
* Multiple snapshots are stored with timestamps
* No changes are made to the data

### Silver Layer

* JSON data is parsed into tables
* Timestamps are converted into readable dates
* Columns are cleaned and renamed
* Data types are corrected
* Clean data is saved as CSV files

### Gold Layer

* BTC data and sentiment data are joined using the date column
* New features are created:

  * btc_daily_return
  * positive_return
* Final dataset is saved for analysis

---

## Project Structure

```
data/
  bronze/
  silver/
  gold/

ingest/
  get_btc_data.py
  get_fear_greed_data.py

transform/
  transform_btc_silver.py
  transform_fear_greed_silver.py
  create_gold_dataset.py

notebooks/

analysis_preview.md
README.md
requirements.txt
.env.example
.gitignore
```

---

## How to Run

### 1. Run ingestion (Bronze)

```
python ingest/get_btc_data.py
python ingest/get_fear_greed_data.py
```

### 2. Run transformations (Silver)

```
python transform/transform_btc_silver.py
python transform/transform_fear_greed_silver.py
```

### 3. Create Gold dataset

```
python transform/create_gold_dataset.py
```

---

## Final Output

The final dataset is saved at:

```
data/gold/btc_sentiment_gold.csv
```

This dataset includes:

* date
* btc_close
* btc_volume
* fear_greed_value
* value_classification
* btc_daily_return
* positive_return

---

## Future Analysis (Part 2)

This dataset supports:

* One-sample t-test
  (Is average BTC return different from 0?)

* Two-sample t-test
  (Are returns different between Fear and Greed days?)

* Proportion z-test
  (Is the proportion of positive-return days higher during Greed?)

---

## AI Usage

I used ChatGPT to help generate starter code for API requests and data transformation.

I verified the correctness of the pipeline manually and fixed issues such as timestamp conversion errors when parsing the Fear & Greed data.

---

## Notes

* This project focuses on building a clean and structured data pipeline. The design decisions (such as selected features and join strategy) are made to support statistical analysis in the next stage.
* Only a small number of Bronze files are included as representative samples.
