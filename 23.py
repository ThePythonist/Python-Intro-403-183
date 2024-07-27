# num = int(input("Enter any number : "))
#
# if num % 2 == 0 and 99 < num < 1000:
#     print(True)
# else:
#     print(False)
# -----------------------------------------------
num = input("Enter any number : ")

if len(num) == 3 and int(num) % 2 == 0:
    print(True)
else:
    print(False)
