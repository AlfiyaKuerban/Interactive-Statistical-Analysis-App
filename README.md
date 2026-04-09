# Bitcoin Returns & Google Search Interest Analysis

## Project Overview

This project extends a Bitcoin data pipeline (Bronze → Silver → Gold architecture) by integrating an external dataset: **Google Trends search interest**.

The goal is to analyze whether public attention toward Bitcoin is associated with:

* returns
* volatility
* and positive-return behavior

The project also includes an **interactive Streamlit app** that allows users to explore the dataset and run statistical tests.

---

## Project Structure

```
your-repo/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│       └── final_dataset.csv
│
├── ingest/
├── transform/
├── notebooks/
│   └── analysis_part2.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── assignment4_analysis_plan.md
├── assignment4_reflection.md
├── README.md
├── requirements.txt
└── .env.example
```

---

## Data Pipeline

### Bronze Layer

* Raw API data (Bitcoin + Fear & Greed)

### Silver Layer

* Cleaned and structured data
* Date formatting and type conversion

### Gold Layer

* Final merged dataset
* Added features:

  * `btc_daily_return`
  * `positive_return`
  * `search_interest`
  * `high_interest`

---

## External Data Source

* **Google Trends**
* Keyword: *Bitcoin*
* Joined by: `date`

This adds context about public attention and market sentiment.

---

## Statistical Analysis

This project includes the following tests:

### 1. One-sample t-test

* Is the average BTC return different from 0?

### 2. Two-sample t-test

* Do returns differ between high vs low search-interest days?

### 3. Variance comparison (Levene test)

* Is volatility different between groups?

### 4. Correlation analysis (Pearson)

* Is search interest associated with BTC returns?

### 5. Chi-square test

* Is positive return independent of search-interest level?

---

## Key Insight

The most important finding:

> Google search interest does not significantly change average Bitcoin returns,
> but it is associated with **significantly different volatility**.

This suggests that public attention may reflect **market uncertainty and price swings**, rather than predictable gains.

---

## Streamlit App

This project includes an interactive dashboard with:

* project overview
* dataset preview
* visual analysis
* hypothesis testing
* interpretation of results

### Run the app locally:

```bash
streamlit run app/streamlit_app.py
```

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Limitations

* Small dataset
* Google Trends data is normalized
* Results are associative, not causal
* External factors (news, macro events) not included

---

## Author

**Alfiya Kuerban**
Applied Data Analytics — Durham College

---

## Acknowledgement

* Binance API (Bitcoin data)
* Alternative.me (Fear & Greed Index)
* Google Trends (search interest data)

---

