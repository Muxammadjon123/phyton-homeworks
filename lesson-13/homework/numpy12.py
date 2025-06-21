import numpy as np

A = np.random.random((3,4))
B = np.random.random((4,3))
prod_A_B = np.dot(A, B)
print("Product of A(3x4) and B(4x3):", prod_A_B)