import numpy as np

rand_5x5 = np.random.random((5,5))
norm_5x5 = (rand_5x5 - rand_5x5.min()) / (rand_5x5.max() - rand_5x5.min())
print("Normalized 5x5 matrix:", norm_5x5)