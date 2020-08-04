import enum
class Days(enum.Enum):
    sun=1
    mon=2
    tue=3
print("Enum Members are:",end=" ")
for weekdays in(Days):
    print(weekdays,end=" and ")