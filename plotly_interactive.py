import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plotly_sales_trend(df):
    trend = df.groupby('Date')['Total_Sales'].sum().reset_index()
    fig = px.line(trend, x='Date', y='Total_Sales', title='Interactive Sales Trend', markers=True)
    fig.update_layout(template='plotly_white')
    return fig

def plotly_product_performance(df):
    perf = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(perf, x='Product', y='Total_Sales', color='Product', title='Product Performance (Interactive)')
    fig.update_layout(template='plotly_white')
    return fig

def plotly_customer_segmentation(df):
    fig = px.box(df, x='Loyalty_Segment', y='Total_Sales', color='Loyalty_Segment', 
                 title='Customer Segmentation Analysis', points="all")
    fig.update_layout(template='plotly_white')
    return fig

def plotly_regional_distribution(df):
    regional = df.groupby('Region')['Total_Sales'].sum().reset_index()
    fig = px.pie(regional, names='Region', values='Total_Sales', title='Sales Distribution by Region', hole=0.3)
    fig.update_layout(template='plotly_white')
    return fig

def plotly_price_vs_quantity(df):
    fig = px.scatter(df, x='Price', y='Quantity', color='Product', size='Total_Sales', 
                     hover_data=['Customer_ID', 'City'], title='Price vs Quantity (Bubble Chart)')
    fig.update_layout(template='plotly_white')
    return fig
