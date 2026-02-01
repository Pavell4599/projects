import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots()

square, = plt.plot([], [], '-', lw=1.5, color = 'blue')
plt.axis('equal')
plt.grid()

square_side = 5
R = np.sqrt(2) * square_side / 2
frames_count = 400
frames = np.arange(frames_count)
phi_0 = np.linspace((1 * np.pi) / 4, (21 * np.pi) / 4, frames_count)
phi_1 = np.linspace((3 * np.pi) / 4, (23 * np.pi) / 4, frames_count)
phi_2 = np.linspace((5 * np.pi) / 4, (25 * np.pi) / 4, frames_count)
phi_3 = np.linspace((7 * np.pi) / 4, (27 * np.pi) / 4, frames_count)
phi_4 = np.linspace((1 * np.pi) / 4, (21 * np.pi) / 4, frames_count)
phis = [phi_0, phi_1, phi_2, phi_3, phi_4]

x = np.zeros(5)
y = np.zeros(5)

ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5) 

def update(frame):
    for i in range(5):
        x[i] = R * np.cos(phis[i][frame])
        y[i] = R * np.sin(phis[i][frame])
    square.set_data(x, y)
    return square

ani = FuncAnimation(fig, 
                    update, 
                    frames=frames, 
                    interval= 40) 

ani.save('rotate_square.gif', writer="pillow", dpi = 120)





