import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[51,52,48,46,95,57,80]
# plt.plot(x,y,'rD')
z=plt.plot(x,y,color="red",marker="D",linestyle="",alpha=1)
print(z)
print(plt.show())