import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score




df = pd.read_csv("data/processed_dataset.csv")

X = df.drop("Logistics_Delay",axis=1)
Y = df["Logistics_Delay"]


print(X.head())
print(Y.head())