def outerFunc(a,b,c):
    def innerFunc(c,d):
        return c+d
    return innerFunc(a,b)
    return a
result=outerFunc(20,10,25)
print(result)