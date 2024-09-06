def is_number(x):
    return True if type(x) in [int, float] else False


print(list(filter(is_number, [True, 0.5, "Tokyo", 1.2, [], "London", 50, "Madrid"])))
