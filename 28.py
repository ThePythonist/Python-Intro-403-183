a, b = 0, 1

for i in range(100):
    # c = a
    # a = b
    # b = c+b
    a, b = b, a + b
    print(a)

# -----------------------------------
