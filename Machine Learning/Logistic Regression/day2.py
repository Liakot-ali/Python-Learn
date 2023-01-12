# Trying to implement logistic regression using some kaggle dataset (titanic data science solution)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# import the data
df = pd.read_csv('gender_submission.csv')

# Split and process the data
X = df['PassengerId']
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5, shuffle=True)
X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)

# print(X_train.shape, y_train.shape)
# Learn the model
logr = LogisticRegression(solver='liblinear')
logr.fit(X_train, y_train)

# Predict the value
predict = logr.predict(X_test)

# Showing in plot
plt.scatter(X_train, y_train)
plt.scatter(X_test, predict, color='r')
plt.show()

# Measuring the accuracy
score = accuracy_score(X_test, predict)
print(score)
