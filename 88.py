import datetime


def show_age(birth):
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    print(age)


show_age(int(input("Enter your birth year : ")))
