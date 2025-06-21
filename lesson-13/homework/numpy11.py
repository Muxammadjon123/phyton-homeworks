import numpy as np

mat_3x3_det = np.random.random((3,3))
det_val = np.linalg.det(mat_3x3_det)
print("Determinant of 3x3 matrix:", det_val)