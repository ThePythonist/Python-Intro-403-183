def is_binary(x):
    for i in x:
        if i not in ["0", "1"]:
            return False

    return True


print(list(filter(is_binary, ["01101", "24", "52", "10"])))
