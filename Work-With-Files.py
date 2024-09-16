# f = open("cars.txt")
# print(f.read())
#
# print("*"*50)
#
# print(f.tell())
# print("*"*50)
#
# f.seek(4)
# print(f.read())

# ------------------------------------

# f = open("cars.txt")
# print(f.readline())
# print(f.readline())
#
# for i in range(5):
#     print(f.readline())

# ------------------------------------

# f = open("cars.txt")
# print(f.readlines())

# ------------------------------------

# f = open("cars.txt", "w")
# f.write("hello")
# f.write("ali")
# names = ("ford", "toyota", "benz", "pagani")
# names2 = []

# for i in names:
#     names2.append(i + "\n")

# print(names2)
# f.writelines(names2)

# ------------------------------------

f = open("cars.txt", "a+")
f.seek(0)

print(f.readlines())
f.write("lamborghini")

f.seek(0)
print(f.readlines())
