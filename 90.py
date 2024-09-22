import random

number = random.randint(1, 10)
chances = 5

print("Hello welcome to number guessing game!")

while chances > 0:
    choice = input("Guess the number : ")
    try:
        choice = int(choice)

        if 0 < choice < 11:
            if choice == number:
                print("You won!")
                break
            elif choice > number:
                print("Try smaller than", choice)
            else:
                print("Try bigger than", choice)
            chances -= 1
        else:
            print("Guess a number between 1-10! Try again")

    except ValueError:
        print("Your guess must be a number! Try again")
else:
    print("Game over! The number was", number)
