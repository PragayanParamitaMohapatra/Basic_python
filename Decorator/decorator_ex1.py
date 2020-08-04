def decor(func):
    def inner(name):
        if name == 'gudu':
            print("Hello", name, "bad morning")
        else:
            func(name)

    return inner


@decor

def wish(name):
    print("Hello", name, "Good Morning")


wish("gudi")
wish("gudu")
wish("gulu")
