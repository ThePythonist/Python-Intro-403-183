num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# print("Bigger :",(lambda x, y: x if x > y else y)(num1, num2))
print("Bigger :", (lambda x, y: max(x, y))(num1, num2))
