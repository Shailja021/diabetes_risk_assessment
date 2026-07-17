import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Diabetes Risk Assessment", page_icon="🩺")

st.title("🩺 Diabetes Risk Assessment")
st.write("Enter the patient's health details below.")

pregnancies = st.number_input("Pregnancies", min_value=0.0)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0.0)

if st.button("Predict"):

    data = np.array([[pregnancies,
                      glucose,
                      blood_pressure,
                      skin_thickness,
                      insulin,
                      bmi,
                      dpf,
                      age]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")