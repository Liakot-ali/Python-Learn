import numpy as np
from pathlib import Path
# Numpy Mathematics
a = np.array([2, 5, 8, 9, 4])
b = a + 2
print(a, b)
print(a ** 3)
print(a * 5)
print(a - 3)

sin = np.sin(a)
cos = np.cos(a)
tan = np.tan(a)
print(sin, '\n', cos, '\n', tan)

# Linear Algebra
a = np.full((3, 3), 3) # a = nxm & b = mxp
b = np.full((3, 3), 5)
mul = np.matmul(a, b)
print(mul)
a = np.identity(3)
b = np.identity(5)
det_a = np.linalg.det(a)
det_b = np.linalg.det(b)
print(det_b, det_b)

# Statistics
a = np.array([2, 5, 8, 9, 4, 10])
b = np.stack([a, a, a, a])
print(b)
sum = np.sum(b, axis=0) # Here, axis = 0, horizontal sum, axis = 1, vertical sum
print("Horizontal Sum :", sum)
sum = np.sum(b, axis=1)
print("Vertical Sum :", sum)

min = np.min(b, axis=0)
print("Horizontal Min :", min)
min = np.min(b, axis=1)
print("Vertical Min :", min)

# Reshape
b = np.reshape(a, (2, 3)) # must be (n*m = total_element)
print("After reshape :\n", b)
h_stack = np.hstack([a, a, a, a])
print("Horizontal stack :", h_stack)
v_stack = np.vstack([a, a, a, a])
print("Vertical Stack :", v_stack)

# Load data form file
fw = open("text.txt", 'w')
fw.write("Liakot, Shuvo, Rajul, Bappy, Akkas, Fahad")
fw.close()

filedata = np.genfromtxt("text.txt", delimiter=' ,', dtype='S')
print(filedata)
