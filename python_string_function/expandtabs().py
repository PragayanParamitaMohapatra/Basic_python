"""The expandtabs() method returns a copy of string with all
tab characters '\t' replaced with whitespace characters
until the next multiple of tabsize parameter"""


str = 'xyz\t12345\tabc'
# default tabsize is 8
result = str.expandtabs()
print(result)