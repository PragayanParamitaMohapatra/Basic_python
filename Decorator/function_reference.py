# # The
# output
# of
# a
# function is also
# a
# reference
# to
# an
# object.Therefore
# functions
# can
# return references
# to
# function
# objects.


def f(x):
    def g(y):
        return y + x + 3

    return g


nf1 = f( 1 )
nf2 = f( 3 )

print( nf1( 1 ) )
print( nf2( 1 ) )
