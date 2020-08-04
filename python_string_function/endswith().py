# The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
# str.endswith(suffix[, start[, end]])
# The endswith() takes three parameters:
        # suffix - String or tuple of suffixes to be checked
        # start (optional) - Beginning position where suffix is to be checked within the string.
        # end (optional) - Ending position where suffix is to be checked within the string.
text = "Python is easy to learn."
result = text.endswith('to learn')
print(result)
result = text.endswith('to learn.')
print(result)
result = text.endswith('Python is easy to learn.')
print(result)