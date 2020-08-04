#Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[20,40,60,65,70,75,80]
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather")
z=plt.plot(x,y,color="green",linewidth=3,linestyle="dotted")
print(z)
print(plt.show())
