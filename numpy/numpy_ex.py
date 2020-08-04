#memory occupation
#as compare to list nympy array is take less memory and more convinient
#faster than list
import  numpy as np
import  sys
import time

s=range(1000)
print(sys.getsizeof(5)*len(s))
D=np.arange(1000)
print(D.size*D.itemsize)