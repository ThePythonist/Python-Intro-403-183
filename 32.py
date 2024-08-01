# numbers = []
#
# for i in range(5):
#     x = int(input('Enter any number : '))
#     if 0 < x < 11:
#         numbers.append(x)
#
# print(numbers)

# ----------------------------------------------
numbers = []

while len(numbers) != 5:
    x = int(input('Enter any number : '))
    if 0 < x < 11:
        numbers.append(x)

print(numbers)
