f = open("words.txt", "r").readlines()
# rev_words = []
#
# for i in f:
#     rev_words.append(i[::-1])
#
# print(rev_words)

rev_words = [i[::-1] for i in f]
print(rev_words)
