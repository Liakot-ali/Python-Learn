import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.arange(1, 5.5, 0.5)
x2 = np.arange(5, 10)

y1 = np.arange(1, 6)
y2 = np.arange(5, 10)
plt.subplot(2, 1, 1)
plt.plot(x1, x1**2,'-g', label='y=x**x')
plt.plot(x2, x2**2,'--r', label='y=x**x')
plt.legend()

second = plt.subplot(2, 1, 2)
x = np.arange(0, (2*math.pi) + 0.05, 0.05)
y = [math.sin(i) for i in x]
print(x, y)
plt.plot(x, y, label='y=sin(x)')
plt.legend()
second.grid(alpha=0.5, linewidth='0.5', color='black')
plt.show()