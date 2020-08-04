def k(m,n):
    ans=0
    while(m>=n):
        (ans,m)=(ans+1,m-n)
    return (ans)
k(62,6)