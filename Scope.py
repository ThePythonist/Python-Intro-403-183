balance = 0  # global
print(balance)


def variz(x):
    print("dar hale variz ...")
    global balance
    balance += x  # local


variz(500)
print(balance)
