import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from parametrs import *



box_limit = 12
point_size = 6
filename = 'sphere_3d_visual'


#points
x = []
y = []
z = []
x_0 = fig_center['x'] - fig_r
y_0 = fig_center['y'] - fig_r
z_0 = fig_center['z'] - fig_r
x_1 = np.ceil(fig_r / h)
y_1 = np.ceil(fig_r / h)
z_1 = np.ceil(fig_r / h)
x_step = h * 2
y_step = h * 2 * np.sqrt(3)
z_step = h * 4 * np.sqrt(2 / 3)

for z_now in np.arange(z_0, z_1, z_step):
    for y_now in np.arange(y_0, y_1, y_step):
        for x_now in np.arange(x_0, x_1, x_step):
            x.append(x_now)
            y.append(y_now)
            z.append(z_now)

x_0 += x_step / 2
x_1 += x_step / 2
y_0 += y_step / 2
y_1 += y_step / 2

for z_now in np.arange(z_0, z_1, z_step):
    for y_now in np.arange(y_0, y_1, y_step):
        for x_now in np.arange(x_0, x_1, x_step):
            x.append(x_now)
            y.append(y_now)
            z.append(z_now)

x_0 = (fig_center['x'] - fig_r + h)
x_1 = (np.ceil(fig_r / h) + h)
y_0 = (fig_center['y'] - fig_r + (h / np.sqrt(3)))
y_1 = (np.ceil(fig_r / h) + (h / np.sqrt(3)))
z_0 = (fig_center['z'] - fig_r + z_step / 2)
z_1 = (np.ceil(fig_r / h) + z_step / 2)

for z_now in np.arange(z_0, z_1, z_step):
    for y_now in np.arange(y_0, y_1, y_step):
        for x_now in np.arange(x_0, x_1, x_step):
            x.append(x_now)
            y.append(y_now)
            z.append(z_now)

x_0 += x_step / 2
x_1 += x_step / 2
y_0 += y_step / 2
y_1 += y_step / 2

for z_now in np.arange(z_0, z_1, z_step):
    for y_now in np.arange(y_0, y_1, y_step):
        for x_now in np.arange(x_0, x_1, x_step):
            x.append(x_now)
            y.append(y_now)
            z.append(z_now)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(x, y, z, s=point_size, edgecolors='none', color = 'black', alpha=1, marker='.')
#sc = plt.scatter(x, z, s=point_size, edgecolors='none', color = 'black', alpha=1, marker='.')

# radius
phi = np.linspace(0, 2 * np.pi, 30)
alpha = np.linspace(0, np.pi, 30)
phi, alpha = np.meshgrid(phi, alpha)
x_rad = []
y_rad = []
z_rad = []
for i in range(len(x)):
    x_rad = h * np.sin(alpha) * np.cos(phi) + x[i]
    y_rad = h * np.sin(alpha) * np.sin(phi) + y[i]
    z_rad = h * np.cos(alpha) + z[i]
    sc = ax.plot_surface(x_rad, y_rad, z_rad, 
                color='green', 
                alpha=0.5,    
                linewidth=0,        
                edgecolor='none') 


plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-box_limit, box_limit)
plt.ylim(-box_limit, box_limit)
plt.axis('equal')
plt.savefig('images/' + filename + '.png', dpi = 800)
#plt.show()