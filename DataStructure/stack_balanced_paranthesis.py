"""
use a stack whether or not a string has balanced usage of paranthesis
Ex:
() ,()(),(({[]}))  <-  Balanced
( (),{{{}}},[][]]]  <- not balanced
Balanced Example {[]}
non-balanced Example  (()
non-balanced Example }}
"""
from DataStructure.stack import StackDs
def is_match(p1,p2):
    if p1=="(" and p2==")":
        return True
    elif p1=="{" and p2=="}":
        return True
    elif p1=="[" and p2=="]":
        return True
    else:
        return  False
def is_balanced_paranthesis(paren_string):
    s=StackDs()
    is_balanced=True
    index=0
    while index < len(paren_string) and is_balanced:
        paren=paren_string[index]
        if paren in "({[":
            s.push(paren)

        else:
           if s.is_empty():
              is_balanced=True
           else:
               top=s.pop()
               if not is_match(top,paren):
                   is_balanced=False
        index +=1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
print(is_balanced_paranthesis("({{{[]}}})"))


