from collections import namedtuple
Car=namedtuple('Car','color mileage')
my_car=Car('red',3218.5)
print(my_car.mileage)