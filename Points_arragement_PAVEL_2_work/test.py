import numpy as np

a = np.linspace(1, 9, 7)
b = np.linspace(1, 9, 7)

c = np.concatenate((a, b))
print(c)