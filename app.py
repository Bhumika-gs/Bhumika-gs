import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦"
)

st.title("🏦 Loan Approval Prediction")
st.write("Enter the applicant details below to predict loan approval.")

# Input fields
Gender = st.selectbox("Gender", ["Male", "Female"])

Married = st.selectbox("Married", ["Yes", "No"])

Dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

Education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

ApplicantIncome = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

CoapplicantIncome = st.number_input(
    "Co-applicant Income",
    min_value=0,
    value=0
)

LoanAmount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=150
)

Loan_Amount_Term = st.number_input(
    "Loan Term (months)",
    min_value=1,
    value=360
)

Credit_History = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)


# Convert inputs to model format
input_data = pd.DataFrame({
    "Gender": [1 if Gender == "Male" else 0],
    "Married": [1 if Married == "Yes" else 0],
    "Dependents": [
        3 if Dependents == "3+" else int(Dependents)
    ],
    "Education": [
        0 if Education == "Graduate" else 1
    ],
    "Self_Employed": [
        1 if Self_Employed == "Yes" else 0
    ],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area": [
        {"Urban": 2, "Semiurban": 1, "Rural": 0}[Property_Area]
    ]
})


# Prediction
if st.button("Check Loan Eligibility"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")