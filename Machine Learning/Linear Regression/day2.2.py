# Implementing linear regression using scipy.stats sub-package
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_test = pd.read_csv('test.csv')
df_train = pd.read_csv('train.csv')

x_train = df_train['x'].to_numpy()
y_train = df_train['y'].to_numpy()
x_test = df_test['x'].to_numpy()
y_test = df_test['y'].to_numpy()

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x_train, y_train)
plt.scatter(x_train, y_train)


def myfunc(x):
    return slope * x + intercept


model = list(map(myfunc, x_test))
plt.plot(x_test, model, color='r')
plt.show()
