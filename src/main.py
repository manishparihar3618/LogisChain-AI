

import pandas as pd

# Load logistics dataset
df = pd.read_csv("data/Processed_dataset.csv")

def calculate_financial_risk(row):
    score = 0

    # Inventory Risk
    if row["Inventory_Level"] < 200:
        score += 2
    elif row["Inventory_Level"] < 400:
        score += 1

    # Demand Risk
    if row["Demand_Forecast"] > 800:
        score += 2
    elif row["Demand_Forecast"] > 600:
        score += 1

    # Waiting Time Risk
    if row["Waiting_Time"] > 40:
        score += 2
    elif row["Waiting_Time"] > 20:
        score += 1

    # Traffic Risk
    if row["Traffic_Status_Heavy"]:
        score += 2

    if row["Traffic_Status_Detour"]:
        score += 1

    # Weather Risk
    if row["Temperature"] > 38 or row["Temperature"] < 5:
        score += 1

    if row["Humidity"] > 85:
        score += 1

    # Asset Utilization
    if row["Asset_Utilization"] > 90:
        score += 1

    # Final Risk Level
    if score >= 8:
        return "High"

    elif score >= 4:
        return "Medium"

    else:
        return "Low"

# Generate Financial Risk
df["Financial_Risk"] = df.apply(calculate_financial_risk, axis=1)

# Save dataset
df.to_csv("Financial_Risk_Dataset.csv", index=False)

print(df.head())
print(df["Financial_Risk"].value_counts())