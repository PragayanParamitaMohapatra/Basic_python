# Count number of occurrences of a given substring using start and end


string = "Python is awesome, isn't it?"
substring = "i"
# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)
print("The count is:", count)