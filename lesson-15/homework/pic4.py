import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(1,10,100)
y=np.random.uniform(1,10,100)


colors=np.random.rand(100)
markers=["<",">","*","o","D","H"]

for i,m in enumerate(markers):
    idx=np.arange(100)%len(markers)==i
    plt.scatter(x[idx],y[idx],c=colors[idx],cmap='viridis',marker=m,label=f"Marker:{m}")
    
plt.title("Random Scatter Plot (uniform distribution)")
plt.xlabel("X qiymatlar (0–10)")
plt.ylabel("Y qiymatlar (0–10)")
plt.grid(True)
plt.legend()
plt.colorbar(label="Color intensity")
plt.show()