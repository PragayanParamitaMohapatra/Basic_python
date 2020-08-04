import numpy as np
a=np.array([(1,2,3,4),(5,6,7,8)])#contain 4 columns 2 rows
print(a)
#convert into 2 columns 4 rows
a=a.reshape(4,2)
print(a)