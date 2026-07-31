import streamlit as st
import joblib
import numpy as np

# Load the trained model (make sure 'backyard_compost_model.joblib' is in your GitHub repo)
model = joblib.load('backyard_compost_model.joblib')

st.title("🌱 Backyard Home Composting Decomposition Predictor")

# Input fields for the user
green_brown = st.slider("Green / Brown Ratio Score", min_value=1, max_value=5, value=3)
turning_freq = st.slider("Turning Frequency (Weekly)", min_value=0, max_value=3, value=1)
moisture = st.slider("Moisture Level Score", min_value=1, max_value=5, value=3)
temp = st.slider("Ambient Season Temperature (°F)", min_value=30.0, max_value=100.0, value=70.0)

# Prediction button
if st.button("Predict Decomposition Time"):
    # Prepare input data for the model
    input_data = np.array([[green_brown, turning_freq, moisture, temp]])
    # Make prediction
    prediction = model.predict(input_data)
    # Display the prediction
    st.success(f"Estimated Time to Finished Compost: **{max(2.0, prediction[0]):.1f} Weeks**")
