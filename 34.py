# numbers = []
#
# for i in range(5):
#     x = int(input("Enter any number : "))
#     numbers.append(x)
#
# numbers = sorted(numbers)
# print(numbers[-1])

# ------------------------------------------------

# numbers = [-10, -30, -20, -50, -40]
# maximum = numbers[0]  # works for positive and negative numbers !
#
# for i in numbers:
#     if i > maximum:
#         maximum = i
#         print("maximum changed here")
#     else:
#         print("maximum didnt change here")
#
# print(maximum)
# 😒
# ------------------------------------------------

numbers = [10, 30, 50, 20, 40]
print(max(numbers))
print(min(numbers))
