items = [[], (), {}, 2, 3.5, "", 4, True, 5.5, False]

numbers = list()

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
