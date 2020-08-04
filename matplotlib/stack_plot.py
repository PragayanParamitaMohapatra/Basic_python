from matplotlib import pyplot as plt
days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

print(plt.plot([],[],label='sleeping',color='m',linewidth=5))
print(plt.plot([],[],label='eating',color='c',linewidth=5))
print(plt.plot([],[],label='working',color='r',linewidth=5))
print(plt.plot([],[],label='playing',color='k',linewidth=5))

print(plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k']))
plt.xlabel('x-axix')
plt.ylabel('y-axis')
plt.title('StackPlot')
plt.legend()
plt.show()
