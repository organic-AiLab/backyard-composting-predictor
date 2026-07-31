import streamlit as st
import joblib
import numpy as np

# Load the trained model (make sure 'irrigation_model.joblib' is in your GitHub repo)
model = joblib.load('irrigation_model.joblib')

st.title("Irrigation Water Requirement Prediction")

# Input fields for the user
max_temp = st.number_input("Max Temperature (°C)", value=30.0)
humidity = st.number_input("Humidity (%)", value=50.0)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)
solar_rad = st.number_input("Solar Radiation (MJ/m²)", value=20.0)
soil_cap = st.number_input("Soil Field Capacity", value=0.35)
crop_stage = st.number_input("Crop Stage (Days)", value=30.0)

# Prediction button
if st.button("Predict"):
    # Prepare input data for the model
    input_data = np.array([[max_temp, humidity, wind_speed, solar_rad, soil_cap, crop_stage]])
    # Make prediction
    prediction = model.predict(input_data)
    # Display the prediction
    st.success(f"Predicted Irrigation Water: **{prediction[0]:.2f} mm**")
