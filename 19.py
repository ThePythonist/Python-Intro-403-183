students = ["artin", "shayan", "reza"]
age = int(input("Enter your age : "))

if age >= 18:
    name = input("Enter your name : ")
    students.append(name)
else:
    print("You are not old enough")

print("Students : ", students)
