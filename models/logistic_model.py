import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)




df = pd.read_csv("data/Processed_dataset.csv")

X = df.drop("Logistics_Delay",axis=1)
Y = df["Logistics_Delay"]


print(X.head())
print(Y.head())


## Train_Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)



## Standarlization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


## Training Logistic regression
model = LogisticRegression(random_state=42)
model.fit(X_train,Y_train)

## Prediction
y_pred = model.predict(X_test)


## Evaluate
print("Accuracy:", accuracy_score(Y_test, y_pred))
print("Precision:", precision_score(Y_test, y_pred))
print("Recall:", recall_score(Y_test, y_pred))
print("F1 Score:", f1_score(Y_test, y_pred))

print(confusion_matrix(Y_test, y_pred))
print(classification_report(Y_test, y_pred))