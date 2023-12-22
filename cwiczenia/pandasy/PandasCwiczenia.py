import numpy as np
a = np.array([2,4,6,8,10])
print(a)
b = np.arange(1, 11)
print(b.data)
print(b.dtype)
print(b.dtype.itemsize)
arr1 = np.hstack((a, b))

c = 2 * b
arr3 = np.column_stack((b, c))
print(arr3)

array = np.arange(1, 10).reshape(3, 3)
fix = array.astype(float)
print("result", fix)
print(fix.dtype)
print(id(arr3))
ararajk = np.arange(0,100, 7)
print("Original:", ararajk)
print("Applying boolean condition", ararajk[ararajk>25])
