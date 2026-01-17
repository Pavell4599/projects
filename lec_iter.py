# a = [0, 1, 2, 4, 6]
# b = iter(a)
a = range(3)

print(id(a))
print(type(a))

new_a = iter(a)
print(new_a)
print(id(new_a))
print(type(new_a))

print(next(new_a))

