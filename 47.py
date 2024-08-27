scores = {
    "mabani computer": 20,
    "zaban omomi": 17,
    "varzesh": 15,
    "riazi omomi 1": 7,
    "andishe eslami 1": 14
}

# scores.keys() # 5 ta
# scores.values() # 5 ta
# scores.items() # 5 ta

for i, j in scores.items():
    if j >= 10:
        print(i, ": Passed")
    else:
        print(i, ": Failed")

# summation = 0
#
# for i in scores.values():
#     summation += i
#
# grade = summation / len(scores)

grade = sum(scores.values()) / len(scores)
print("Grade :", grade)
