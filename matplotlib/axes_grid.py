import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,32,56,64]
min_t=[43,42,32,34,45,50,48]
avg_t=[45,48,48,46,40,42,41]
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weather")
print(plt.plot(days,max_t,label="max",color="red"))
print(plt.plot(days,min_t,label="min",color="yellow"))
print(plt.plot(days,avg_t,label="avg",color="green"))
plt.legend(shadow=True,fontsize="small")
plt.grid()
plt.show()