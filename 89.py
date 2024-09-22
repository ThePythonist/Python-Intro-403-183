import random


def generate1(length):
    password = []
    for i in range(length):
        x = str(random.randint(0, 9))
        password.append(x)

    password = "".join(password)
    print(password)


def generate2(length):
    password = ""
    for i in range(length):
        x = str(random.randint(0, 9))
        password += x

    print(password)


def generate3(length):
    password = [str(i) for i in random.sample(range(0, 10), length)]
    password = "".join(password)
    print(password)

generate3(6)
