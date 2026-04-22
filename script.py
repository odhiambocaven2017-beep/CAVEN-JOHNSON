#Install requirements
#pip install streamlit pandas scikit-learn plotly

#Streamlit dashboard code
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import plotly.express as px

# Load Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target
df["species"] = df["species"].map(dict(enumerate(iris.target_names)))

# Streamlit App Title
st.set_page_config(page_title="Iris Dashboard", layout="wide")
st.title("Iris Dataset Interactive Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")

species_filter = st.sidebar.multiselect(
    "Select Species",
    options=df["species"].unique(),
    default=df["species"].unique()
)

filtered_df = df[df["species"].isin(species_filter)]

# Show Data
st.subheader("Dataset Preview")
st.dataframe(filtered_df)

# Basic Statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Scatter Plot
st.subheader("Scatter Plot")

x_axis = st.selectbox("X-axis", df.columns[:-1])
y_axis = st.selectbox("Y-axis", df.columns[:-1], index=1)

fig_scatter = px.scatter(
    filtered_df,
    x=x_axis,
    y=y_axis,
    color="species",
    title=f"{x_axis} vs {y_axis}"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# Histogram
st.subheader("Histogram")

feature = st.selectbox("Select Feature", df.columns[:-1], key="hist")

fig_hist = px.histogram(
    filtered_df,
    x=feature,
    color="species",
    marginal="box",
    nbins=20,
    title=f"Distribution of {feature}"
)

st.plotly_chart(fig_hist, use_container_width=True)

# Correlation Heatmap
st.subheader("Correlation Heatmap")

corr = filtered_df.iloc[:, :-1].corr()

fig_heatmap = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Viridis",
    title="Feature Correlation Heatmap"
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# Pair Plot
st.subheader("Pair Plot")

fig_pair = px.scatter_matrix(
    filtered_df,
    dimensions=df.columns[:-1],
    color="species",
    title="Pairwise Feature Relationships"
)

st.plotly_chart(fig_pair, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built using Streamlit")
#In the terminal, run
#streamlit run script.py
