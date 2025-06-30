import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("personality.pkl")

st.title("🧠 Personality Predictor (Introvert vs Extrovert)")
st.write("Enter your behavioral data:")

# Input fields
event = st.number_input("Social Event Attendance per month (0–10)", min_value=0, max_value=10)
outside = st.number_input("Going Outside per week (0–7)", min_value=0, max_value=7)
post = st.number_input("Social media Post Frequency per week (0–10)", min_value=0, max_value=10)
friends = st.number_input("Friends Circle Size (0–15)", min_value=0, max_value=15)

# Predict button
if st.button("Predict"):
    data = np.array([[event, outside, post, friends]])
    prediction = model.predict(data)[0]
    result = "Extrovert 🎉" if prediction == 1 else "Introvert 🤫"
    st.success(f"Predicted Personality: {result}")