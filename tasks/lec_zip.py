names = ['Johnie', 'David', 'Maria', 'Roman']
ages = [16, 25, 19, 41]
isTeenager = [True, False, True, False]

users = tuple(zip(names, ages, isTeenager))
print(users)

print('user age:', dict(zip(names, ages)))


def checker(user):
    name, age = user
    return age > 21



can_drink_alcohol = list(filter(checker, zip(names, ages)))
print(can_drink_alcohol)

