
# Write a Python program to find the most common  3 elements and their counts of a specified text.
from collections import Counter
s = 'lkseropewdssafsdfafkpwe'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))
