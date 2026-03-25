import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(__file__)

# LOAD DATA
data_path = os.path.join(BASE_DIR, "data", "sales.csv")
df = pd.read_csv(data_path)

# LOAD MODEL
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
model = joblib.load(model_path)


# PAGE CONFIG
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# TITLE
st.title("📊 Sales Profit Predictor")
st.markdown("### Predict business profit using machine learning")

# DIVIDER
st.markdown("---")

# CREATE COLUMNS
col1, col2 = st.columns(2)

# INPUT SECTION
with col1:
    st.subheader("📝 Input Data")

    amount = st.number_input("💰 Sales Amount", min_value=0.0)
    quantity = st.number_input("📦 Quantity", min_value=1)
    month = st.slider("📅 Month", 1, 12)

    category = st.selectbox("🏷️ Category", ["Furniture", "Electronics"])
    sub_category = st.selectbox("📂 Sub-Category", [
        "Chairs", "Tables", "Phones", "Bookcases"
    ])

# PREDICTION SECTION
with col2:
    st.subheader("🤖 Prediction Result")

    if st.button("Predict Profit"):

        input_data = pd.DataFrame({
            "Amount": [amount],
            "Quantity": [quantity],
            "Month": [month],
            "Category_Furniture": [1 if category == "Furniture" else 0],
            "Category_Electronics": [1 if category == "Electronics" else 0],
            "Sub-Category_Chairs": [1 if sub_category == "Chairs" else 0],
            "Sub-Category_Tables": [1 if sub_category == "Tables" else 0],
            "Sub-Category_Phones": [1 if sub_category == "Phones" else 0],
            "Sub-Category_Bookcases": [1 if sub_category == "Bookcases" else 0],
        })

        # MATCH MODEL FEATURES
        model_features = model.feature_names_in_

        for col in model_features:
            if col not in input_data.columns:
                input_data[col] = 0

        input_data = input_data[model_features]

        prediction = model.predict(input_data)

        st.success(f"💰 Predicted Profit: {prediction[0]:.2f}")

# FOOTER
st.markdown("---")
st.caption("Built with Python, Machine Learning & Streamlit")

st.markdown("---")
st.subheader("📊 Sales Dashboard")

# TOTAL SALES
st.metric("💰 Total Revenue", f"{df['Amount'].sum():,.0f}")

# TOTAL PROFIT
st.metric("📈 Total Profit", f"{df['Profit'].sum():,.0f}")

category_sales = df.groupby("Category")["Amount"].sum()

st.bar_chart(category_sales)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month

monthly_profit = df.groupby("Month")["Profit"].sum()

st.line_chart(monthly_profit)

top_products = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).head(5)

st.bar_chart(top_products)