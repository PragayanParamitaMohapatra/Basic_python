# Add each character, and it's ordinal, of user's text input, to two lists
s = input("Enter value: ")
l1 = []
l2 = []
l3=[]
for c in s:   # in Python, a string is just a sequence, so we can iterate over it!
    l1.append(c)
    l2.append(ord(c))
    l3.append(int(chr(l1)))
print(l1)
print(l2)
print(l3)