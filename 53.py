def has_duplication1(word):
    letters = []
    for i in word:
        if i in letters:
            return "Tekrari darad"
        else:
            letters.append(i)

    return "Tekrari nadarad"


# print(has_duplication1("mohammad"))


def has_duplication2(word):
    if len(word) == len(set(word)):
        print("Tekrari nadarad")
    else:
        print("Tekrari darad")


has_duplication2("mohammad")
