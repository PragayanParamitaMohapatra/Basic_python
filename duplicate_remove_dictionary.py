def count(elements):
    if elements[-1]=='.':
        elements=elements[0:len(elements)-1]
    if elements in dictionary:
        dictionary[elements]+=1
    else:
        dictionary.update({elements:1})
sent="app sap tap app tap vcv"
dictionary={}
st=sent.split()
for ele in st:
        count(ele)
for allKeys in dictionary:
    print("frequency of allkeys:",allKeys,end="")
    print(":",end="")
    print(dictionary[allKeys],end='')
    print()