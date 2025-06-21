import numpy as np

def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

F = np.array([32, 68, 100, 212, 77])
vectorized_converter = np.vectorize(fahrenheit_to_celsius)
C = vectorized_converter(F)

print("Celsius:", C)