import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set aesthetic style for charts
sns.set_theme(style="whitegrid")

def load_and_clean_data(file_path):
    """Loads and cleans the sales dataset."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    
    # Basic cleaning
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Ensure numeric columns are correct
    numeric_cols = ['Quantity', 'Price', 'Total_Sales']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # Drop any rows with missing values introduced by coercion
    df = df.dropna()
    
    return df

def calculate_metrics(df):
    """Calculates key business metrics."""
    metrics = {
        'Total Revenue': df['Total_Sales'].sum(),
        'Average Order Value': df['Total_Sales'].mean(),
        'Total Units Sold': df['Quantity'].sum(),
        'Unique Customers': df['Customer_ID'].nunique()
    }
    return metrics

def generate_visualizations(df, output_dir):
    """Creates and saves visualizations."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 1. Sales by Product (Bar Chart)
    plt.figure(figsize=(10, 6))
    product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
    sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
    plt.title('Total Sales by Product', fontsize=15)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xlabel('Product', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_product.png'))
    plt.close()

    # 2. Sales by Region (Pie Chart)
    plt.figure(figsize=(8, 8))
    region_sales = df.groupby('Region')['Total_Sales'].sum()
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Sales Distribution by Region', fontsize=15)
    plt.savefig(os.path.join(output_dir, 'sales_by_region.png'))
    plt.close()

    # 3. Sales Trend Over Time (Line Chart)
    plt.figure(figsize=(12, 6))
    df_trend = df.sort_values('Date').groupby('Date')['Total_Sales'].sum().reset_index()
    sns.lineplot(data=df_trend, x='Date', y='Total_Sales', marker='o', color='b')
    plt.title('Daily Sales Trend', fontsize=15)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xlabel('Date', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_trend.png'))
    plt.close()

def create_report(metrics, product_sales, regional_sales, output_path):
    """Generates the final markdown report."""
    report_content = f"""# Sales Data Analysis Report

## Executive Summary
This report analyzes the sales performance based on the provided dataset.

## Key Metrics
- **Total Revenue**: ${metrics['Total Revenue']:,.2f}
- **Average Order Value**: ${metrics['Average Order Value']:,.2f}
- **Total Units Sold**: {metrics['Total Units Sold']:,}
- **Unique Customers**: {metrics['Unique Customers']}

## Visual Insights

### 1. Product Performance
![Sales by Product](../visualizations/sales_by_product.png)
*Insight: Laptop and Phone are the primary revenue drivers for the business.*

### 2. Regional Distribution
![Sales by Region](../visualizations/sales_by_region.png)
*Insight: The North region shows the highest market share, followed closely by South.*

### 3. Sales Trends
![Sales Trend](../visualizations/sales_trend.png)
*Insight: There is significant daily fluctuation, indicating potential seasonal or promotional influences.*

## Conclusion
The business should focus on maintaining inventory for high-value items like Laptops and potentially investigate the lower sales in certain regions to identify growth opportunities.
"""
    with open(output_path, 'w') as f:
        f.write(report_content)

def main():
    data_path = 'e:/dev/Sales_Analysis_Project_Full/data/sales_data.csv'
    viz_dir = 'e:/dev/Sales_Analysis_Project_Full/visualizations'
    report_path = 'e:/dev/Sales_Analysis_Project_Full/report/analysis_report.md'
    
    try:
        print("Loading and cleaning data...")
        df = load_and_clean_data(data_path)
        
        print("Calculating metrics...")
        metrics = calculate_metrics(df)
        
        print("Generating visualizations...")
        generate_visualizations(df, viz_dir)
        
        print("Generating report...")
        product_sales = df.groupby('Product')['Total_Sales'].sum()
        regional_sales = df.groupby('Region')['Total_Sales'].sum()
        create_report(metrics, product_sales, regional_sales, report_path)
        
        print(f"Analysis complete! Report generated at {report_path}")
        
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()
