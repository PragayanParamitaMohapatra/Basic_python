def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result
print(temperature(20))