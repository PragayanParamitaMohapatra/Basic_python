# lst=list('123456')
# print(lst)
# lst[0]=lst[5]=0
# lst[3]=lst[-2]
# print(lst)

# a=[3,4,5,6,4,7]
# print(a.index(3))
# print(a.index(4))

# for i in range(10,1):
#     print(i,end='')
import itertools
lst=[[2,4,3],[1,5,6]]
new_list=list(itertools.chain(*lst))
print(new_list)