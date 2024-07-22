info1 = {
    "name": "james",
    "job": "mi6 agent",
    "country": "england",
    "age": 35
}

info2 = {
    "city": "london",
    "emial": "jamesbond@gmail.com",
    "age": 37
}

# info1.setdefault("age",37) # update nemikonad !
# print(info1)

info1.update(info2)
print(info1)
