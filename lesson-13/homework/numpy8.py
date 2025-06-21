import numpy as np

mat_5x3 = np.random.random((5,3))
mat_3x2 = np.random.random((3,2))
prod_5x2 = np.dot(mat_5x3, mat_3x2)
print("Product of 5x3 and 3x2 matrices:", prod_5x2)