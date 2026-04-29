import pickle
import pandas as pd

# Load trained model
modelObject = pickle.load(open(
r"C:\Users\HP\OneDrive\Desktop\ML Project 1 (HOUSE PRICE PREDICTION)\Model\model_linear.pkl","rb"))

# Sample input with all features
sample = pd.DataFrame(
[[2000,3,2,2,1,0,0,0,1,2,1,1]],
columns=[
'area',
'bedrooms',
'bathrooms',
'stories',
'mainroad',
'guestroom',
'basement',
'hotwaterheating',
'airconditioning',
'parking',
'prefarea',
'furnishingstatus'
])

# Predict
prediction = modelObject.predict(sample)

print("Predicted House Price:", prediction[0])