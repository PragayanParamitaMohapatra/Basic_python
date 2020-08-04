lst=[[1,2,3],
     [4,5,6],
     [7,8,9]]
lst_com=[lst[i][len(lst)-1-i] for i in range(len(lst))]
print(lst_com)