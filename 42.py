numbers = []
for i in range(3):
    entry = input("Enter any number : ")
    try:
        entry = float(entry)
        numbers.append(entry)
    except ValueError:
        # print("Entry is not a number")
        pass

print(numbers)
