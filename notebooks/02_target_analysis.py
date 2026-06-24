import pandas as pd

df = pd.read_csv("data/smart_logistics_dataset.csv")

print("Target Distribution")
print(df["Logistics_Delay"].value_counts())

print("\nShipment Status")
print(df["Shipment_Status"].value_counts())

print("\nTraffic Status")
print(df["Traffic_Status"].value_counts())

print("\nDelay Reasons")
print(df["Logistics_Delay_Reason"].value_counts())