import pandas as pd

# -----------------------------
# STEP 1: Create Dataset
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, None],
    "Salary": [50000, 60000, None, 80000, 90000]
}

# -----------------------------
# STEP 2: Convert to DataFrame
# -----------------------------
df = pd.DataFrame(data)

# -----------------------------
# STEP 3: View Original Data
# -----------------------------
print("----- ORIGINAL DATA -----")
print(df)

# -----------------------------
# STEP 4: Explore Data
# -----------------------------
print("\n----- DATA INFO -----")
print(df.info())

print("\n----- DATA DESCRIPTION -----")
print(df.describe())

# -----------------------------
# STEP 5: Clean Data
# -----------------------------
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# -----------------------------
# STEP 6: View Cleaned Data
# -----------------------------
print("\n----- CLEANED DATA -----")
print(df)

# -----------------------------
# STEP 7: Basic Analysis
# -----------------------------
print("\n----- ANALYSIS -----")
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())