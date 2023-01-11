import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as ss
from scipy import constants as sc
# Standard Deviation, Variance, Mean, Median form numpy
# mode from scipy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

print(np.std(ages))
print(np.var(ages))
print(np.mean(ages))
print(np.median(ages))

# Percentile
arr = [25, 4, 15, 10, 2]
print(np.percentile(arr, 60))
print(sc.liter)

# Normal Distribution
plt.subplot(1, 2, 1)
num = np.random.normal(10, 100, 100000)
plt.hist(num, 1000)

plt.subplot(1, 2, 2)
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()
