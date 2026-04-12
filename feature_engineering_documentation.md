# Feature Engineering Documentation

## 1. Tenure Group
Created bins for `Tenure` (Short, Medium, Long, Very Long) to allow the model to catch non-linear patterns.

## 2. Charge Ratio
`MonthlyCharges` / `TotalCharges`. This captures whether a customer is paying more per month relative to their overall relationship.

## 3. High Value Flag
A binary feature identifying customers with both high `MonthlyCharges` and high `Tenure`.

## 4. Payment Method Frequency
Using Frequency Encoding on the `PaymentMethod` to capture its overall market share in the customer base.

## 5. Senior-Contract Interaction
`SeniorCitizen` * `Contract`. This captures whether being a senior citizen impacts the likelihood of signing long-term contracts.

## 6. Average Cost Per Month (Engineered in Model)
`TotalCharges / (Tenure + 1)` which is a refined version of Monthly Charges.
