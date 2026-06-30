import joblib 
import pandas as pd 

model = joblib.load("models/financial_risk_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

sample = pd.DataFrame({
    "Latitude": [22.57],
    "Longitude": [88.36],
    "Inventory_Level": [250],
    "Temperature": [35],
    "Humidity": [80],
    "Waiting_Time": [28],
    "User_Transaction_Amount": [420],
    "User_Purchase_Frequency": [5],
    "Asset_Utilization": [88],
    "Demand_Forecast": [720],
    "Year": [2024],
    "Month": [6],
    "Day": [30],
    "Hour": [10],
    "Day_of_Week": [1],
    "Traffic_Status_Detour": [1],
    "Traffic_Status_Heavy": [0]
})

prediction = model.predict(sample)
print("predicted Financial Risk: ",prediction[0])