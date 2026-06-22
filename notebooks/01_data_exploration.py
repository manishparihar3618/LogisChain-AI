import pandas as pd
df = pd.read_csv("data/smart_logistics_dataset.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print("Missing values are:",df.isnull().sum())
print("Number of duplicates are: ",df.duplicated().sum())