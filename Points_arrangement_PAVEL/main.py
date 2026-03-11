import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from parametrs import *
from scipy.spatial import Delaunay, ConvexHull



box_limit = 12
point_size = 6
filename = 'main'



#points
x = []
y = []
z = []
x_0 = fig_center['x'] - fig_r - h
y_0 = fig_center['y'] - fig_r - h
z_0 = fig_center['z'] - fig_r - h
x_1 = np.ceil(fig_r / h)
y_1 = np.ceil(fig_r / h)
z_1 = np.ceil(fig_r / h)
x_step = h * 2
y_step = h * 2 * np.sqrt(3)
z_step = h * 4 * np.sqrt(2 / 3)
layer_prm = np.array(((0, 0, 0),
                      ((x_step / 2), (y_step / 2), 0),
                      (-(x_step / 2) + h, (-(y_step / 2) + (h / np.sqrt(3))), (z_step / 2)),
                      ((x_step / 2), (y_step / 2), 0)))

for layer in layer_prm:
    x_0 += layer[0]
    x_1 += layer[0]
    y_0 += layer[1]
    y_1 += layer[1]
    z_0 += layer[2]
    z_1 += layer[2]
    for z_now in np.arange(z_0, z_1, z_step):
        for y_now in np.arange(y_0, y_1, y_step):
            for x_now in np.arange(x_0, x_1, x_step):
                x.append(x_now)
                y.append(y_now)
                z.append(z_now)


#figure
phi = np.linspace(0, 2 * np.pi, fig_quality)
alpha = np.linspace(0, np.pi, fig_quality)
x_figure_border = fig_r * np.sin(alpha) * np.cos(phi) + fig_center['x']
y_figure_border = fig_r * np.sin(alpha) * np.sin(phi) + fig_center['y']
z_figure_border = fig_r * np.cos(alpha) + fig_center['z']


#point_choose
x_figure = []
y_figure = []
z_figure = []
box_coords = np.stack([x, y, z], axis=1)
border_coords = np.stack([x_figure_border, y_figure_border, z_figure_border], axis=1)
mesh = Delaunay(border_coords)

is_inside = mesh.find_simplex(box_coords) >= 0
for i in range(len(is_inside)):
    if is_inside[i]:
        x_figure.append(x[i])
        y_figure.append(y[i])
        z_figure.append(z[i])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(x_figure, y_figure, z_figure, s=point_size, edgecolors='none', color = 'black', alpha=1, marker='.')
#sc = plt.scatter(x_figure, z_figure, s=point_size, edgecolors='none', color = 'black', alpha=1, marker='.')


# radius
phi = np.linspace(0, 2 * np.pi, 30)
alpha = np.linspace(0, np.pi, 30)
phi, alpha = np.meshgrid(phi, alpha)
x_rad = []
y_rad = []
z_rad = []
for i in range(len(x_figure)):
    x_rad = h * np.sin(alpha) * np.cos(phi) + x_figure[i]
    y_rad = h * np.sin(alpha) * np.sin(phi) + y_figure[i]
    z_rad = h * np.cos(alpha) + z_figure[i]
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