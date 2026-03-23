# Project Documentation: Interactive Sales Dashboard

## 1. Introduction
The **Interactive Sales Dashboard** is a comprehensive visual analytics tool developed to assist sales teams in monitoring key performance indicators (KPIs), analyzing trends, and understanding customer behavior.

## 2. Project Structure
```text
Interactive_Sales_Dashboard/
├── dashboard.py               # Main Streamlit application
├── dashboard.ipynb            # Jupyter Notebook for analysis
├── data_preparation.py        # Data cleaning and merging script
├── requirements.txt           # List of dependencies
├── README.md                  # Project overview and setup instructions
├── visualizations/            # Modular visualization folder
│   ├── seaborn_plots.py       # Static statistical plots
│   └── plotly_interactive.py  # Interactive Plotly charts
├── dashboard_demo.gif         # Visual demonstration
└── Interactive_Sales_Dashboard_Report.docx # Professional Report
```

## 3. Data Processing
The dashboard uses two primary data sources:
- `sales_data.csv`: Transactional records containing dates, products, prices, and quantities.
- `customer_data.csv`: Demographic and loyalty segmentation data.

These are merged on `Customer_ID` to provide a holistic view of sales performance by customer segment.

## 4. Visualizations
### 4.1 Sales Trend (Interactive)
Uses a Line Chart to show daily revenue. Allows users to zoom into specific time periods.

### 4.2 Product Performance (Bar Chart)
Identifies which products contribute most to the total revenue.

### 4.3 Customer Segmentation (Box Plot)
Displays the distribution of sale amounts across 'Loyal', 'Premium', 'Standard', and 'New' segments to identify high-value customer groups.

### 4.4 Regional Sales (Donut Chart)
A breakdown of total sales by geographic region (North, South, East, West).

### 4.5 Correlation Heatmap (Static)
Interprets the relationship between numerical variables like Price, Quantity, and Total Sales.

## 5. Usage
To run the dashboard:
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Launch the Streamlit app: `streamlit run dashboard.py`
3. Access the dashboard at `http://localhost:8501`.
