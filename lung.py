# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 11:08:18 2025

@author: ASUS
"""

import numpy as np
import streamlit as st
import pickle

loaded_model=pickle.load(open("lungcancer.sav",'rb'))

def survival_prediction(input_data):
    input_data_arr=np.asarray(input_data)
    input_data_reshape=input_data_arr.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction==0):
      return 'Not Survived'
    else:
      return 'Survived'
def main():
    st.title('Lung Cancer Survival Prediction App')
   
    age=st.text_input('Enter Age')
    gender=st.text_input('Enter Gender(Male:1,Femail:0)')
    family_history=st.text_input('Family History of Smoking(Yes:1,No:0)')
    smoking_status=st.text_input('Passive Smoker:3,Former Smoker:1,Current Smoker:0,Never Smoked:2')
    bmi=st.text_input('Enter Body Mass Index')
    cholesterol_level=st.text_input('Enter cholestrol level')
    hypertension=st.text_input('Enter hypertension(Yes:1,No:0)')
    asthma=st.text_input('Asthma(Yes:1,No:0)')
    cirrhosis=st.text_input('Cirrhosis(Yes:1,No:0)')
    other_cancer=st.text_input('Other Cancer(Yes:1,No:0)')
    treatment_type=st.text_input('Surgery:3,Chemotherapy:0,Combined:1,Radiation:2')
    cancer_stage=st.text_input('Stage of Cancer(Stage 1, Stage 2,Stage 3,Stage 4)')
   
    survival=''
   
    if(st.button('See Survival Chances')):
        survival=survival_prediction([float(age),float(gender),float(family_history),float(smoking_status),float(bmi),float(cholesterol_level),float(hypertension),float(asthma),float(cirrhosis),float(other_cancer),float(treatment_type),float(cancer_stage)])
       
    st.success(survival)
main()

    
