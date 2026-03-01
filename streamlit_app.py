import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Model & Assets
# -----------------------------
model = joblib.load("impulse_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Impulse Risk Detector", layout="wide")

st.title("💳 Financial Impulse Behaviour Detection")
st.write("Predict impulsive spending behaviour based on user patterns.")

# -----------------------------
# User Inputs
# -----------------------------
st.sidebar.header("User Behaviour Inputs")

total_transactions = st.sidebar.slider("Total Transactions", 10, 300, 50)
avg_transaction_amount = st.sidebar.slider("Average Transaction Amount", 100, 5000, 800)
std_transaction_amount = st.sidebar.slider("Std Transaction Amount", 0, 3000, 400)
max_transaction_amount = st.sidebar.slider("Max Transaction Amount", 100, 10000, 2000)
weekend_ratio = st.sidebar.slider("Weekend Spending Ratio", 0.0, 1.0, 0.3)
night_ratio = st.sidebar.slider("Night Transaction Ratio", 0.0, 1.0, 0.2)
end_month_ratio = st.sidebar.slider("End-of-Month Spending Ratio", 0.0, 1.0, 0.2)
spike_ratio = st.sidebar.slider("Spending Spike Ratio", 0.0, 1.0, 0.05)

# -----------------------------
# Create Input DataFrame
# -----------------------------
input_data = pd.DataFrame({
    "total_transactions": [total_transactions],
    "avg_transaction_amount": [avg_transaction_amount],
    "std_transaction_amount": [std_transaction_amount],
    "max_transaction_amount": [max_transaction_amount],
    "weekend_ratio": [weekend_ratio],
    "night_ratio": [night_ratio],
    "end_month_ratio": [end_month_ratio],
    "spike_ratio": [spike_ratio]
})

# Ensure correct feature order
input_data = input_data[features]

# Scale
scaled_input = scaler.transform(input_data)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Impulse Risk"):

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    risk_score = probabilities[2] * 100  # High risk probability
    
    st.subheader("📊 Risk Assessment")
    
    if risk_score < 40:
        st.success("Low Risk")
    elif risk_score < 70:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")
    
    st.metric("Impulse Risk Score", f"{risk_score:.2f}/100")
    
    # -----------------------------
    # Recommendations
    # -----------------------------
    st.subheader("🧠 Recommended Intervention")
    
    if risk_score > 70:
        st.write("• Introduce spending caps.")
        st.write("• Enable cooling-off period before large purchases.")
        st.write("• Disable late-night transaction approvals.")
    elif risk_score > 40:
        st.write("• Set category-wise limits.")
        st.write("• Enable real-time spending alerts.")
    else:
        st.write("• Maintain current financial discipline.")

    st.subheader("📈 Behavioural Drivers")

    importances = model.feature_importances_
    feat_df = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)

    st.bar_chart(feat_df.set_index("Feature"))