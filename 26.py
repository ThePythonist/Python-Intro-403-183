# x = input("Type something : ")
#
# while x != "exit":
#     print(x)
#     print("-" * 50)
#     x = input("Type something : ")
#
# else:  # faghat 1 bar ejra mishe
#     print("👋👋")

# -------------------------------------------------

flag = 1

while flag:
    x = input("Type something : ")

    if x == "exit" or x == "quit":
        flag = 0

    print(x)
    print("-" * 50)

else:  # faghat 1 bar ejra mishe
    print("👋👋")
