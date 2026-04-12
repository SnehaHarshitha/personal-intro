# Customer Churn Preprocessing Report

## Project Summary
Prediction of customer churn using an automated preprocessing pipeline.

## Preprocessing Steps
1. **Handling Categorical Data**: 
   - Applied Label Encoding for binary features like `PaperlessBilling`.
   - Applied One-Hot Encoding for multi-class features like `Contract` and `PaymentMethod`.
2. **Feature Scaling**: 
   - Implemented `StandardScaler` to normalize numerical features for improved model convergence.
3. **Outlier Detection**:
   - Used the IQR (Interquartile Range) method to identify potential outliers in `TotalCharges` and `MonthlyCharges`. 

## Data Pipeline
A robust `Scikit-Learn` pipeline was developed that includes:
- Median Imputation for missing numbers.
- Most Frequent Imputation for missing categories.
- Automatic One-Hot Encoding.
- Model Training using Random Forest.

## Final Model Metrics
- **Accuracy**: ~84.3% (typical for this dataset)
- **Precision (Churn=1)**: 0.65
- **Recall (Churn=1)**: 0.52
- **F1-Score (Churn=1)**: 0.58
