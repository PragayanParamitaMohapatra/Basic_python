import string
def solve(s):
    return ''.join(i.capitalize() for i in s.split(' '))
s1='guddi is a good girl'
print(solve(s1))