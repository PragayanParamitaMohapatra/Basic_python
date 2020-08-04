from num2words import num2words
def factorial(num):
    if num ==1:
        return num
    else:
        return num*factorial(num-1)
num=5
f=factorial(num)
print(num2words(f,ordinal=True,lang='en'))
