number = int(input("How many files do you want : "))
frmt = input("What type of file do you want : ")

for i in range(number):
    open(f"file{i+1}.{frmt}", "w")
