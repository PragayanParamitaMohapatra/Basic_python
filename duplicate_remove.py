def unique_str(str):
    str_list=str.split()
    uniue=set(str_list)
    for str in uniue:
        print(str_list.count(str))
if __name__=='__main__':
    str1="apple mango apple spam mango"
    unique_str(str1)

