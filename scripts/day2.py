import pandas as pd
import matplotlib.pyplot as plt

# LOAD FIRST DATASET
df = pd.read_csv("data/list of orders.csv")

print("----- FIRST 5 ROWS -----")
print(df.head())

print("\n----- COLUMN NAMES -----")
print(df.columns)

print("\n----- DATA INFO -----")
print(df.info())

print("\n----- DATA DESCRIPTION -----")
print(df.describe())

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# REMOVE MISSING DATA
df = df.dropna()

print("\n----- CLEANED DATA INFO -----")
print(df.info())

print("\n----- TOP STATES -----")
print(df["State"].value_counts())

print("\n----- TOP CITIES -----")
print(df["City"].value_counts().head(5))

print("\n----- ORDERS FROM MADHYA PRADESH -----")
print(df[df["State"] == "Madhya Pradesh"])

# LOAD ORDER DETAILS
df_details = pd.read_csv("data/order details.csv")

print("\n----- ORDER DETAILS -----")
print(df_details.head())

print("\n----- DETAILS COLUMNS -----")
print(df_details.columns)

# MERGE DATASETS
merged_df = pd.merge(df, df_details, on="Order ID")

print("\n----- MERGED DATA -----")
print(merged_df.head())

print("\n----- TOTAL REVENUE -----")
print(merged_df["Amount"].sum())

print("\n----- TOTAL PROFIT -----")
print(merged_df["Profit"].sum())

print("\n----- TOP CATEGORIES -----")
print(merged_df["Category"].value_counts())

print("\n----- PROFIT BY CATEGORY -----")
print(merged_df.groupby("Category")["Profit"].sum())

# BAR CHART - PROFIT BY CATEGORY
merged_df.groupby("Category")["Profit"].sum().plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.savefig("outputs/profit_by_category.png")
plt.show()

# REVENUE BY STATE
print("\n----- REVENUE BY STATE -----")
state_revenue = merged_df.groupby("State")["Amount"].sum()
print(state_revenue.sort_values(ascending=False))

state_revenue.sort_values(ascending=False).head(10).plot(kind="bar")

plt.title("Top 10 States by Revenue")
plt.xlabel("State")
plt.ylabel("Revenue")

plt.savefig("outputs/state_revenue.png")
plt.show()

# SALES OVER TIME
merged_df["Order Date"] = pd.to_datetime(merged_df["Order Date"], dayfirst=True)

print("\n----- SALES OVER TIME -----")
monthly_sales = merged_df.groupby(merged_df["Order Date"].dt.to_period("M"))["Amount"].sum()
print(monthly_sales)

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.savefig("outputs/monthly_sales.png")
plt.show()