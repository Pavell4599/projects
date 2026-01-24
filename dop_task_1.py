import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots()

cycloida, = plt.plot([], [], '-', lw=1)
circle, = plt.plot([], [], '-', lw=1, color = 'green')
rad, = plt.plot([], [], '-', lw=2, color = 'red')
plt.axis('equal')
x, y = [], []


frames_count = 200
R = 1.5
circle_count = 8

frames = np.arange(frames_count)
angle = np.linspace(0, circle_count * np.pi, frames_count)

last_angle = circle_count * np.pi
x_offset = np.linspace(0, (R * last_angle - R * np.sin(last_angle)), frames_count)

ax.set_xlim(-10, 35) 
ax.set_ylim(-3, 16) 


def cycloida_fr(frame):
    r = R
    t = angle[frame]
    xapp = r * t - r * np.sin(t)
    yapp = r - r * np.cos(t)
    x.append(xapp)
    y.append(yapp)
    
    x_rad = [x_offset[frame], xapp]
    y_rad = [r, yapp]
    
    rad.set_data(x_rad, y_rad)
    cycloida.set_data(x, y)
    return cycloida, rad


def circle_fr(frame):
    r = R
    alpha = np.arange(-0.1, 2 * np.pi, 0.1)
    x = r * np.cos(alpha) + x_offset[frame]
    y = r * np.sin(alpha) + r

    circle.set_data(x, y)
    return circle
    

def update(t):
    return cycloida_fr(t), circle_fr(t)


ani = FuncAnimation(fig, 
                    update, 
                    frames=frames, 
                    interval= 20) 

ani.save('cycloida.gif', writer="pillow")
plt.close()

