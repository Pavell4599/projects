import numpy as np
from task_1_constants import *


hh = 100
a = np.radians(45)
B= np.radians(35)
V = np.sqrt((g * hh * np.tan(B) ** 2) / (2 * np.cos(a) ** 2 * (1 - np.tan(B) * np.tan(a))))

T = 200
ee = 300
# N = 2 / np.sqrt(np.pi) * np.sqrt(h) * (k * T) ** 1.5 * e ** (ee / (k * T)) * ee ** (T / 2)

print()
print(V)
# print(N)
print()