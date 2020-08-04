import matplotlib.pyplot as plt
import numpy as np
company=["GOOGLE","AMAZON","MICROSOFT","FACEBOOK"]
revenue=[50,60,40,70]
profit=[40,2,34,12]
xpos=np.arange(len(company))
plt.ylabel("revenue(Billionare")
plt.title("US tech stocks")
print(plt.bar(xpos-0.2,revenue ,width=0.3,label="Revenue"))

print(plt.bar(xpos+0.2,profit ,width=0.3,label="Profit"))
plt.xticks(xpos,company)
plt.legend()
plt.show()