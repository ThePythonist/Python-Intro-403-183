x = input("Entry : ")

try:
    x = float(x)
    print("Entry is a number")
except ValueError:
    print("Entry is not a number")
