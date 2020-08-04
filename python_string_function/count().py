# In simple words, count() method searches the substring in the given string and returns how many times the substring is present in it.
# It also takes optional parameters start and end to specify the starting and ending positions in the string respectively
# string.count(substring, start=..., end=...)


string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
print("The count is:", count)