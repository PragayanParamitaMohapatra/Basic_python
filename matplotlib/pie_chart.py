import matplotlib.pyplot as plt
expns_value=[500,450,380,430,550]
exp_labels=['HomeRent','food','phone','grocery','electricity']
plt.axis('equal')
print(plt.pie(expns_value,labels=exp_labels,radius=1.5,autopct="%0.1f%%",shadow=True,explode=[0,0.1,0.1,0,0],startangle=180))
plt.show()