import pandas as pd
import sqlite3

# Load your dataset
df = pd.read_csv("data/sales.csv")

# Create database
conn = sqlite3.connect("sales.db")

# Save to SQL
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")