import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
companies = pd.read_csv('1000_Companies.csv')
X = companies.iloc[:, :-2]      # all columns except the last one
y = companies.iloc[:, 4]     # only the 5th column (4 index)
# labelEncoder = LabelEncoder()
# X[:, 3] = labelEncoder.fit_transform(X[:, 3])
# onehotencoder = OneHotEncoder(categories=[3])
# X = onehotencoder.fit_transform(X).toarray()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train, X_test, y_train, y_test)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True)

y_predict = regressor.predict(X_test)
x_predict = regressor.predict(X_train)
plt.scatter(X_train, y_train, color='r')
# plt.plot(X_train, y_predict, color='g')
plt.show()

print(y_predict)



