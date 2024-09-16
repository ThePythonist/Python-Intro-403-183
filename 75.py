lines = open("words.txt").readlines()
five_letters = []

for i in lines:
    if len(i) == 6:
        five_letters.append(i)

open("fiveletters.txt", "w").writelines(five_letters)
print("Finished")
