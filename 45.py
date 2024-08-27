info = {
    "name": "Bayern Munich",
    "city": "Munich",
    "manager": "Vincent Kompany",
    "ucls": 6,
    "bundesligas": 32
}

key = input("Seach for key : ")

# if key in info:
#     print(info[key])
# else:
#     print("Key not found")

try:
    print(info[key])
except KeyError:
    print("Key not found")
