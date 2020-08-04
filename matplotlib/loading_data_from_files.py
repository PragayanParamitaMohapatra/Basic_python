from matplotlib import pyplot as plt
import csv
import numpy as np

# x=[]
# y=[]
# with open('data.txt','r') as csvfile:
#     plots=csv.reader(csvfile,delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
x,y=np.loadtxt('data.txt',delimiter=',',unpack=True)
print(plt.plot(x,y,label="loaded from file"))
plt.title("Data Visualization")
plt.xlabel("x")
plt.ylabel("y") 
plt.legend()
plt.show()