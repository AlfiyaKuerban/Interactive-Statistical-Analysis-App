# Assignment 4 — Analysis Plan

## 1. Project Overview

This project extends the Assignment 3 Bitcoin data pipeline by adding an external data source: Google Trends search interest for "Bitcoin".

The goal is to explore whether public attention (measured by search interest) is associated with Bitcoin returns, volatility, and positive-return behavior.

---

## 2. Data Sources

### Original Dataset (Assignment 3)

* Bitcoin price and volume (Binance API)
* Fear & Greed Index (sentiment)
* Derived variables:

  * daily return
  * positive return indicator

### New External Source

* Google Trends data (search interest for "Bitcoin")
* Joined by: **date**

---

## 3. Key Variables

* **btc_daily_return** (numeric)
* **positive_return** (categorical: 0/1)
* **search_interest** (numeric)
* **high_interest** (categorical: 0/1 based on median split)

---

## 4. Research Questions

1. Is the average Bitcoin return different from 0?
2. Do returns differ between high and low search-interest days?
3. Is return volatility different between high and low search-interest days?
4. Is search interest associated with Bitcoin returns?
5. Is the probability of a positive return independent of search-interest level?

---

## 5. Planned Statistical Tests

### 1. One-sample t-test

* Purpose: Test whether average BTC return differs from 0
* Variable: btc_daily_return

---

### 2. Two-sample t-test

* Purpose: Compare returns between high and low search-interest groups
* Variables:

  * numeric: btc_daily_return
  * categorical: high_interest

---

### 3. Variance comparison (Levene’s test)

* Purpose: Compare volatility (variance) between groups
* Reason: Levene test is robust to non-normal data

---

### 4. Correlation analysis (Pearson)

* Purpose: Measure linear relationship between:

  * search_interest
  * btc_daily_return

---

### 5. Chi-square test of independence

* Purpose: Test whether:

  * positive_return is independent of high_interest
* Uses contingency table

---

## 6. Expected Insights

* Search interest may not significantly change average returns
* However, it may be associated with higher volatility
* Public attention could reflect market uncertainty rather than predictable gains

---

## 7. Limitations Considered

* Small dataset (limited time period)
* Google Trends data is normalized, not absolute
* Results are associative, not causal
* External factors (news, macro events) are not included

---
