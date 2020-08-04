import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
# Hashing to create a dictionary
Daytype = {}
Daytype[Days.Sun] = 'Sun God'
Daytype[Days.Mon] = 'Moon God'

# Checkign if the hashing is successful
print(Daytype)
print(Daytype =={Days.Sun:'Sun God',Days.Mon:'Moon God'})