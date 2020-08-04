n=input("Stirngs:")
c=0
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in vowel:
        c=c+1
print("vowels are",c)