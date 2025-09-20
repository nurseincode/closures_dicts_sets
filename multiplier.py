def multiply(multiplier): # multiply: a function factory that will generate custom functions
    return lambda x: x * multiplier

doubler = multiply(2)
tripler = multiply(3)

print(doubler(10))
print(tripler(5))



