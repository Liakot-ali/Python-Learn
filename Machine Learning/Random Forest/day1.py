import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score

# Import and process data
df = pd.read_csv('Social_Network_Ads.csv')
# print(df.head())
# X = df.drop(columns='Purchased')
# y = df['Purchased']

# crop age and estimated salary to X, and purchased to y
X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values

# print(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model with information gain ASM
ranForest = RandomForestClassifier(n_estimators=10, criterion='entropy')
ranForest.fit(X_train, y_train)

# Predict train and testing dataset
test_predict = ranForest.predict(X_test)
tr_predict = ranForest.predict(X_train)

# Crop the age and estimated salary to plot
tr_sca_x = X_train[:, 0]     # copy the ages
tr_sca_y = X_train[:, 1]     # copy the estimated salary

te_sca_x = X_test[:, 0]     # copy the ages
te_sca_y = X_test[:, 1]     # copy the estimated salary

# Plot training age and estimated salary
plt.subplot(2, 3, 1)
plt.scatter(tr_sca_x, tr_sca_y, color='r')
# # Plot testing age and estimated salary
plt.scatter(te_sca_x, te_sca_y, color='g')

# Plot training and testing age with purchased
plt.subplot(2, 3, 2)
plt.scatter(tr_sca_x, y_train, color='r')
plt.scatter(te_sca_x, y_test, color='g')

# Plot training and testing estimated with purchased
plt.subplot(2, 3, 3)
plt.scatter(tr_sca_y, y_train, color='g')
plt.scatter(te_sca_y, y_test, color='r')

# plot train age with actual and predicted value
plt.subplot(2, 3, 4)
score = accuracy_score(y_train, tr_predict)
plt.title('Score: ' + str(score))
plt.scatter(tr_sca_x, y_train, color='r')
plt.scatter(tr_sca_x, tr_predict, color='b')

# plot test age with actual and predicted value
plt.subplot(2, 3, 5)
score = accuracy_score(y_test, test_predict)
plt.title('Score:' + str(score))
plt.scatter(te_sca_x, y_test, color='r')
plt.scatter(te_sca_x, test_predict, color='b')
plt.show()


