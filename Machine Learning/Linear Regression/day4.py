# Implementing multiple linear regression
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# import and process data
df = pd.read_csv('kc_house_data.csv')

# Delete if the dataframe contain null values and replace with median

# df.bedrooms = df.bedrooms.fillna(math.floor(np.median(df.bedrooms)))
# df.iloc[:, 4] = df.iloc[:, 4].fillna(np.median(df.iloc[:, 4]))
# df.iloc[:, 5] = df.iloc[:, 5].fillna(np.median(df.iloc[:, 5]))
# df.iloc[:, 6] = df.iloc[:, 6].fillna(np.median(df.iloc[:, 6]))

X = df.iloc[:, [3, 4, 5, 6]].values
y = df.iloc[:, 2].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# y_test = np.array(y_test).reshape(-1, 1)
mulR = LinearRegression()
mulR.fit(X_train, y_train)
print(f"Co-efficients: {mulR.coef_} ", f"\nIntercept : {mulR.intercept_}")

predict = mulR.predict(X_test)
# print(y_test, predict)

score = mulR.score(X_test, y_test)
print("Score: ", score)