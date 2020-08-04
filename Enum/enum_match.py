import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 1
if Days.Sun == Days.Tue:
   print('Match')
if Days.Mon != Days.Tue:
   print('No Match')