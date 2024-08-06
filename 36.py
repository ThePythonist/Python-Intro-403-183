# pythons = ["arman", "sepehr", "ali", "kiana"]
# icdls = ["kiana", "parsa", "ali", "mahdyar", "kian"]
# common = []
#
# for i in pythons:
#     for j in icdls:
#         if i == j:  # 20 bar barresi mishe
#             # print(i) # 2 bar
#             common.append(i)
#
# print(common)

# ============================================================

# pythons = ["arman", "sepehr", "ali", "kiana"]
# icdls = ["kiana", "parsa", "ali", "mahdyar", "kian"]
# common = []
#
# for i in pythons:
#     if i in icdls:  # 4 bar
#         print(i)

# ============================================================

pythons = ["arman", "sepehr", "ali", "kiana"]
icdls = ["kiana", "parsa", "ali", "mahdyar", "kian"]
common = [i for i in pythons if i in icdls]
print(common)
