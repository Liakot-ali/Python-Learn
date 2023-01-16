# Learning and implementing State Vector Classifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# import and split data
df = pd.read_csv('../Random Forest/Social_Network_Ads.csv')
X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values
# print(len(X), len(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=0)

# train the model
print(X_train.shape, y_train.shape)
classifier = svm.SVC(kernel='linear', C=1)
classifier.fit(X_train, y_train)

# Predict the value and score the result
predict = classifier.predict(X_test)
score = accuracy_score(y_test, predict)

# Plot the original data
plt.subplot(2, 1, 1)
for x, y, con in zip(X_test[:, 0], X_test[:, 1], y_test):
    if con == 1:
        plt.scatter(x, y, color='r')
    else:
        plt.scatter(x, y, color='g')

# Plot prediction value
plt.subplot(2, 1, 2)
for x, y, con in zip(X_test[:, 0], X_test[:, 1], predict):
    if con == 1:
        plt.scatter(x, y, color='b')
    else:
        plt.scatter(x, y, color='y')
plt.show()
print(score)

