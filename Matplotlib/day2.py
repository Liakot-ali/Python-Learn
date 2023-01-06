import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.arange(1, 5.5, 0.5)
x2 = np.arange(5, 10)

y1 = np.arange(1, 6)
y2 = np.arange(5, 10)
plt.plot(x1, x1**2,'-g', label='y=x**x')
plt.plot(x2, x2**2,'--r', label='y=x**x')

plt.legend()
plt.show()