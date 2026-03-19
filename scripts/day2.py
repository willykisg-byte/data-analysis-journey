import pandas as pd

# LOAD FIRST DATASET
df = pd.read_csv("list of orders.csv")

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
df_details = pd.read_csv("order details.csv")

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

import matplotlib.pyplot as plt

merged_df.groupby("Category")["Profit"].sum().plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()