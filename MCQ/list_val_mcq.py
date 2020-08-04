value=[1,2,3,4]
data=0
try:
    data=value[4]
except IndexError:
    print("pi",end="")
except:
    print("pythonin",end="")