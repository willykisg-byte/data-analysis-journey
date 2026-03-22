import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("scripts/model.pkl")

# Title
st.set_page_config(page_title="Profit Predictor", layout="centered")

st.title("📊 Profit Prediction App")
st.markdown("Predict profit based on sales data")

# Inputs
st.subheader("Enter Order Details")

amount = st.number_input("💰 Order Amount", min_value=0.0, value=100.0)
quantity = st.number_input("📦 Quantity", min_value=1, value=1)
month = st.slider("📅 Month", 1, 12, 1)

category = st.selectbox("🏷️ Category", ["Clothing", "Electronics", "Furniture"])

# Encode category (match your training)
if category == "Clothing":
    cat_val = 0
elif category == "Electronics":
    cat_val = 1
else:
    cat_val = 2

# Prediction button
if st.button("🔮 Predict Profit"):

    features = np.array([[amount, quantity, month, cat_val]])
    prediction = model.predict(features)[0]

    st.subheader("📈 Prediction Result")

    # Styling output
    if prediction >= 0:
        st.success(f"💵 Estimated Profit: ${prediction:.2f}")
    else:
        st.error(f"📉 Estimated Loss: ${prediction:.2f}")