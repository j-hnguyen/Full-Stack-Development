import numpy as np
arr = np.arange(2, 10).reshape(4, 2)
print(arr, "\n")

a = np.ones((3,3))
a = np.zeros((8,8),dtype=int)
a[1::2,::2] = 1
a[::2,1::2] = 1
print(a, "\n")

List = np.unique([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
print(List, "\n")

x = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
print(x[x>37], "\n")

F = np.array([0, 12, 45.21, 34, 99.91])
F = np.multiply(F, 9/5)
F = np.add (F, 32)
print(F)
#print(9*F/5 + 32)