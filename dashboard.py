import streamlit as st
import pandas as pd
from data_preparation import load_and_prepare_data
from visualizations.seaborn_plots import *
from visualizations.plotly_interactive import *
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Interactive Sales Dashboard", layout="wide")

# Title and Branding
st.title("📊 Interactive Sales Dashboard")
st.markdown("---")

# Load data
@st.cache_data
def get_data():
    return load_and_prepare_data()

df = get_data()

# Sidebar filters
st.sidebar.header("Filter Options")
region_filter = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
segment_filter = st.sidebar.multiselect("Select Loyalty Segment", options=df['Loyalty_Segment'].unique(), default=df['Loyalty_Segment'].unique())

filtered_df = df[(df['Region'].isin(region_filter)) & (df['Loyalty_Segment'].isin(segment_filter))]

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['Total_Sales'].sum():,.2f}")
col2.metric("Total Orders", f"{len(filtered_df)}")
col3.metric("Avg Order Value", f"${filtered_df['Total_Sales'].mean():,.2f}")
col4.metric("Unique Customers", f"{filtered_df['Customer_ID'].nunique()}")

st.markdown("---")

# Visualizations Row 1
st.header("📈 Sales Trends & Product Performance")
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Interactive Sales Trend")
    st.plotly_chart(plotly_sales_trend(filtered_df), use_container_width=True)

with col_right:
    st.subheader("Product Performance")
    st.plotly_chart(plotly_product_performance(filtered_df), use_container_width=True)

st.markdown("---")

# Visualizations Row 2
st.header("👥 Customer Segmentation & Metrics")
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("Customer Loyalty Segmentation")
    st.plotly_chart(plotly_customer_segmentation(filtered_df), use_container_width=True)

with col_r:
    st.subheader("Regional Sales Distribution")
    st.plotly_chart(plotly_regional_distribution(filtered_df), use_container_width=True)

st.markdown("---")

# Row 3: Advanced Visualizations
st.header("🔍 Deeper Insights")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Price vs Quantity Insights")
    st.plotly_chart(plotly_price_vs_quantity(filtered_df), use_container_width=True)

with c2:
    st.subheader("Correlation Heatmap (Static)")
    set_style()
    fig_corr = plot_correlation_heatmap(filtered_df)
    st.pyplot(fig_corr)

st.markdown("---")
st.write("Dashboard created with Streamlit, Seaborn, and Plotly.")
