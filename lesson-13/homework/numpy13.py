import numpy as np

mat_3x3_mv = np.random.random((3,3))
vec_3 = np.random.random(3)
mv_product = np.dot(mat_3x3_mv, vec_3)
print("Matrix-vector product:", mv_product)