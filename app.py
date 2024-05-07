import sklearn
import streamlit as st
import pandas as pd 
import numpy as np 
import pickle
from PIL import Image


# Load model 
model = pickle.load(open('model.pkl', 'rb'))

image = Image.open('md.jpg')
st.image(image, '')
st.title("Diebetes prediction model")

#Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'

pregnancies = st.sidebar.number_input("Please enter the number of pregnencies", min_value=0, max_value=90)
