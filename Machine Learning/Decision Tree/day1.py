import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# import data from csv and split
df = pd.read_csv('Social_Network_Ads.csv')
X = df.drop(columns='Purchased')
y = df['Purchased']
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(X_train.shape, y_train.shape)

# Train the model with 'Information Gain' ASM
dcsnt = DecisionTreeClassifier(criterion='entropy', random_state=0)
dcsnt.fit(X_train, y_train)

# Predict the result based on testing data
predict = dcsnt.predict(x_test)

# showing the actual and predicted data
for i, j in zip(y_test, predict):
    print(i, j)

# Measuring the accuracy
score = accuracy_score(y_test, predict)
print("Accuracy: ", score)