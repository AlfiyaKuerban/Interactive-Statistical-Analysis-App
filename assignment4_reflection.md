# Assignment 4 — Reflection

## 1. Overview

This project explored whether Google search interest is associated with Bitcoin returns and market behavior. By extending the Assignment 3 pipeline, I introduced a new external dataset and created a more complete analytical story.

---

## 2. Key Findings

* The average Bitcoin return was not significantly different from 0.
* There was no significant difference in returns between high and low search-interest days.
* Chi-square test suggested that positive-return probability is independent of search interest.
* However, variance comparison showed that volatility differs significantly between groups.
* Correlation analysis showed a weak and non-significant relationship.


The most important insight is that **search interest appears to be associated with volatility rather than average returns**.

---

## 3. Assumptions

* Observations are treated as independent daily values
* Data is assumed to be reasonably stable over the selected time period
* Chi-square assumes sufficient expected counts
* Linear relationship assumed in correlation analysis


---

## 4. Limitations

* The dataset is relatively small, which reduces statistical power
* Google Trends provides normalized scores, not exact search volumes
* Only one external variable (search interest) was included
* Other important factors (news sentiment, macroeconomic events) were not considered
* Results do not imply causation

---

## 5. Data and Join Issues

* The join was performed on date, which assumes alignment across datasets
* Some missing values appeared during merging and required handling
* Differences in frequency (daily vs weekly trends) required adjustment

---

## 6. What I Would Improve

* Extend the dataset to cover a longer time period
* Include additional external sources such as:

  * news sentiment
  * macroeconomic indicators
* Use more advanced models (regression or time-series analysis)
* Improve visualization interactivity

---

## 7. Final Reflection

This project helped me understand how to connect multiple datasets and apply statistical testing in a meaningful way. I learned that not all relationships are significant, and that interpreting results carefully is as important as running the tests.

---
