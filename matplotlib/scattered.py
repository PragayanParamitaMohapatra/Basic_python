from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7]
y=[7,5,6,8,4,3,5]
print(plt.scatter(x,y,label='skitscat',color='r',s=25,marker='o'))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("scattered plot")
plt.legend()
plt.show()
