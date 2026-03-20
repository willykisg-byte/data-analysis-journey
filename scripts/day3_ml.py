import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

# LOAD DATA (FIXED PATHS)
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
X = df.drop(columns=["Amount", "Profit", "Order ID", "CustomerName", "State", "City", "Order Date"])

# TARGET
y = df["Amount"]

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# MODEL (UPGRADED)
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

# FEATURE IMPORTANCE
import matplotlib.pyplot as plt

importance = model.feature_importances_
features = X.columns

feature_importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

print("\n----- FEATURE IMPORTANCE -----")
print(feature_importance_df.head(10))

feature_importance_df.head(10).plot(
    kind="bar",
    x="Feature",
    y="Importance",
    title="Top 10 Important Features"
)

plt.tight_layout()
plt.savefig("../outputs/feature_importance.png")
plt.show()