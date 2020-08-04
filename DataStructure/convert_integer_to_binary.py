"""
use stack data structure to convert the integer values to binary values
"""


from DataStructure.stack import StackDs
def div_by_2(dec_num):
    s=StackDs()
    while dec_num>0:
        rem=dec_num%2
        s.push(rem)
        dec_num=dec_num//2
    bin_num=""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num
