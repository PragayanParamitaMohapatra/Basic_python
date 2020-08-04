from array import *
a=([
    [1,2,3,4,5,6],[2,3,4,5,6,7],[1,3,5,7,8,9,],[1,2,3,4,7,8],[2,3,4,5,6,7],[2,3,4,5,6,7]
])
print(a[0])
print(a[1][5])
print(a[2][3]+a[3][3])
print(a[2][3]*a[3][3])
if a[2][1]==a[3][2]:
   print ( 'True')
else:
    print('false')
for r in a:
    for d in r:
        print(d)
print()
