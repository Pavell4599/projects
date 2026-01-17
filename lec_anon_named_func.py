def sum_app(a, b):
    return a + b

print(sum_app(12, 34))

sum_app = lambda a, b: a + b


a = [lambda a, b: f'{a}: {b**2 = }' for _ in range(100)]
print(a[0](99, 7))


import numpy as np
tgs = (np.cos, np.sin, np.tan)
print(tgs[2](45))


maximum = (lambda a, b: a if a > b else b)
print(maximum(9, 87))

