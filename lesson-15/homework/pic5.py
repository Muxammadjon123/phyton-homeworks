import numpy as np
import matplotlib.pyplot as plt


x=np.random.normal(loc=0.0, scale=1.0, size=1000)
plt.hist(x,bins=30,alpha=0.6,density=True,edgecolor='k',color='r')
plt.title("Histogram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()