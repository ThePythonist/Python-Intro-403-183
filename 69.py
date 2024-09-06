def find_longest1(arg):
    words = text.split()
    lengths = []

    for i in words:
        lengths.append(len(i))

    maxlen = max(lengths)

    for i in words:
        if len(i) == maxlen:
            print(i)


def find_longest2(arg):
    words = text.split()
    words = sorted(words, key=len)
    # words.sort(key=len)
    print(words[-1])


def find_longest3(arg):
    words = text.split()
    print(max(words, key=len))


text = "python is a good programming language"
find_longest3(text)
