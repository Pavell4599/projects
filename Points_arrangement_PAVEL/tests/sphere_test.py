import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



box_limit = 4

phi = np.linspace(0, 2 * np.pi, 100)
alpha = np.linspace(0, np.pi, 100)
phi, alpha = np.meshgrid(phi, alpha)

R = 1
x = R * np.sin(alpha) * np.cos(phi) 
y = R * np.sin(alpha) * np.sin(phi)
z = R * np.cos(alpha)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.plot_surface(x, y, z, alpha=0.5, lw = 0, edgecolor='none')

ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-box_limit, box_limit)
ax.set_ylim(-box_limit, box_limit)
ax.set_zlim(-box_limit, box_limit)
plt.savefig('sphere_test.png', dpi = 1000)