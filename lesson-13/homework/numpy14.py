import numpy as np

A_sys = np.random.random((3,3))
b_sys = np.random.random(3)
x_sol = np.linalg.solve(A_sys, b_sys)
print("Solution of Ax = b:", x_sol)