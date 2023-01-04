import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 5, 10, 13, 15, 28])
y = np.array([0, 25, 10, 15, 21, 10])
font1 = {'family' : 'serif' , 'color' : 'blue' , 'size' : 20}
font2 = {'family' : 'serif' , 'color' : 'darkred' , 'size' : 15}

# plt.title("Sample Plot", loc='right', c='r', fontdict=font1)
# plt.xlabel("X axis", fontdict=font2)
# plt.ylabel("Y axis", fontdict=font2)

# Subplot 1
plt.subplot(1, 2, 1)
plt.title('Subplot 1')
plt.plot(x, y, 'g', ms='10', mec='r', mfc='b', lw='5', ls='-')

# Subplot 2
plt.subplot(1, 2, 2)
plt.title('Subplot 2')
plt.plot(y, x, ls='-', lw='5')

plt.show()

