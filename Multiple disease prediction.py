# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:50:39 2023

@author: hp
"""

import pickle
import streamlit as st
from streamlit_option_menu  import option_menu

# Loading the saved model

diabetes_model = pickle.load(open('C:/Users/hp/Desktop/Multiple disease prediction system/saved_model/Diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/hp/Desktop/Multiple disease prediction system/saved_model/Heart_model.sav','rb'))
cancer_model = pickle.load(open('C:/Users/hp/Desktop/Multiple disease prediction system/saved_model/Cancer_model.sav','rb'))

# sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Cancer Prediction'],icons=['activity','heart','person'],default_index=0)
    
# Diabetes Prediction page
if(selected=='Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    # column for input fields
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for  prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if(st.button('Diabetes Test Result')):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
      
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'
    
    st.success(diab_diagnosis)
    
    
# Heart Disease Prediction page
if(selected=='Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    # column for input fields
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex= st.text_input('sex')
    with col3:
        cp = st.text_input('chest pain value')
    with col1:
        trestbps = st.text_input('Resting blood pressure (in mm Hg value)')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl')
    with col3:
        fbs= st.text_input('fasting blood sugar>120 mg/dl value')
    with col1:
        restecg = st.text_input('resting ecg value(0,1,2)')
    with col2:
        thalach = st.text_input('maximum heart rate achieved')
    with col3:
        exang = st.text_input('exercise induced angina value')
    with col1:
        oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest value')
    with col2:
        slope = st.text_input('the slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('thal:0 = normal; 1= fixed defect; 2= reversable defect')
    
    
    # code for  prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if(st.button('Heart Disease Test Result')):
        diab_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
      
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person have heart disease'
        else:
            diab_diagnosis = 'The person have healthy heart/The person is healthy'
    
    st.success(diab_diagnosis)

# Diabetes Prediction page
if(selected=='Cancer Prediction'):
    
    # page title
    st.title('Cancer Prediction using ML')
    
    # getting the input data from the user
    # column for input fields
    col1,col2,col3 = st.columns(3)
    with col1:
        id = st.text_input('id')
    with col2:
        diagnosis= st.text_input('Diagnosis')
    with col3:
        radius_mean = st.text_input('Radius Mean value')
    with col1:
        texture_mean = st.text_input('Texture Mean value')
    with col2:
        perimeter_mean = st.text_input('Perimeter Mean value')
    with col3:
        area_mean= st.text_input('Area Mean value')
    with col1:
        smoothness_mean = st.text_input('Smoothness Mean value')
    with col2:
        compactness_mean = st.text_input('Compactness Mean value')
    with col3:
        concavity_mean = st.text_input('Concavity Mean value')
    with col1:
        concave_points_mean = st.text_input('Concave Points Mean value')
    with col2:
        symmetry_mean = st.text_input('Symmetry Mean value')
    with col3:
        fractal_dimension_mean= st.text_input('Fractal Dimension Mean value')
    with col1:
        radius_se = st.text_input('Radius Se value')
    with col2:
        texture_se = st.text_input('Texture Se value')
    with col3:
        perimeter_se = st.text_input('Perimeter Se value')
    with col1:
        area_se = st.text_input('Area Se value')
    with col2:
        smoothness_se = st.text_input('Smoothness Se value')
    with col3:
        compactness_se= st.text_input('Compactness Se value')
    with col1:
        concavity_se = st.text_input('Concavity Se value')
    with col2:
        concave_points_se= st.text_input('Concavuty Points Se')
    with col3:
        symmetry_se = st.text_input('Symmetry Se value')
    with col1:
        fractal_dimension_se= st.text_input('Fractal Dimension Se value')
    with col2:
        radius_worst = st.text_input('Radius Worst value')
    with col3:
        texture_worst = st.text_input('Texture Worst value')
    with col1:
        perimeter_worst = st.text_input('Perimeter Worst value')
    with col2:
        area_worst = st.text_input('Area Worst value')
    with col3:
        smoothness_worst = st.text_input('Smoothness Worst value')
    with col1:
        compactness_worst = st.text_input('Compactness Worst value')
    with col2:
        concavity_worst = st.text_input('Concavity Worst value')
    with col3:
        concave_points_worst = st.text_input('Concave Points Worst value')
    with col1:
        symmetry_worst= st.text_input('Symmetry Worst value')
    with col2:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst value')
    
    
    # code for  prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if(st.button('Cancer Test Result')):
        diab_prediction = cancer_model.predict([[id,diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
      
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person have Cancer'
        else:
            diab_diagnosis = "The person don't  have Cancer"
    
    st.success(diab_diagnosis)
  
if(selected=='Heart Disease Prediction'):
    
    # page title
    st.title(' Heart Disease Prediction using ML')

if(selected=='Cancer Prediction'):
    
    # page title
    st.title('Cancer Prediction using ML')
    
    