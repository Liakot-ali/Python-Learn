import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets, metrics

digits = datasets.load_digits()

# Showing some sample dataset
# index = 1
# plt.figure()
# for image, label in zip(digits.data[0:10], digits.target[0:10]):
#     plt.subplot(2, 5, index)
#     plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
#     plt.title(label)
#     index += 1
# plt.show()

# Splitting the dataset into train and test
X = digits.data
y = digits.target
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
print(X_train.shape, y_train.shape)

# Train the dataset
logr = LogisticRegression(solver='liblinear')
logr.fit(X_train, y_train)

# Predict the result
predict = logr.predict(x_test)
# print(predict, y_test)

# see the score
score = metrics.accuracy_score(y_test, predict)
print("Prediction Score:", score)

# Show the result
index = 0
plt.figure()
for image, label, pre in zip(x_test[0:10], y_test[0:10], predict[0:10]):
    plt.subplot(2, 5, index+1)
    plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
    plt.title(f'R: {label} P: {pre}')
    index += 1
plt.show()


