def trace(f):
    f.indent=0
    def g(x):
        print('|  '* f.indent+'|--',f.__name__,x)
        f.indent +=1
        value=f(x)
        print( '|  ' * f.indent + '|--','return',repr(value))
        f.indent -=1
        return value
    return g
def fib(g):
    pass
fib(3)
trace(fib(3))