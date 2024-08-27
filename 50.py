# def summation(number):
#     number = str(number)
#     s = 0
#     for i in number:
#         s += int(i)
#
#     return s
#
#
# print(summation(24234))

# ----------------------------------------------
def summation(number):
    number = str(number)
    digits = [int(i) for i in number]
    return sum(digits)


print(summation(24234))
