import numpy as np
from numpy import linalg

#a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3,3)
#b = np.array([3, 1, 4, 2, 6, 1, 2, 9, 7]).reshape(3,3)
#print(a+b)

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = np.array([[3, 1, 4],
              [2, 6, 1],
              [2, 9 ,7]])
print("A + B")
x = np.add(A, B)
print(x, "\n")

print('A * B')
y = np.dot(A, B)
print(y, "\n")

print('Determinate of A')
print(linalg.det(A), "\n")

print("Inverse of B")
print(linalg.inv(B), "\n")

print('Eigenvalues of A')
print(linalg.eigvals(A))