import matplotlib.pyplot as plt
import numpy as np
from parametrs import *



box_limit = 16
fig, ax = plt.subplots()
point_size = 3
circle_size = 0.3
filename = 'matplotlib_sphere_2d.png'


#points
x = []
y = []
x_0 = fig_center['x'] - fig_r
y_0 = fig_center['y'] - fig_r
x_1 = np.ceil(fig_r / h)
y_1 = np.ceil(fig_r / h)
x_step = h * 2
y_step = h * 2 * np.sqrt(3)

for x_now in np.arange(x_0, x_1, x_step):
    for y_now in np.arange(y_0, y_1, y_step):
        x.append(x_now)
        y.append(y_now)

x_0 += x_step / 2
x_1 += x_step / 2
y_0 += y_step / 2
y_1 += y_step / 2

for x_now in np.arange(x_0, x_1, x_step):
    for y_now in np.arange(y_0, y_1, y_step):
        x.append(x_now)
        y.append(y_now)

z = [0]
ax.scatter(x, y, s=point_size, edgecolors='none', color = 'black', alpha=1, marker='.')


#radius
alpha = np.arange(0, 2 * np.pi, 0.1)
x_rad = []
y_rad = []
for i in range(len(x)):
    x_rad = h * np.cos(alpha) + x[i]
    y_rad = h * np.sin(alpha) + y[i]
    ax.plot(x_rad, y_rad, color = 'red', ms=circle_size, lw=circle_size)


ax.set_ylabel('X')
ax.set_ylabel('Y')
ax.set_xlim(-box_limit, box_limit)
ax.set_ylim(-box_limit, box_limit)
ax.axis('equal')
plt.savefig('images/' + filename + '.png', dpi = 800)