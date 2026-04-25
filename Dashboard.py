import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("Sales_and_Customer_Data.xlsx")

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales & Customer Analytics Dashboard")

# =========================
# SIDEBAR FILTERS
# =========================
region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Product_Category"].unique(),
    default=df["Product_Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Product_Category"].isin(category))
]

# =========================
# DATASET VIEW
# =========================
st.subheader("Dataset View")
st.dataframe(filtered_df)

# =========================
# SUMMARY STATISTICS
# =========================
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# =========================
# CORRELATION HEATMAP
# =========================
st.subheader("Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include='number')
corr = numeric_df.corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# =========================
# SCATTER PLOT
# =========================
st.subheader("Scatter Plot (Quantity vs Total Sales)")

fig1 = px.scatter(
    filtered_df,
    x="Quantity",
    y="Total_Sales",
    color="Region",
    size="Unit_Price"
)
st.plotly_chart(fig1, use_container_width=True)

# =========================
# HISTOGRAM
# =========================
st.subheader("Histogram (Total Sales Distribution)")

fig2 = px.histogram(
    filtered_df,
    x="Total_Sales",
    nbins=20,
    color="Product_Category"
)
st.plotly_chart(fig2, use_container_width=True)

# =========================
# PAIRPLOT
# =========================
st.subheader("Pairplot (Numerical Features)")

pairplot_fig = sns.pairplot(numeric_df)
st.pyplot(pairplot_fig)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("Built with Streamlit")