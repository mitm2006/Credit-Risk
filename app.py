import streamlit as st
import pandas as pd 
import joblib

st.set_page_config(
    page_title="Credit Risk Assessment",
    page_icon="🏦",
    layout="wide"
)

@st.cache_resource
def load_data():
    model = joblib.load('C:\\Study\\Programming\\PYTHON\\Projects\\best_rf_credit_risk_modeling.pkl')
    encoders = {col: joblib.load(f"{col}_encoder.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account", "Purpose"]}
    return model, encoders

try:
    model, encoders = load_data()
except FileNotFoundError as e:
    st.error(f"Error loading model or encoders. Please check files: {e}")
    st.stop()

st.title("Credit Risk Prediction App")
st.markdown("### Intelligent Credit Risk Assessment System")
st.markdown("---")

with st.sidebar:
    st.header("Applicant Information")
    st.write("Please fill in the details below:")
    
    age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Applicant's age in years")
    sex = st.selectbox("Sex", ["Male", "Female"], help="Applicant's gender")
    job = st.number_input("Job Content (0-3)", min_value=0, max_value=3, value=1, help="Job qualification level (0-3)")
    housing = st.selectbox("Housing Type", ["Own", "Rent", "Free"], help="Type of housing")
    saving_accounts = st.selectbox("Saving Accounts", ["Little", "Moderate", "Rich", "Quite Rich", "No Account"], help="Status of saving accounts")
    checking_account = st.selectbox("Checking Account", ["Little", "Moderate", "Rich", "No Account"], help="Status of checking account")
    credit_amount = st.number_input("Credit Amount", min_value=0, max_value=100000, value=10000, step=500, help="Amount of credit requested")
    duration = st.number_input("Duration (Months)", min_value=0, max_value=100, value=12, help="Duration of credit in months")
    purpose = st.selectbox("Purpose", ["Business", "Car", "Domestic Appliances", "Education", "Furniture/Equipment", "Radio/TV", "Repairs", "Vacation/Others"], help="Purpose of the credit")
    
    st.markdown("---")
    predict_btn = st.button("Predict Credit Risk", type="primary")

col1, col2 = st.columns([2, 1])

with col1:
    st.info("**Instructions:** Adjust the values in the sidebar to simulate a credit application.")
    
    st.subheader("Current Application Summary")
    summary_df = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "Credit Amount": [credit_amount],
        "Duration": [f"{duration} months"]
    })
    st.table(summary_df)

with col2:
    if predict_btn:
        with st.spinner("Analyzing credit risk..."):

            sex_val = sex.lower()
            housing_val = housing.lower()
            
            saving_val = "No Account" if saving_accounts == "No Account" else saving_accounts.lower()
            checking_val = "No Account" if checking_account == "No Account" else checking_account.lower()
            
            purpose_map = {
                "Business": "business",
                "Car": "car",
                "Domestic Appliances": "domestic appliances",
                "Education": "education",
                "Furniture/Equipment": "furniture/equipment",
                "Radio/TV": "radio/TV",
                "Repairs": "repairs",
                "Vacation/Others": "vacation/others"
            }
            purpose_val = purpose_map[purpose]
            
            input_df = pd.DataFrame({
                "Age": [age],
                "Sex": encoders["Sex"].transform([sex_val])[0],
                "Job": [job],
                "Housing": encoders["Housing"].transform([housing_val])[0],
                "Saving accounts": encoders["Saving accounts"].transform([saving_val])[0],
                "Checking account": encoders["Checking account"].transform([checking_val])[0],
                "Credit amount": [credit_amount],
                "Purpose": encoders["Purpose"].transform([purpose_val])[0],
                "Duration": [duration]
            })
            
            prediction = model.predict(input_df)[0]
            
            st.divider()
            st.subheader("Result")
            
            if prediction == 1:
                st.success("Risk Level: **Low** (Good)")
                st.balloons()
            else:
                st.error("Risk Level: **High** (Bad)")
    
