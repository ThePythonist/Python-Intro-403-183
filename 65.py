x = int(input("Enter any number to check if its perfect : "))
divs = [i for i in range(1, x) if x % i == 0]
print((lambda x: True if x == sum(divs) else False)(x))  # with lambda

# --------------------------------------------------------------------------

# def func(x):
#     return True if x == sum(divs) else False
# print(func(x))  # without lambda
