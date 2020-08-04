import matplotlib.pyplot as plt
blood_sugar_men=[113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_sugar_women=[67,98,89,120,133,150,84,69,89,79,120,112,100]
blood_sugar_can=[113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_sugar_wan=[67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.xlabel("sugar range")
plt.ylabel('Total no. of patients')
plt.title('Blood sugar analysis')
print(plt.hist([blood_sugar_men,blood_sugar_women,blood_sugar_can,blood_sugar_wan],bins=[80,100,125,150],rwidth=0.50,color=["green","yellow","blue","orange"],label=['men','women']))
plt.legend()
plt.show()