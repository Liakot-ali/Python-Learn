
import numpy as np
a = np.array([[5, 2, 6, 10], [1, 2, 3, 4], [5, 4, 7, 8]], dtype='int32')
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a[0, :]) # Access row 0 values
print(a[:, 3]) # Access column 3 values
print(a.itemsize)
print(a.nbytes)


print(np.identity(5))
mat0 = np.zeros((5, 7))
print(mat0)
mat1 = np.ones((2, 4))
print(mat1)
matx = np.full((3, 4), 45)
print(matx)

matrandom = np.random.rand(2, 4)
print(matrandom)
matran = np.random.random_sample(matx.shape)
print(matran)

matranx = np.random.randint(0, 9, (4, 5))
print(matranx)


# output like this
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# using numpy array

print("\nAssignment")
output = np.ones((5, 5), 'int32')
zero = np.zeros((3, 3), dtype='int32')
zero[1, 1] = 9
output[1 : 4, 1 : 4] = zero
print(output)