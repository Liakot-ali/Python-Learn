import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Import Iris dataset and store the data and target
iris = load_iris()
X = np.array(iris['data'])
y = np.array(iris['target'])

# Train and fit the model
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Transform the data
data_set = lda.transform(X)
print(data_set)

# Plotting the grouped data
plt.scatter(data_set[y == 0, 0], data_set[y == 0, 1], c='r', label=iris['target_names'][0])
plt.scatter(data_set[y == 1, 0], data_set[y == 1, 1], c='g', label=iris['target_names'][1])
plt.scatter(data_set[y == 2, 0], data_set[y == 2, 1], c='b', label=iris['target_names'][2])
plt.legend()
plt.show()

# Predicting score
score = cross_val_score(lda, X, y, scoring='accuracy')
print(np.mean(score))