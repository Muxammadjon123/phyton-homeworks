import numpy as np

A_circuit = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
b_circuit = np.array([12, -5, 15])

currents = np.linalg.solve(A_circuit, b_circuit)
print("Currents (I1, I2, I3):", currents)