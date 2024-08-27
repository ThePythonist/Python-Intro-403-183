numbers = []

while True:
    entry = input("Enter any number : ")

    if entry == "exit":
        break

    try:
        entry = float(entry)
        if entry == int(entry):
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        # print("Entry is not a number")
        pass

print(numbers)
