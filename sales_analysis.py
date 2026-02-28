import pandas as pd
import os

# --- Day 2: Explore Data ---
def explore_data(df):
    print("--- Data Exploration ---")
    print(f"Shape: {df.shape}")
    print("\nColumns and Data Types:")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())
    print("-" * 30)

# --- Day 3: Clean Data ---
def clean_data(df):
    print("\n--- Data Cleaning ---")
    # Check for missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Handle missing values: Fill Quantity with 1 (default)
    df['Quantity'] = df['Quantity'].fillna(1)
    
    # Handle missing values: Dropping rows with any other crucial missing data if applicable
    # In this case, we only had Quantity missing.
    
    # Remove duplicates
    initial_count = len(df)
    df = df.drop_duplicates()
    if len(df) < initial_count:
        print(f"Removed {initial_count - len(df)} duplicate rows.")
    
    print("Data cleaning complete.")
    print("-" * 30)
    return df

# --- Day 4: Analyze Sales ---
def analyze_sales(df):
    print("\n--- Sales Analysis ---")
    # Calculate Revenue for each row (verify Total_Sales if present, or just use it)
    if 'Total_Sales' in df.columns:
        df['Revenue'] = df['Total_Sales']
    else:
        df['Revenue'] = df['Quantity'] * df['Price']
    
    # Metric 1: Total Revenue
    total_revenue = df['Revenue'].sum()
    
    # Metric 2: Best Selling Product (by Quantity)
    best_product = df.groupby('Product')['Quantity'].sum().idxmax()
    best_product_qty = df.groupby('Product')['Quantity'].sum().max()
    
    # Metric 3: Region Performance (Total Revenue per Region)
    # Using 'Region' as 'Category' is no longer present in the new dataset
    group_col = 'Region' if 'Region' in df.columns else 'Category'
    group_revenue = df.groupby(group_col)['Revenue'].sum()
    
    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Best Selling Product: {best_product} ({best_product_qty} units)")
    print(f"\nRevenue by {group_col}:")
    print(group_revenue)
    print("-" * 30)
    
    return total_revenue, best_product, group_revenue, group_col

# --- Day 5: Create Report ---
def create_report(total_revenue, best_product, group_revenue, group_col):
    report_content = f"""# Sales Analysis Report
Generated automatically using Pandas.

## Key Metrics
- **Total Revenue**: ₹{total_revenue:,.2f}
- **Best Selling Product**: {best_product}
- **Top {group_col}**: {group_revenue.idxmax()} (₹{group_revenue.max():,.2f})

## Performance by {group_col}
| {group_col} | Total Revenue |
|----------|---------------|
"""
    for group, rev in group_revenue.items():
        report_content += f"| {group} | ₹{rev:,.2f} |\n"
        
    report_path = 'analysis_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\nReport saved to {report_path}")

def main():
    # Load Data
    file_path = 'sales_data (2).csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return
        
    df = pd.read_csv(file_path)
    
    explore_data(df)
    df = clean_data(df)
    total_rev, best_prod, group_rev, group_col = analyze_sales(df)
    create_report(total_rev, best_prod, group_rev, group_col)

if __name__ == "__main__":
    main()
