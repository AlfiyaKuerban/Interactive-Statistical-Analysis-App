# Statistical Analysis Preview

## Statistical Question

One question I want to answer in Part 2 is:
Is the average daily Bitcoin return different between Fear days and Greed days?

---

## Outcome Variable

The outcome variable is **btc_daily_return**, which represents the daily percentage change in Bitcoin price.

---

## Grouping Variable

The grouping variable is **value_classification**, which indicates whether the market sentiment is Fear or Greed.

---

## Binary Variable

I created a binary variable called **positive_return**, which is 1 if the daily return is positive and 0 otherwise.

This variable is useful because it allows me to perform proportion-based tests, such as checking whether positive returns happen more often during Greed periods.

---

## Hypotheses

For a two-sample t-test:

* Null hypothesis (H₀): The mean daily return is the same for Fear and Greed days.
* Alternative hypothesis (H₁): The mean daily return is different between Fear and Greed days.

For a proportion test:

* Null hypothesis (H₀): The proportion of positive-return days is the same for Fear and Greed days.
* Alternative hypothesis (H₁): The proportion of positive-return days is different between the two groups.

---

## Chosen Test

I think a **two-sample t-test** is appropriate for comparing the average returns between Fear and Greed days because we are comparing the means of two independent groups.

I can also use a **proportion z-test** to compare how often positive returns occur under different sentiment conditions.

---

## Summary

The dataset is designed to support statistical testing by including both numeric and categorical variables. The daily return and sentiment classification allow meaningful comparisons and hypothesis testing in Part 2.
