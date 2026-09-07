# 🏦 Loan Approval Prediction

A machine learning project that predicts whether a loan application is likely to be approved based on applicant and loan-related information.

## 📌 Project Overview

The objective of this project is to build a classification model that helps predict loan approval decisions using historical loan application data.

The project includes data preprocessing, exploratory data analysis, categorical encoding, model training, evaluation, and a Streamlit web application.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest Classifier
- Joblib
- Streamlit

## 🔄 Project Workflow

1. Load the loan dataset
2. Explore the data
3. Handle missing values
4. Encode categorical variables
5. Split data into training and testing sets
6. Train the Random Forest Classifier
7. Evaluate the model
8. Save the trained model using Joblib
9. Build a Streamlit application

## 🤖 Machine Learning Model

### Random Forest Classifier

Random Forest is used to predict whether a loan application will be approved or rejected.

### Target Variable

- `Y` → Loan Approved
- `N` → Loan Not Approved

## 📊 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 📁 Project Structure

Loan-Approval-Prediction/
│
├── data/
│   └── loan_prediction.csv
│
├── notebooks/
│   └── Loan_Approval_Prediction.ipynb
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore


**🚀 How to Run**

Install the required libraries
pip install -r requirements.txt
Run the Streamlit application
python -m streamlit run app.py

The application will open in your browser.

**##💡 Key Learning Outcomes**

Data cleaning and preprocessing
Exploratory Data Analysis
Handling missing values
Categorical variable encoding
Classification using Random Forest
Model evaluation
Feature importance
Model saving using Joblib
Building a Streamlit ML application

**🔮 Future Improvements**

Compare multiple classification algorithms
Perform hyperparameter tuning
Improve model performance
Add interactive visualizations
Deploy the application online


**👩‍💻 Author**

Bhumika G S
