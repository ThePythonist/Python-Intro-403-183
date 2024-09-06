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
    characters = word # p y t h o n
    indexes = range(len(word)) # 0 1 2 3 4 5
    print(dict(zip(indexes, characters)))


make_dict2("python")
