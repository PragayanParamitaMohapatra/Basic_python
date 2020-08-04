import random
import string

# printing lowercase
letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing uppercase
letters = string.ascii_uppercase
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing letters
letters = string.ascii_letters
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing digits
letters = string.digits
print ( ''.join(random.choice(letters) for i in range(10)) )

# printing punctuation
letters = string.punctuation
print ( ''.join(random.choice(letters) for i in range(10)) )
#random.choice() is used to generate strings in which characters may repeat,
# while random.sample() is used for non-repeating characters.