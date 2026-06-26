import streamlit as st
import pandas as pd
import joblib

model = joblib.load("weather_model.pkl")

st.set_page_config(
    page_title="Weather Prediction App",
    layout="centered")

st.title("🌦 Weather Rain Prediction System")
st.write("Enter weather conditions to predict whether it will rain tomorrow.")


col1, col2 = st.columns(2)

with col1:
    humidity = st.number_input("Humidity at 3pm", min_value=0.0, max_value=100.0, value=50.0,step=1.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=0.0,step=1.0)
    sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=15.0,step=1.0, value=5.0)

with col2:
    cloud = st.number_input("Cloud cover at 3pm", min_value=0.0, max_value=9.0,step=1.0, value=4.0)
    pressure = st.number_input("Pressure at 3pm", value=1015.0,step=1.0)
    rain_today = st.selectbox("Rain Today", ["Yes", "No"])

input_data = pd.DataFrame([{
    "Humidity3pm": humidity,
    "Rainfall": rainfall,
    "Sunshine": sunshine,
    "Cloud3pm": cloud,
    "Pressure3pm": pressure,
    "RainToday": rain_today }])

st.markdown("---")

if st.button("Predict Rain Tomorrow"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🌧 It WILL rain tomorrow")
    else:
        st.success("☀ No rain expected tomorrow")

    st.write("Prediction output:", prediction[0])

with st.expander("Show input data"):
    st.write(input_data)
