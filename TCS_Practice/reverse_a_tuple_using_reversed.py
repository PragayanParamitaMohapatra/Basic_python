def tup_reverse(t1):
    t2 = ()
    for ele in reversed( t1 ):
        t2 = t2 + (ele,)
    print( t2 )


t1 = ('a', 'b', 'c', 'd')
tup_reverse( t1 )
