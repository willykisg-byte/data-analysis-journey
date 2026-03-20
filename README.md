# 📊 Sales Data Analysis Project

## 📌 Overview

This project analyzes sales data to uncover insights about revenue, profit, and product performance.

## 📁 Dataset

The dataset includes:

* Orders data
* Order details
* Sales targets

## 🧹 Data Cleaning

* Removed missing values
* Ensured consistent formatting

## 🤖 Machine Learning Model
Built a machine learning model to predict sales revenue.

### Improvements:
- Switched from Linear Regression to Random Forest
- Added feature engineering (Month extraction)
- Encoded categorical variables (Category & Sub-Category)

### Results:
- Initial profit prediction model performed poorly
- Reframed problem to revenue prediction
- Achieved 24% model accuracy (R² score)

### Insight:
Revenue is more predictable than profit due to lower variability.

## 📊 Key Insights

* Total Revenue: 431,502
* Total Profit: 23,955
* Clothing is the most profitable category
* Furniture is the least profitable category
* Highest sales come from Madhya Pradesh, especially Indore

## 📈 Visualization

The bar chart below shows profit by category:

![Profit Chart](outputs/profit_chart.png)

### Profit by Category
![Profit by Category](outputs/profit_by_category.png)

### Revenue by State
![Revenue by State](outputs/state_revenue.png)

### Monthly Sales Trend
![Monthly Sales Trend](outputs/monthly_sales.png)

## 💡 Business Recommendations

* Reduce operational costs to improve profit margins
* Focus on scaling Clothing category
* Improve marketing and pricing strategy for Furniture

## 🛠️ Tools Used

* Python
* Pandas
* Matplotlib

## 📊 Feature Importance

The chart below shows which factors most influence revenue prediction:

![Feature Importance](outputs/feature_importance.png)
## 🚀 Author

Willy Kisiang'ani
