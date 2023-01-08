import matplotlib.pyplot as plt
import numpy as np

# Bar
items = np.array(['Shirts', 'T-Shirts', 'Jacket', 'Hoddie', 'Pangabi'])
cnt = np.array([5, 10, 3, 2, 3])
colors = np.array(['red', 'green', 'yellow', 'blue', 'pink'])

# Vertical Bar
plt.subplot(2, 2, 1)
plt.bar(items, cnt, width=0.5, color=colors)

# Horizontal bar
plt.subplot(2, 2, 2)
plt.barh(items, cnt, color='red', height=0.6)

# Histogram
plt.subplot(2, 2, 3)
x = np.random.normal(170, 10, 250)
# print(x)
plt.hist(x, color='red', rwidth=0.3)

# Pie
plt.subplot(2, 2, 4)
plt.pie(cnt, labels=items, colors=colors, explode=[0.1, 0.2, 0, 0, 0.3], shadow=True, startangle=67, autopct='%0.2f')
# plt.legend()

plt.show()