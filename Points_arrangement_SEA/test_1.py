import matplotlib.pyplot as plt
import numpy as np



box_limit = 4

alpha = np.arange(0, 8 * np.pi, 0.1)
R = 1
x = R * np.cos(alpha)
y = alpha ** 0.5
z = R * np.sin(alpha)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

sc = ax.scatter(x, y, z, c=y, cmap='winter_r', alpha=1.0, s=2)
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-box_limit, box_limit)
ax.set_ylim(-box_limit, box_limit)
ax.set_zlim(-box_limit, box_limit)
ax.axis('equal')
#fig.colorbar(sc, ax=ax) # добавление шкалы цветов

plt.savefig('Points_arrangement_SEA/SEA_sphere.png', dpi = 400)
