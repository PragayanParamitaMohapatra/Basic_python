from numpy import *

m = array( [['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
            ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
            ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
            ['Sun', 13, 15, 19, 16]] )
# axis value of a column is 1
m_c = insert( m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1 )

print( m_c )