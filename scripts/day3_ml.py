import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import joblib

# LOAD DATA
df_orders = pd.read_csv("../data/list of orders.csv")
df_details = pd.read_csv("../data/order details.csv")

# CLEAN DATA
df_orders = df_orders.dropna()

# MERGE DATA
df = pd.merge(df_orders, df_details, on="Order ID")

# CONVERT DATE
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# FEATURE ENGINEERING
df["Month"] = df["Order Date"].dt.month

# ENCODE CATEGORIES
df = pd.get_dummies(df, columns=["Category", "Sub-Category"], drop_first=True)

# SELECT FEATURES
X = df.drop(columns=["Profit", "Order ID", "CustomerName", "State", "City", "Order Date"])

# TARGET (WHAT YOU WANT TO PREDICT)
y = df["Profit"]

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# MODEL
model = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# PREDICTIONS
predictions = model.predict(X_test)

print("\n----- SAMPLE PREDICTIONS -----")
print(predictions[:10])

# ACCURACY
score = r2_score(y_test, predictions)

print("\n----- MODEL ACCURACY -----")
print(score)

# FEATURE IMPORTANCE (CORRECT VERSION)
features = X.columns
importances = model.feature_importances_

feat_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
})

feat_df = feat_df.sort_values(by="Importance", ascending=False).head(10)

print("\n----- FEATURE IMPORTANCE -----")
print(feat_df)

# PLOT
plt.figure(figsize=(10,5))
plt.bar(feat_df["Feature"], feat_df["Importance"])
plt.xticks(rotation=45)
plt.title("Top 10 Feature Importance")
plt.tight_layout()

# SAVE IMAGE
plt.savefig("../outputs/feature_importance.png")
plt.show()

# SAVE MODEL FOR DASHBOARD
joblib.dump(model, "../sales-dashboard-project/model/model.pkl")

print("✅ Model and feature importance saved successfully!")