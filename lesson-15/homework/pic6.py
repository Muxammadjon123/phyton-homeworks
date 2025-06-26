import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

plt.colorbar(surf, ax=ax, shrink=0.6, aspect=10)

ax.set_title(r"$f(x, y) = \cos(x^2 + y^2)$")
ax.set_xlabel("X o‘qi")
ax.set_ylabel("Y o‘qi")
ax.set_zlabel("Z = f(x, y)")

plt.tight_layout()
plt.show()
