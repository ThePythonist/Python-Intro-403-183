# def make_dict1(word):
#     chars = {}
#     for i in range(len(word)):
#         chars.setdefault(i, word[i])
#
#     print(chars)
#
#
# make_dict1("python")

def make_dict2(word):
    characters = word
    indexes = range(len(word))
    print(dict(zip(indexes, characters)))


make_dict2("python")
