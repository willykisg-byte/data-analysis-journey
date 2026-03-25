import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sales.db")

# Query 1: View all data
df = pd.read_sql("SELECT * FROM sales", conn)
print("\n--- ALL DATA ---")
print(df)

# Query 2: Total Sales
total_sales = pd.read_sql("SELECT SUM(Sales) as Total_Sales FROM sales", conn)
print("\n--- TOTAL SALES ---")
print(total_sales)

# Query 3: Profit by Category
profit_category = pd.read_sql("""
SELECT Category, SUM(Profit) as Total_Profit
FROM sales
GROUP BY Category
""", conn)

print("\n--- PROFIT BY CATEGORY ---")
print(profit_category)

# Query 4: Monthly Sales
monthly_sales = pd.read_sql("""
SELECT strftime('%m', "Order Date") as Month, SUM(Sales) as Total_Sales
FROM sales
GROUP BY Month
""", conn)

print("\n--- MONTHLY SALES ---")
print(monthly_sales)