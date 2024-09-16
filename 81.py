f1 = open("words.txt", "r").read().split("\n")

open("onelinewords.txt","w").writelines(f1)
