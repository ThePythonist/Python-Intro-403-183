# people = {
#     "johhny depp": 61,
#     "tom hanks": 68,
#     "al pacino": 84,
#     "brad pitt": 60,
#     "zidane": 52,
# }
#
# maxage = max(people.values())

# for i in people:
#     if people[i] == maxage:
#         print(i,":",people[i])

# for a, b in people.items():
#     if b == maxage:
#         print(a, ":", b)

# ===================================================

test = {
    "johnny depp": {"age": 61, "height": 178},
    "brad pitt": {"age": 61, "height": 178},
    "tom hanks": {"age": 61, "height": 178},
}

for a, b in test.items():
    print(b["age"])
