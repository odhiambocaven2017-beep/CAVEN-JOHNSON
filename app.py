import streamlit as st
import pandas as pd
import plotly.express as px

# Sample Data
df = pd.DataFrame({
    "Customer_ID": [1,2,3,4,5,6,7,8],
    "Name": ["Asha","John","Peter","Mary","James","Grace","Kevin","Linda"],
    "Age": [23,35,29,40,31,27,22,36],
    "Gender": ["F","M","M","F","M","F","M","F"],
    "Purchase_Amount": [200,450,300,700,150,500,220,600],
    "Purchase_Date": pd.date_range("2025-01-01", periods=8)
})

# App setup
st.set_page_config(page_title="Customer Dashboard", layout="wide")
st.title("Customer Analytics Dashboard")

# Sidebar filter
gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[df["Gender"].isin(gender)]

# Data
st.subheader("Dataset")
st.dataframe(filtered_df)

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Customers", filtered_df["Customer_ID"].nunique())
col2.metric("Total Revenue", filtered_df["Purchase_Amount"].sum())
col3.metric("Avg Spend", round(filtered_df["Purchase_Amount"].mean(), 2))

# Scatter
st.subheader("Age vs Purchase Amount")
fig1 = px.scatter(filtered_df, x="Age", y="Purchase_Amount", color="Gender")
st.plotly_chart(fig1, use_container_width=True)

# Bar comparison
st.subheader("Gender Comparison")
fig2 = px.bar(df, x="Gender", y="Purchase_Amount", color="Gender", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# Trend
st.subheader("Sales Trend")
fig3 = px.line(df, x="Purchase_Date", y="Purchase_Amount", markers=True)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.markdown("Built using Streamlit")