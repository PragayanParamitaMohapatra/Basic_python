# import matplotlib.pyplot as plt
# Name=["Eatload-TimeLine","OnBoarding","User Registration","Main Screen","My Order","Payment Process","Order Confirmed","Food is Being Prepared","Order is Ready","Delivered","My Account","Setting"]
# Duration=["66Days","39Days","6Days","1Days","1Days","7Days","1Days","1Days","2Days","4Days","3Days","11Days"]
# start=["07-01-2020","07-01-2020","28-02-2020","28-02-2020","28-02-2020","02-03-2020","10-03-2020","11-03-2020","12-03-2020","16-03-2020","19-03-2020","24-03-2020"]
# finish=["07-04-2020","28-02-2020","06-03-2020","28-02-2020","28-02-2020","10-03-2020","10-03-2020","11-03-2020","13-03-2020","19-03-2020","23-03-2020","07-04-2020"]
# plt.xlabel("Product Milestone",fontsize=8)
# plt.ylabel('TimeLine')
# plt.title('Corporate Dine Management')
# print(plt.hist([Name,Duration,start,finish],rwidth=1.5,color=["green","yellow","blue","orange"],label=['start','finish']))
# plt.legend()
# plt.show()
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('Eatload.xlsx', header = None ,quoting=2)

data.hist(bins=10)
plt.xlim([0,100])
plt.ylim([50,500])
plt.title("Data")
plt.xlabel("fruits")
plt.ylabel("Frequency")
plt.show()
