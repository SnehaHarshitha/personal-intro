import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def set_style():
    sns.set_theme(style="whitegrid", palette="viridis")
    plt.rcParams['figure.figsize'] = (10, 6)

def plot_sales_trend(df):
    plt.figure()
    trend = df.groupby('Date')['Total_Sales'].sum().reset_index()
    sns.lineplot(data=trend, x='Date', y='Total_Sales', marker='o')
    plt.title('Daily Sales Trend', fontsize=15)
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

def plot_product_performance(df):
    plt.figure()
    perf = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(data=perf, x='Product', y='Total_Sales', hue='Product', legend=False)
    plt.title('Total Sales by Product', fontsize=15)
    plt.xlabel('Product')
    plt.ylabel('Total Sales ($)')
    plt.tight_layout()
    return plt.gcf()

def plot_customer_segmentation(df):
    plt.figure()
    sns.boxplot(data=df, x='Loyalty_Segment', y='Total_Sales', hue='Loyalty_Segment')
    plt.title('Sales Distribution by Loyalty Segment', fontsize=15)
    plt.xlabel('Loyalty Segment')
    plt.ylabel('Total Sales ($)')
    plt.tight_layout()
    return plt.gcf()

def plot_price_vs_quantity(df):
    plt.figure()
    sns.scatterplot(data=df, x='Price', y='Quantity', hue='Product', style='Region', s=100)
    plt.title('Price vs Quantity by Product and Region', fontsize=15)
    plt.xlabel('Price ($)')
    plt.ylabel('Quantity')
    plt.tight_layout()
    return plt.gcf()

def plot_correlation_heatmap(df):
    plt.figure()
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Matrix of Sales Metrics', fontsize=15)
    plt.tight_layout()
    return plt.gcf()

if __name__ == "__main__":
    from data_preparation import load_and_prepare_data
    df = load_and_prepare_data()
    set_style()
    
    # Save test plots
    plot_sales_trend(df).savefig('visualizations/sales_trend.png')
    plot_product_performance(df).savefig('visualizations/product_performance.png')
    plot_customer_segmentation(df).savefig('visualizations/customer_segmentation.png')
    plot_price_vs_quantity(df).savefig('visualizations/price_vs_quantity.png')
    plot_correlation_heatmap(df).savefig('visualizations/correlation_heatmap.png')
    print("Seaborn Plots Generated in visualizations/ folder.")
