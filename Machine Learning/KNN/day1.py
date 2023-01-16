import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as cmap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Import and process data
df = pd.read_csv('../Random Forest/Social_Network_Ads.csv')
X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the dataset
# print(X_train.size)
knn = KNeighborsClassifier(n_neighbors=int(math.sqrt(X_train.size)), p=2)
knn.fit(X_train, y_train)

# Plot the training set
plt.subplot(2, 1, 1)
index = 0
for i in y_train:
    if i == 0:
        plt.scatter(X_train[index][0], X_train[index][1], color='r')
    else:
        plt.scatter(X_train[index][0], X_train[index][1], color='g')
    index += 1

# Predict the testing result and accuracy score
predict = knn.predict(X_test)
score = accuracy_score(y_test, predict)
print(score)

# Plot the result
plt.subplot(2, 1, 2)
index = 0
for i in predict:
    if i == 0:
        plt.scatter(X_test[index][0], X_test[index][1], color='b')
    else:
        plt.scatter(X_test[index][0], X_test[index][1], color='y')
    index += 1

plt.show()


