lines = open("words.txt").readlines()
subwords = []
for i in lines:
    # if i[-4:] == "ing\n":
    if i[-4:-1] == "ing":
        subwords.append(i)

print(subwords)
