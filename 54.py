def is_binary(number):
    for i in number:
        if i not in ("0", "1"):
            return False

    return True


print(is_binary("0001101"))
print(is_binary("0101020"))
