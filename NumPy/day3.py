import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10])

c_0 = np.concatenate((a, b))
print(c_0)
root = np.sqrt(a)
print(root)
split = np.split(c_0, 2)
print(split[0], split[1])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
sarr = np.split(arr, 3)
print(sarr[0], sarr[1])

x = np.where(arr % 2 == 0)
print("Index and value of even number: ")
for i in x:
    print(i)