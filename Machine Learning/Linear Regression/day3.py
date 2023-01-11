import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Linear regression using Sklearn.linear_model
df_train = pd.read_csv('test.csv')
df_test = pd.read_csv('train.csv')
X_train = np.array(df_train['x']).reshape(-1, 1)
y_train = np.array(df_train['y']).reshape(-1, 1)

# x_test = np.array(df_test['x']).reshape(-1, 1)
# y_test = np.array(df_test['y']).reshape(-1, 1)
x_test = np.array(df_train['x']).reshape(-1, 1)
y_test = np.array(df_train['y']).reshape(-1, 1)

# Training the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the score using test data set
predict = regressor.predict(x_test)
# Showing the actual and predicted dataset
x = 0
for i in predict:
    print(y_test[x], i)
    x += 1

score = regressor.score(y_test, predict)
print(score)

plt.scatter(X_train, y_train, color='r')
plt.plot(x_test, predict, color='g')
plt.show()
