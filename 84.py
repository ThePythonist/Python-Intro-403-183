f = open("words.txt").read().split("\n")
numbers = []

for i in f:
    if i.isdigit():
        numbers.append(i)

print(numbers)
