import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots()
square, = plt.plot([], [], '-', lw=4, color = '#FFFF38')
alpha = np.linspace(0, 2 * np.pi, 250)
plt.axis('equal')
plt.grid()
ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5)
edge = 3
def update(alpha):
    x = np.array([-edge, -edge, edge, edge, -edge])
    y = np.array([-edge, edge, edge, -edge, -edge])
    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)
    square.set_data(X, Y)
    return square

ani = FuncAnimation(fig, 
                    update, 
                    frames=alpha, 
                    interval= 40) 

ani.save('rotate_square_2.gif', writer="pillow", dpi = 100)









