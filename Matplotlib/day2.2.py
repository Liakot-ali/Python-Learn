import random

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
z = np.random.randint(50, 1000, 13)
cmap = np.random.randint(1, 100, 13)
colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan", "magenta"])
plt.scatter(x, y, s=z, marker='o', c=cmap, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
z = np.random.randint(50, 1000, 15)
cmap = np.random.randint(1, 100, 15)
colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan","magenta", "green", "blue"])
plt.scatter(x, y, s=z, alpha=0.7, c=cmap, cmap='nipy_spectral')
plt.colorbar()

plt.show()
