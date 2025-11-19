# zip() - итератор, объединяющий элементы из
# нескольких источников данных

names = ["John", "David", "Maria", "Richard"]
ages = [16, 25, 19, 41]
isTeenager = [True, False, True, False]

users = list(zip(names, ages, isTeenager))
print(users)

print("User age:", dict(zip(names, ages)))