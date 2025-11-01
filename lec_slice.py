import numpy as np

a = [1, 2, 5, 9]
slice = a[0:2:1]
print(slice)

slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)

print()

b = np.array([a, np.array(a) * 3])
print(b)

slice = b[::, 1]
print(slice)

slice = b[1, 2:3:1]
print(slice)