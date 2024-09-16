lines = open("words.txt").readlines()
subwords = []
for i in lines:
    if i[0:3] == "sub":
        subwords.append(i)

print(subwords)