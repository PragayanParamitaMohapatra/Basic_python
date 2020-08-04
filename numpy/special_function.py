import numpy as np
from matplotlib import pyplot as plt
# a=np.array([(1,2,3),(4,5,6)])
# print(np.sqrt(a))
# to find the sin and cosine function we need matplotlib
x=np.arange(0,3*np.pi,0.1)
y=np.tan(x)
print(plt.plot(x,y))
plt.title("Sin function")
plt.legend()
plt.show()
