import matplotlib.pyplot as plt
import numpy as np


a = 1
b = -4
c = 3

x = np.linspace(-5, 5, 100)

y = a * x**2 + b * x + c

plt.figure(figsize = (8, 8))
plt.plot(x, y, label = f'$y = {a}x^2 + {b}x + {c}$')


plt.title('График параболы')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.axhline(0, color = 'black', linewidth = 0.5)
plt.axvline(0, color = 'black', linewidth = 0.5)
plt.legend()
plt.show()


    




