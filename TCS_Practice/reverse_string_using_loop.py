str = "guddi"
rev_str = []
index_str = len( str )
while index_str > 0:
    rev_str += str[index_str - 1]
    index_str = index_str - 1
print( rev_str )
