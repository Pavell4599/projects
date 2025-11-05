import numpy as np

g = 9.8
N = 10

x0 = 5
y0 = 7
v0x = 4
v0y = 3

t = np.linspace(0, 5, N)
x = x0 + v0x * t
y = y0 + v0y * t - g * t**2 / 2

output = np.zeros((N, 3))
output[:, 0], output[:, 1], output[:, 2] = t[:], x[:], y[:]

print(output)