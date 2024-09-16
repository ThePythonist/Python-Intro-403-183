f = open("words.txt", "r").readlines()
rev_words = f[::-1]

output = "".join(rev_words)
open("rev-words.txt", "w").write(output)
