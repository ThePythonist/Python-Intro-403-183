f = open("words.txt").read().split("\n")
numbers = []

for line in f:
    if not line.isdigit():
        for character in line:
            if character.isdigit():
                numbers.append(line)
                break

print(numbers)
