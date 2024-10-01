import streamlit as st
import joblib
import numpy as np

def main():
  st.markdown("<h1 style = 'text-align: center; color: white; '>Stroke Prediction</h1>",
              unsafe_allow_html = True)

  model = joblib.load('Stroke_Prediction (1)')

  age = st.number_input('Age:', min_value = 1, max_value = 100)

  avg_glucose_level = st.number_input("Enter Your Average Glucose Level:", min_value = 0, max_value = 350)

  bmi = st.number_input("Enter Your BMI Value:")
  st.markdown("You can calculate your BMI value here: https://www.calculator.net/bmi-calculator.html")

  gender = st.selectbox('Gender', ('Female', 'Male'))
  if(gender == 'Female'):
    gender = 0
  else:
    gender = 1

  hypertension_1 = st.selectbox('Hypertension', ('Yes', 'No'))
  if(hypertension_1 == 'Yes'):
    hypertension_1 = 1
  else:
    hypertension_1 = 0

  heart_disease_1 = st.selectbox('Heart Disease', ('Yes', 'No'))
  if(heart_disease_1 == 'Yes'):
    heart_disease_1 = 1
  else:
    heart_disease_1 = 0

  ever_married_Yes = st.selectbox('Ever Married', ('Yes', 'No'))
  if(ever_married_Yes == 'Yes'):
    ever_married_Yes = 1
  else:
    ever_married_Yes = 0

  work_type = st.selectbox('Work Type?', ('Children', 'Never Worked', 'Private', 'Self Employed', 'Goverment'))
  if(work_type == 'Children'):
    work_type = 0
  elif(work_type == 'Never Worked'):
    work_type = 1
  elif(work_type == 'Private'):
    work_type = 2
  elif(work_type == 'Self Employed'):
    work_type = 3
  else:
    work_type = 4

  residence_type = st.selectbox('Enter Your Residence Type', ('Rural', 'Urban'))
  if(residence_type == 'Rural'):
    residence_type = 0
  else:
    residence_type = 1

  smoking_status = st.selectbox('Smoking Status', ('Never', 'Formerly Smoked', 'Smokes', 'Unknown'))
  if(smoking_status == 'Never'):
    smoking_status = 0
  elif(smoking_status == 'Formerly Smoked'):
    smoking_status = 1
  elif(smoking_status == 'Smokes'):
    smoking_status = 2
  else:
    smoking_status = 3

  if st.button('Predict'):
    pred = model.predict([[age, bmi, avg_glucose_level, gender, hypertension_1, heart_disease_1, ever_married_Yes, work_type, residence_type, smoking_status]])

    if pred == 0:
        # Stroke prediction is 0 (not stroke)
        st.success('Your Stroke Prediction is: **Not Stroke**')
        st.balloons()
    else:
        # Stroke prediction is 1 (stroke)
        st.error('Your Stroke Prediction is: **Stroke**')

if __name__ == '__main__':
  main()