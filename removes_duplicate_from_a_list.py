def remove(duplicate):
    final_list=[]
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
dup=[1,2,3,2,4,5,6,5,6,7]
s=remove(dup)
print(s)