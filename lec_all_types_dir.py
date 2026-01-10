import numpy as np


a = 'popa'
b = [1, 2, 3]
c = 3
d = 4.3
e = np.zeros(5)
f = {'one': '333', 9: 'popa'}
g = (1, 6, 7)

print(dir(a))
print()
print(dir(b))
print()
print(dir(c))

def popa():
    pass

class Popa:
    pass

p = Popa()

print(dir(popa))
print()
print(dir(Popa))
print()
print(dir(p))


b = []
c = []
print(b is c)