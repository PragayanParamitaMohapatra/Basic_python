import enum
class Name(enum.Enum):
    agu=334
    sagu=213
    pogo=123
print("Enum members name is:{}".format(Name.agu.name))
print("Enum members value is:{}".format(Name.agu.value))