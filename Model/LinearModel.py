import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\ML Project 1 (HOUSE PRICE PREDICTION)\Datasets\Housing.csv")

print(df.head())
print(df.isnull().sum())

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# Label Encoding
le = LabelEncoder()
cat_cols = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Train test split
X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

# Pipeline
pipeline = Pipeline([
("scaler",StandardScaler()),
("model",LinearRegression())
])

# Train
pipeline.fit(X_train,y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Accuracy
r2 = r2_score(y_test,y_pred)

print("Improved R2 Score:", r2)

# Save model
pickle.dump(pipeline,open("model_linear.pkl","wb"))
print("Model Successfully Dumped")