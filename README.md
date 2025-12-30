# 🏦 Credit Risk Prediction App

## Project Overview

The **Credit Risk Prediction App** is a machine learning–powered web application built using **Streamlit** that predicts the credit risk of loan applicants.  
By analyzing demographic and financial information, the app classifies applicants as **Low Risk (Good Credit)** or **High Risk (Bad Credit)**.

This project demonstrates an end-to-end ML workflow — from model training to deployment in an interactive web application.

---

## Features

- Interactive Streamlit user interface  
- Pre-trained Random Forest model  
- Automatic encoding of categorical features  
- Fast predictions using cached resources  
- Clear and user-friendly risk classification  

---

## Machine Learning Model

- **Algorithm:** Random Forest Classifier  
- **Problem Type:** Binary Classification  
- **Target:** Credit Risk (Good / Bad)  

**Model File:**
best_rf_credit_risk_modeling.pkl


Categorical variables are transformed using saved encoders loaded at runtime.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Joblib  

---

## Project Structure

├── app.py<br>
├── best_rf_credit_risk_modeling.pkl<br>
├── Sex_encoder.pkl<br>
├── Housing_encoder.pkl<br>
├── Saving accounts_encoder.pkl<br>
├── Checking account_encoder.pkl<br>
├── Purpose_encoder.pkl<br>
├── README.md<br>


---

## 🧾 Input Parameters

The application requires the following inputs:

- Age  
- Sex  
- Job level (0–3)  
- Housing type  
- Saving account status  
- Checking account status  
- Credit amount  
- Loan duration (months)  
- Purpose of the loan  

---

## 📈 Output

The model predicts the applicant's credit risk:

- **Low Risk (Good Credit)**  
- **High Risk (Bad Credit)**  

Results are displayed instantly after clicking **Predict Credit Risk**.

---

## How to Run the Application

### Clone the Repository
```bash
git clone https://github.com/mitm2006/credit-risk-prediction.git
cd credit-risk-prediction

pip install streamlit pandas scikit-learn joblib
streamlit run app.py
```
## Important Notes
Ensure all .pkl files are present in the project directory.
Update file paths if required.
This project is for educational purposes only and should not be used for real-world financial decisions.

## Author
Mit Mhatre<br>
Aspiring Data Scientist | Machine Learning Enthusiast




