import numpy as np

a = np.array([2, 4, 6, 8, 10])
print(a)
b = np.arange(1, 11)
c = np.array([1, 3, 5, 7, 9],dtype=float)
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
ararajk = np.arange(0, 100, 7)
print("Original:", ararajk)
print("Applying boolean condition", ararajk[ararajk > 25])


result = np.concatenate((a, c))
print(result)

print("===========================")
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(f"Array number of dims:", array_example.ndim)
print(f"Array datatype:", array_example.dtype)
print(f"Array shape:", array_example.shape)
print(f"Array size:", array_example.size)
reshaped = np.reshape(array_example, newshape=(8, 3))
print(reshaped)