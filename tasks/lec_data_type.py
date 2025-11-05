x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)
print(z + w)

# Strings
s = 'hello'
print(s[0])

#s[0] = 'H'

# Tuple
t = (1, 2, 9)
print(t)
print(t[0])
#t[0] = 3 нельзя, так как он неизменяемый тип данных

#List
a = [1, 2, 3]
a[0] = 999
print(a)

#Dictionary = dict
d = {'key_1': 4, 2: 'red', 'str': 'hello'}
print(d)

for keys in d.items():
    print(keys[0])
    
#print(d.keys())