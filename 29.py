numbers = [
    26, 23, 21,
    10, 11, 12,
    3, 5, 7, 18
]

evens = []

for i in numbers:
    if i % 2 == 0:
        evens.append(i)

print(evens)
