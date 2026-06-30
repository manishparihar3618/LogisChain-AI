import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("data/Financial_Risk_Dataset.csv")
encoder = LabelEncoder()
Y = encoder.fit_transform(df["Financial_Risk"])


X = df[["Latitude","Longitude","Inventory_Level","Temperature","Humidity","Waiting_Time", "User_Transaction_Amount","User_Purchase_Frequency","Asset_Utilization","Demand_Forecast","Year","Month","Day","Hour","Day_of_Week","Traffic_Status_Detour","Traffic_Status_Heavy"]]
Y = df["Financial_Risk"]

print(X.head())
print(Y.head())


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = RandomForestClassifier(
n_estimators = 100,
random_state = 42,class_weight="balanced")
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(Y_test, Y_pred))
print(confusion_matrix(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))

# Removed "Shipment_Status_Delivered","Shipment_Status_In Transit" columns because they were leakaging data and because of that out model was getting 100 accuracy 