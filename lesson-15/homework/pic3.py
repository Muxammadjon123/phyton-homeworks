import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,40)
top_left=x**3
top_right=np.sin(x)
bottom_left=np.e**x
bottom_right=np.log(x+1)

plt.subplot(2,2,1)
plt.plot(x,top_left,c='r')
plt.title("x^3")

plt.subplot(2,2,2)
plt.plot(x,top_right,c='k')
plt.title("sin(x)")

plt.subplot(2,2,3)
plt.plot(x,bottom_left,c='g')
plt.title("e^x")

plt.subplot(2,2,4)
plt.plot(x,bottom_right,c='b')
plt.title("log(x+1)")

plt.tight_layout()
plt.show()