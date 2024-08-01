items = [[], "paris", {}, 2, 3.5, "new york", 4, True, 5.5, False]

numbers = list()

for i in items:
    if type(i) == str:
        numbers.append(i)

print(numbers)
