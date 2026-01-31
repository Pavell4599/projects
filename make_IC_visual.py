import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d


#переменные
asteroid_count = 60
R = 4

# Создание 3D-пространства
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Определение параметров кривой
alpha = np.linspace(0, 2 * np.pi, asteroid_count)


x = R * np.cos(alpha)
y = R * np.sin(alpha)
z = 0
ax.plot(x, y, z, '.', ms=2.5, label='Asteroids', color = '#0F2199')
ax.axis('equal')

x = 0
y = 0
z = 0
ax.plot(x, y, z, '.', ms=5, label='Sun', color='#FF3838')
ax.axis('equal')

edge = 5
ax.set(xlim3d=(-edge, edge), xlabel='X')
ax.set(ylim3d=(-edge, edge), ylabel='Y')
ax.set(zlim3d=(-edge, edge), zlabel='Z')

ax.legend()
ax.set_title('Sun ans asteroid belt')

plt.savefig('Sun_and_aster.png', dpi=1000)