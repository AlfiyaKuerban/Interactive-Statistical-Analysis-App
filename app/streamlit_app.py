import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import pearsonr, chi2_contingency, levene

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Bitcoin Returns and Google Search Interest",
    layout="wide"
)

# ---------------------------
# Load data
# ---------------------------
df = pd.read_csv("data/gold/final_dataset.csv")
df["date"] = pd.to_datetime(df["date"])

# ---------------------------
# Prepare variables
# ---------------------------
returns = df["btc_daily_return"]
high = df[df["high_interest"] == 1]["btc_daily_return"]
low = df[df["high_interest"] == 0]["btc_daily_return"]

# One-sample t-test
t1_stat, t1_p = stats.ttest_1samp(returns, 0)

# Two-sample t-test
t2_stat, t2_p = stats.ttest_ind(high, low)

# Variance comparison
var_high = high.var()
var_low = low.var()
lev_stat, lev_p = levene(high, low)

# Correlation
corr_val, corr_p = pearsonr(df["search_interest"], df["btc_daily_return"])

# Chi-square
table = pd.crosstab(df["positive_return"], df["high_interest"])
chi2_stat, chi2_p, dof, expected = chi2_contingency(table)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("Dashboard Navigation")
section = st.sidebar.radio(
    "Go to section",
    [
        "Overview",
        "Data Preview",
        "Visual Story",
        "Hypothesis Testing",
        "Key Insight",
        "Limitations"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Dataset: final_dataset.csv")
st.sidebar.write("External source: Google Trends")
st.sidebar.write("Join key: date")

# ---------------------------
# Title
# ---------------------------
st.title("Bitcoin Returns and Google Search Interest")
st.caption("Assignment 4 — Interactive Statistical Analysis App")

# ---------------------------
# Overview
# ---------------------------
if section == "Overview":
    st.header("1. Project Overview")

    st.write("""
This project extends the Assignment 3 Bitcoin pipeline by adding Google Trends as a new external data source.

The goal is to explore whether public search interest in Bitcoin is associated with:
- daily returns
- volatility
- and positive-return behavior
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

    st.subheader("Main Research Questions")
    st.write("""
1. Is the average Bitcoin return different from 0?  
2. Do returns differ between high and low search-interest days?  
3. Is positive return independent of search-interest level?  
4. Is volatility different between high and low search-interest days?  
5. Is search interest associated with Bitcoin returns?
""")

    st.subheader("Quick Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Rows", len(df))
    m2.metric("Mean Return", f"{df['btc_daily_return'].mean():.4f}")
    m3.metric("Avg Search Interest", f"{df['search_interest'].mean():.1f}")
    m4.metric("Positive Return Rate", f"{df['positive_return'].mean():.0%}")

# ---------------------------
# Data Preview
# ---------------------------
elif section == "Data Preview":
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
- **high_interest**: 1 if search interest is above the median, otherwise 0
""")

# ---------------------------
# Visual Story
# ---------------------------
elif section == "Visual Story":
    st.header("3. Visual Storytelling")
    st.write("These charts are designed to support the statistical analyses shown later.")

    # Row 1
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("3.1 BTC Daily Returns Over Time")
        st.line_chart(df.set_index("date")["btc_daily_return"])
        st.caption("This chart shows how returns fluctuate over time and supports the one-sample t-test.")

    with col2:
        st.subheader("3.2 Returns by Search-Interest Group")
        fig1, ax1 = plt.subplots(figsize=(5, 3.5))
        ax1.boxplot([low.dropna(), high.dropna()], labels=["Low Interest", "High Interest"])
        ax1.set_ylabel("BTC Daily Return")
        ax1.set_title("Distribution of Returns by Search Interest")
        st.pyplot(fig1)
        st.caption("This chart supports the two-sample t-test and variance comparison.")

    # Row 2
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("3.3 Search Interest vs BTC Return")
        fig2, ax2 = plt.subplots(figsize=(5, 3.5))
        ax2.scatter(df["search_interest"], df["btc_daily_return"])
        ax2.set_xlabel("Search Interest")
        ax2.set_ylabel("BTC Daily Return")
        ax2.set_title("Search Interest and BTC Return")
        st.pyplot(fig2)
        st.caption("This chart supports the correlation analysis.")

    with col4:
        st.subheader("3.4 Positive Return Count by Search-Interest Group")
        count_table = pd.crosstab(df["high_interest"], df["positive_return"])
        st.bar_chart(count_table)
        st.caption("This chart supports the chi-square test of independence.")

# ---------------------------
# Hypothesis Testing
# ---------------------------
elif section == "Hypothesis Testing":
    st.header("4. Hypothesis Testing")

    test_choice = st.selectbox(
        "Select a test",
        [
            "1. One-sample t-test",
            "2. Two-sample t-test",
            "3. Chi-square test",
            "4. Variance comparison",
            "5. Correlation analysis"
        ]
    )

    if test_choice == "1. One-sample t-test":
        st.subheader("One-sample t-test")
        st.write("**Question:** Is the average Bitcoin daily return different from 0?")
        st.write("**Null hypothesis:** Mean BTC return = 0")
        st.write("**Alternative hypothesis:** Mean BTC return ≠ 0")
        st.write(f"**T-statistic:** {t1_stat:.4f}")
        st.write(f"**P-value:** {t1_p:.4f}")

        if t1_p < 0.05:
            st.success("Conclusion: The average BTC return is significantly different from 0.")
        else:
            st.warning("Conclusion: The average BTC return is not significantly different from 0.")

        st.info("""
Why this test fits:
- BTC daily return is numeric.
- We compare one sample mean to a fixed value.

Assumptions / limitation:
- Assumes observations are reasonably independent.
- Small sample size may reduce reliability.
""")

    elif test_choice == "2. Two-sample t-test":
        st.subheader("Two-sample t-test")
        st.write("**Question:** Do returns differ between high and low search-interest days?")
        st.write("**Null hypothesis:** Mean returns are equal")
        st.write("**Alternative hypothesis:** Mean returns are different")
        st.write(f"**T-statistic:** {t2_stat:.4f}")
        st.write(f"**P-value:** {t2_p:.4f}")

        if t2_p < 0.05:
            st.success("Conclusion: Returns differ significantly between groups.")
        else:
            st.warning("Conclusion: No significant difference in returns between groups.")

        st.info("""
Why this test fits:
- BTC daily return is numeric.
- high_interest creates two independent groups.

Assumptions / limitation:
- Assumes observations are reasonably independent.
- Small sample size may reduce statistical power.
""")

    elif test_choice == "3. Chi-square test":
        st.subheader("Chi-square Test of Independence")
        st.write("**Question:** Is positive return independent of search-interest group?")
        st.write("**Null hypothesis:** positive_return and high_interest are independent")
        st.write("**Alternative hypothesis:** They are associated")

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
- We are testing independence between two categorical variables.

Assumptions / limitation:
- Expected counts should be reasonably large.
- Small sample size can weaken reliability.
""")

    elif test_choice == "4. Variance comparison":
        st.subheader("Variance Comparison")
        st.write("**Question:** Is volatility different between high and low search-interest days?")
        st.write(f"**Variance (High interest):** {var_high:.6f}")
        st.write(f"**Variance (Low interest):** {var_low:.6f}")
        st.write(f"**Levene test p-value:** {lev_p:.4f}")

        if lev_p < 0.05:
            st.success("Conclusion: Volatility is significantly different between the two groups.")
        else:
            st.warning("Conclusion: No significant difference in volatility between the two groups.")

        st.info("""
Why this test fits:
- The question is about variability, not the mean.
- Levene's test is robust and suitable for financial return data.

Assumptions / limitation:
- Significant variance does not imply causation.
- Other market events may also influence volatility.
""")

    elif test_choice == "5. Correlation analysis":
        st.subheader("Correlation Analysis")
        st.write("**Question:** Is search interest associated with BTC daily return?")
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
- A weak result may reflect small sample size or non-linear patterns.
""")

# ---------------------------
# Key Insight
# ---------------------------
elif section == "Key Insight":
    st.header("5. Key Insight")

    st.write("""
The most important result in this project is the variance comparison.

Although search interest did not significantly change average returns or the probability of a positive-return day,
it was associated with significantly different volatility.

In simple terms, when more people are searching about Bitcoin, the market becomes more unstable,
even if the average return does not change much.
""")

# ---------------------------
# Limitations
# ---------------------------
elif section == "Limitations":
    st.header("6. Reflection / Limitations")

    st.write("""
- The dataset covers a short time period.  
- Google Trends values are normalized scores, not absolute search counts.  
- The analysis shows association, not causation.  
- Other market factors were not included.  
- Small sample size may reduce the strength of some conclusions.
""")