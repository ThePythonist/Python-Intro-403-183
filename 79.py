# f = open("words.txt").readlines()
# lines = []
#
# for i in f:
#     lines.append(i[:-1])
#
# print(lines)
# ----------------------------------------------------
# f = open("words.txt", "r").read()
# print(f.split("\n"))
# ----------------------------------------------------
f = open("words.txt", "r").read()
f = f.replace("\n", " ")
print(f)
