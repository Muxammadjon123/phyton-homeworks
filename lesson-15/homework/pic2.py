import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
sin_x=np.sin(x)
cos_x=np.cos(x)

plt.plot(x,sin_x,'r--',label='sin(x)')
plt.plot(x,cos_x,'g:',label='cos(x)')
plt.legend()
plt.show()