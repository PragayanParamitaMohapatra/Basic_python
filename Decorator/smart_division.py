def smart_division(func):
    def inner(a, b):
        if b == 0:
            print("hey stupid zero cant't be divisible")
        else:
            return func(a, b)

    return inner


@smart_division
def division(a, b):
    return a / b


print(division(10, 2))
print(division(5, 0))
print(division(4, 2))
