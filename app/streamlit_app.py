import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import pearsonr, chi2_contingency, levene

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Bitcoin & Google Trends Analysis",
    layout="wide"
)

# ---------------------------
# Load data
# ---------------------------
df = pd.read_csv("data/gold/final_dataset.csv")
df["date"] = pd.to_datetime(df["date"])

# ---------------------------
# Precompute test variables
# ---------------------------
returns = df["btc_daily_return"]

high = df[df["high_interest"] == 1]["btc_daily_return"]
low = df[df["high_interest"] == 0]["btc_daily_return"]

# One-sample t-test
t1_stat, t1_p = stats.ttest_1samp(returns, 0)

# Two-sample t-test
t2_stat, t2_p = stats.ttest_ind(high, low)

# Chi-square
table = pd.crosstab(df["positive_return"], df["high_interest"])
chi2_stat, chi2_p, dof, expected = chi2_contingency(table)

# Variance comparison
var_high = high.var()
var_low = low.var()
lev_stat, lev_p = levene(high, low)

# Correlation
corr_val, corr_p = pearsonr(df["search_interest"], df["btc_daily_return"])

# ---------------------------
# Title
# ---------------------------
st.title("Bitcoin Returns and Google Search Interest")
st.caption("Assignment 4 — Interactive Statistical Analysis App")

# ---------------------------
# 1. Project Overview
# ---------------------------
st.header("1. Project Overview")

st.write("""
This project extends the Assignment 3 Bitcoin pipeline by adding Google Trends data as a new external source.  
The goal is to explore whether public search interest in Bitcoin is associated with returns, volatility, and positive-return behavior.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Assignment 3 Dataset")
    st.write("""
- Bitcoin closing price  
- Bitcoin trading volume  
- Fear & Greed value  
- Sentiment classification  
- Daily return  
- Positive return flag
""")

with col2:
    st.subheader("New External Source")
    st.write("""
- Google Trends search interest for **Bitcoin**
- Joined by **date**
- New derived variable: **high_interest**
""")

st.subheader("Main Questions")
st.write("""
1. Is average BTC return different from 0?  
2. Do returns differ between high and low search-interest days?  
3. Is volatility different between high and low search-interest days?  
4. Is search interest correlated with BTC returns?  
5. Is positive return independent of search-interest level?
""")

# ---------------------------
# 2. Data Preview
# ---------------------------
st.header("2. Data Preview")

st.subheader("Sample of Final Dataset")
st.dataframe(df.head(), use_container_width=True)

st.subheader("Summary Statistics")
st.dataframe(df.describe(), use_container_width=True)

st.subheader("Column Descriptions")
st.write("""
- **date**: trading date  
- **btc_close**: Bitcoin closing price  
- **btc_volume**: Bitcoin trading volume  
- **fear_greed_value**: numeric sentiment score  
- **value_classification**: sentiment category  
- **btc_daily_return**: daily Bitcoin return  
- **positive_return**: 1 if daily return is positive, otherwise 0  
- **search_interest**: Google Trends score for Bitcoin  
- **high_interest**: 1 if search interest is above median, otherwise 0
""")

# ---------------------------
# 3. Visual Storytelling
# ---------------------------
st.header("3. Visual Storytelling")

st.write("These charts help motivate the formal tests shown later in the app.")

# Chart 1: time series
st.subheader("3.1 BTC Daily Returns Over Time")
st.line_chart(df.set_index("date")["btc_daily_return"])

# Chart 2: boxplot high vs low
st.subheader("3.2 Returns by Search-Interest Group")

fig1, ax1 = plt.subplots(figsize=(7, 4))
groups = [low.dropna(), high.dropna()]
ax1.boxplot(groups, labels=["Low Interest", "High Interest"])
ax1.set_ylabel("BTC Daily Return")
ax1.set_title("Distribution of Returns by Search Interest")
st.pyplot(fig1)

st.caption("This chart supports the two-sample t-test and variance comparison.")

# Chart 3: category counts for chi-square
st.subheader("3.4 Positive Return Count by Search-Interest Group")
count_table = pd.crosstab(df["high_interest"], df["positive_return"])
st.bar_chart(count_table)

st.caption("This chart supports the chi-square test of independence.")

# Chart 4: scatterplot for correlation
st.subheader("3.3 Search Interest vs BTC Daily Return")

fig2, ax2 = plt.subplots(figsize=(7, 4))
ax2.scatter(df["search_interest"], df["btc_daily_return"])
ax2.set_xlabel("Search Interest")
ax2.set_ylabel("BTC Daily Return")
ax2.set_title("Search Interest and BTC Return")
st.pyplot(fig2)

st.caption("This chart supports the correlation analysis.")


# ---------------------------
# 4. Hypothesis Testing
# ---------------------------
st.header("4. Hypothesis Testing")

test_choice = st.selectbox(
    "Choose a test to view",
    [
        "One-sample t-test",
        "Two-sample t-test",
        "Variance comparison",
        "Correlation analysis",
        "Chi-square test"
    ]
)

if test_choice == "One-sample t-test":
    st.subheader("One-sample t-test: Is mean BTC return different from 0?")
    st.write("**Null hypothesis:** The average BTC daily return equals 0.")
    st.write("**Alternative hypothesis:** The average BTC daily return is different from 0.")
    st.write(f"**T-statistic:** {t1_stat:.4f}")
    st.write(f"**P-value:** {t1_p:.4f}")

    if t1_p < 0.05:
        st.success("Conclusion: The average BTC return is significantly different from 0.")
    else:
        st.warning("Conclusion: The average BTC return is not significantly different from 0.")

    st.info("""
Why this test fits:
- The variable is numeric.
- We are comparing one sample mean to a fixed reference value (0).

Assumptions / limitation:
- Assumes daily returns are reasonably independent.
- Small sample size may weaken the reliability of conclusions.
""")

elif test_choice == "Two-sample t-test":
    st.subheader("Two-sample t-test: Are returns different between high and low search-interest days?")
    st.write("**Null hypothesis:** Average returns are equal in both groups.")
    st.write("**Alternative hypothesis:** Average returns differ between groups.")
    st.write(f"**T-statistic:** {t2_stat:.4f}")
    st.write(f"**P-value:** {t2_p:.4f}")

    if t2_p < 0.05:
        st.success("Conclusion: Returns differ significantly between high and low search-interest days.")
    else:
        st.warning("Conclusion: No significant difference in returns between high and low search-interest days.")

    st.info("""
Why this test fits:
- BTC return is numeric.
- high_interest creates two groups.

Assumptions / limitation:
- Observations should be reasonably independent.
- Small sample size may reduce statistical power.
""")

elif test_choice == "Variance comparison":
    st.subheader("Variance Comparison: Is volatility different between high and low search-interest days?")
    st.write(f"**Variance (High interest):** {var_high:.6f}")
    st.write(f"**Variance (Low interest):** {var_low:.6f}")
    st.write(f"**Levene test p-value:** {lev_p:.4f}")

    if lev_p < 0.05:
        st.success("Conclusion: Return volatility is significantly different between the two groups.")
    else:
        st.warning("Conclusion: No significant difference in volatility between the two groups.")

    st.info("""
Why this test fits:
- The question is about variability, not mean.
- Levene's test is appropriate because it is more robust than a classical F-test.

Assumptions / limitation:
- Volatility differences do not imply causation.
- Other unobserved market events may also affect variance.
""")

elif test_choice == "Correlation analysis":
    st.subheader("Correlation Analysis: Is search interest associated with BTC daily return?")
    st.write(f"**Pearson correlation:** {corr_val:.4f}")
    st.write(f"**P-value:** {corr_p:.4f}")

    if corr_p < 0.05:
        st.success("Conclusion: There is a statistically significant linear relationship.")
    else:
        st.warning("Conclusion: No statistically significant linear relationship was detected.")

    st.info("""
Why this test fits:
- Both variables are quantitative.
- Pearson correlation measures linear association.

Assumptions / limitation:
- Sensitive to outliers.
- A weak or non-significant result may reflect small sample size or non-linear patterns.
""")

elif test_choice == "Chi-square test":
    st.subheader("Chi-square Test: Is positive return independent of search-interest group?")
    st.write("**Contingency table:**")
    st.dataframe(table, use_container_width=True)
    st.write(f"**P-value:** {chi2_p:.4f}")

    if chi2_p < 0.05:
        st.success("Conclusion: Positive return and search-interest group are associated.")
    else:
        st.warning("Conclusion: Positive return appears independent of search-interest group.")

    st.info("""
Why this test fits:
- Both variables are categorical.
- We are testing whether two categorical variables are independent.

Assumptions / limitation:
- Expected cell counts should be reasonably large.
- Small datasets can weaken chi-square reliability.
""")

# ---------------------------
# 5. Key Insight
# ---------------------------
st.header("5. Key Insight")

st.write("""
The most important result in this project is the variance comparison.

Although search interest did not significantly change the average return or the probability of a positive-return day,
higher search-interest periods showed significantly different volatility.
This suggests that public attention may be associated more with market uncertainty and larger swings than with predictable gains.
""")

# ---------------------------
# 6. Reflection / Limitations
# ---------------------------
st.header("6. Reflection / Limitations")

st.write("""
- The dataset covers a short time period.  
- Search interest is a normalized Google Trends score, not an absolute count.  
- The data supports association analysis, not causal claims.  
- Other market drivers were not included in the model.  
- Small sample size may reduce the power of some tests.
""")
