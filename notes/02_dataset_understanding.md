# Dataset Understanding - LogisChain AI

## Dataset Purpose

This dataset contains logistics and supply chain information of trucks, shipments, inventory, traffic conditions, and customer demand.

The goal is to analyze factors that cause delivery delays and predict logistics risks using Machine Learning.

---

## Target Variable

### Logistics_Delay

Values:
- 0 = No Delay
- 1 = Delay

This is the column our ML model will predict.

---

## Column Explanation

### Timestamp
Date and time when logistics data was recorded.


Example:
2024-03-20 00:11:14

Importance:
Helps identify peak hours, busy days, and seasonal patterns.

---

### Asset_ID
Unique truck or vehicle identifier.

Example:
Truck_7

Importance:
Used to track individual vehicle performance.

---

### Latitude
Current geographical latitude of truck.

Example:
-65.7383

Importance:
Shows truck location.

---

### Longitude
Current geographical longitude of truck.

Example:
11.2497

Importance:
Used with latitude for route analysis.

---

### Inventory_Level
Available stock quantity.

Example:
390

Importance:
Low inventory may create supply chain issues.

---

### Shipment_Status

Possible values:
- Delivered
- In Transit
- Delayed

Importance:
Shows current shipment condition.

---

### Temperature

Example:
27.0°C

Importance:
Extreme weather can affect transportation.

---

### Humidity

Example:
67.8%

Importance:
Environmental condition affecting goods and transportation.

---

### Traffic_Status

Possible values:
- Clear
- Heavy
- Detour

Importance:
Major factor affecting delivery delays.

---

### Waiting_Time

Example:
38 minutes

Importance:
Measures idle or waiting duration.

Higher waiting time may increase delay probability.

---

### User_Transaction_Amount

Example:
320

Importance:
Represents customer transaction value.

Useful for business analysis.

---

### User_Purchase_Frequency

Example:
4

Importance:
Shows how often a customer purchases.

Can indicate future demand.

---

### Logistics_Delay_Reason

Possible values:
- Weather
- Traffic
- Mechanical Failure
- None

Importance:
Explains why delays occurred.

Useful for root cause analysis.

---

### Asset_Utilization

Example:
60.1%

Importance:
Measures vehicle usage efficiency.

High utilization may increase maintenance risk.

---

### Demand_Forecast

Example:
285

Importance:
Predicted future demand.

Helps inventory planning.

---

### Logistics_Delay (Target)

Values:
- 0 = No Delay
- 1 = Delay

This is the final prediction column for our Machine Learning model.

---

## Features Used For Prediction

- Inventory_Level
- Shipment_Status
- Temperature
- Humidity
- Traffic_Status
- Waiting_Time
- User_Transaction_Amount
- User_Purchase_Frequency
- Asset_Utilization
- Demand_Forecast

---

## Project Objective

Build a Machine Learning model that predicts whether a shipment will be delayed based on logistics, traffic, inventory, environmental, and customer demand factors.

Input → Supply Chain Data

Output → Logistics Delay Prediction (0 or 1)
