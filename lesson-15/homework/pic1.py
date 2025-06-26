import numpy as np
import matplotlib.pyplot as plt


x=np.arange(1,100,5)
y=x**2-4*x+4

plt.plot(x,y)
plt.title(f"The function of (x**2-4*x+4)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()