# num = 1
#
# while num <= 20:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# -----------------------------------------------------

# num = 0
#
# while num <= 20:
#     print(num)
#     num += 2

# -----------------------------------------------------

evens = []
odds = []

for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print("Adad zoj :",evens)
print("Adad fard :",odds)
