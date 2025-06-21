import numpy as np

mat_5x5_sum = np.random.random((5,5))
row_sums = mat_5x5_sum.sum(axis=1)
col_sums = mat_5x5_sum.sum(axis=0)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)