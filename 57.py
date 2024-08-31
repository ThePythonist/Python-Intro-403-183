def even_or_odd(number):  # func 2
    print("entry is even") if number % 2 == 0 else print("entry is odd")


def is_number(entry):  # func 1
    try:
        entry = int(entry)
        print("entry is a number")
        even_or_odd(entry)  # calling func 2
    except ValueError:
        print("entry is not a number")


is_number(input("Entry : "))
