# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:59:49 2022

@author: HP
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Pregnancies  : int
    Glucose : int
    BloodPressure  :int
    SkinThickness : int
    Insulin : int
    BMI :float
    DiabetesPedigreeFunction :float
    Age :int
    
#loading the saved model
diabetes_model = pickle.load(open('Diabetes.sav','rb'))
 
@app.post('/diabetes_prediction')
 
def diabetes_pred(input_parameters : model_input):
     
     input_data = input_parameters.json()
     input_dictionary = json.loads(input_data)
     
     preg = input_dictionary['Pregnancies']
     glu = input_dictionary['Glucose']
     bp = input_dictionary['BloodPressure']
     st = input_dictionary['SkinThickness']
     ins = input_dictionary['Insulin']
     bmi = input_dictionary['BMI']
     dbf = input_dictionary['DiabetesPedigreeFunction']
     age = input_dictionary['Age']
     
     input_list = [preg,glu,bp,st,ins,bmi,dbf,age]     
     
     prediction = diabetes_model.predict([input_list])
     if(prediction==0):
         return 'The person is non-diabetic'
     else:
         return 'The person is diabetic'