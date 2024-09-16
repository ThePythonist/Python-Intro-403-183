def find_longest1(file):
    lines = file.readlines()
    lines.sort(key=len)
    # print(lines[0])  # min
    print(lines[-1])  # max


def find_longest2(file):
    lines = file.readlines()
    maxlen = len(max(lines, key=len))
    for i in lines:
        if len(i) == maxlen:
            print(i)


f = open("words.txt")
find_longest2(f)
