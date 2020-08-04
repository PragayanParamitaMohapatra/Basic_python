def anagram(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    pos=0
    match=True
    while pos < len(s1) and match:
        if l1[pos]==l2[pos]:
            pos+=1
        else:
            match=False
    return match
print(anagram('abcd','bacd'))
