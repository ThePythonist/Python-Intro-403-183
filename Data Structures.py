# 1 - Tuple

# names = ("ali", "kiarash", "amir", "saman")
# print(type(names))
# print(names[1:3]) # indexing darad

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# t3 = t2 + t1  # jam pazir ast
# print(t3)  # tartib mohem ast

# t3 = (10,20,10,10,30,40) # tekrari ghabol mikonad
# print(t3)

# items = ("ekbatan", "janat abad", 120, 5, 5.5, "@") # mahdodiat type nadarim
# print(items)

# items = (10, 20, "Python", "Java", (1, 2, 3))  # dakhel sakhteman dade mitavan sakhteman dade dasht
# print(items[4][-1])

# t = ("sony","apple","sony","samsung","asus")
# print(t.count("apple"))

# --------------------------------------------------------------------------------------------------------------------------
# 1 - Set

# s = {10, 445, 9, -5, 5, 6, 7, -1, 1, 2, 3}
# print(s[0]) #index nadarad !
# print(s) # tartib nadarad !

# s1 = {10,20,30}
# s2 = {40,50,60}
# print(s1+s2)

# s = {1,2,3,1,4,5,6,1}
# print(s)

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}

# print(s2.union(s1)) # meghdari ra barmigadanad
# s1.remove(3) # meghdari ra bar nemigardanad
# print(s1)
# s1.add(4) # meghdari ra bar nemigardanad
# print(s1)

# --------------------------------------------------------------------------------------------------------------------------
# 3 - List

# names = ["aria", "pedram", "zahra", "melisa"]
# print(type(names))
# print(names[-1]) # indexing midahad

# lst1 = [1,2,3,4,5]
# lst2 = [10,20,30,40,50]
# print(lst2+lst1) # jam pazir hast - tartib ham darad

# lst = [10, 30, 30, 40, 50] # tekrari ghabol mikonad
# lst[1] = 20 # mutable ast ! ( ghabel taghir )
# print(lst)

# lst = [10, 30, 20, 40, 70, 50, 60]

# lst.append(40) # ezafe kardan item
# print(lst)

# lst.insert(0, 40) # ezafe kardan itemm be yek position khas
# print(lst)

# lst.sort() # moratab kardan list
# print(lst)

# print(lst.count(50)) # shomaresh

# lst.reverse() # baraxesh mikone
# print(lst)

# print(lst.index(70)) # index item khaste shode ra barmigardone

# --------------------------------------------------------------------------------------------------------------------------
# 4 - Dictionary

# d = {"name": "mamad", "age": 17, "city": "tehran"}
# print(d)

# d = {"name": "mamad", "age": 17, "city": "tehran", "name": "parsa"}
# print(d)

# info = {"name": "ahmad", "weight": 60, "age": 60}
# print(info)

# info = {"name": "mamad", "age": 17, "city": "tehran", "name": "parsa"}
# print(info["city"])

# info["age"] = 20
# print(info)

# info.setdefault("height", 179)
# print(info)

# info1 = {"name": "mamad", "age": 17, "city": "tehran", "name": "parsa"}
# info2 = {"address": "ekbatan", "bloodtype": "O+", "job": "programmer"}
# info1.update(info2)
# print(info1)

info = {"name": "mamad", "age": 17, "city": "tehran", "name": "parsa"}
# print(info.keys())
# print(info.values())
# print(info.items())

print(list(info.items())[1])
