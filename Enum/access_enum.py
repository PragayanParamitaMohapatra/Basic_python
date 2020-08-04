import enum
class Days(enum.Enum):
    sun=1
    mon=2
print("Enum members are:",Days['sun'])
print("Enum members are:",Days(1))
