# Capstone Project: Real-World Business Analysis
## Retention Roadmap: Optimizing Customer Lifecycle in Subscription Services

### 🚀 Overview
This repository contains a full end-to-end data analysis project focusing on **Customer Churn**. It covers everything from data collection and cleaning to advanced statistical modeling and business strategy implementation.

### 📁 Project Structure
- `data/`: Raw and cleaned datasets.
- `notebooks/`: Source scripts for Data Cleaning, EDA, and Advanced Analysis.
- `reports/`: Executive Summary (PDF), Technical Report (PDF), and Visualizations.
- `presentations/`: Business Presentation (PPTX).
- `portfolio/`: High-quality web-based portfolio of findings.
- `generate_reports.py`: Automated tool to generate PDFs and PPTX using Python.

### 🛠️ Technical Stack
- **Languages**: Python 3.x, HTML/CSS
- **Libraries**: Pandas, Seaborn, Matplotlib, SciPy, Statsmodels, FPDF (PDF Gen), Python-PPTX (PPTX Gen)
- **Methods**: T-Tests, Chi-Square Analysis, Logistic Regression.

### 📈 Key Insights
1. **Contract Strategy**: Month-to-month contracts are at a 4x higher risk compared to annual plans.
2. **The 90-Day Window**: Customer churn is highest in the first 3 months of tenure.
3. **Price Sensitivity**: High monthly charges without value-added service engagement lead to attrition.

### 📋 Setup & Reproduction
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run data cleaning:
   ```bash
   python notebooks/1_data_cleaning.py
   ```
3. Perform analysis and generate visuals:
   ```bash
   python notebooks/3_analysis.py
   ```
4. Generate reports:
   ```bash
   python generate_reports.py
   ```

### 🤝 Contact
Developed as part of the 2-Month Data Science Learning Journey - Week 8 Capstone.
