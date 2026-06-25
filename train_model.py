import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("house_data.csv")

X = data[["Area", "Bedrooms"]]
y = data["Price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")