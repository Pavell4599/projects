import numpy as np
import matplotlib.pyplot as plt

# Создание 3D-пространства
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Определение параметров кривой
alpha = np.arange(0, 8 * np.pi, 0.5)
R = 2

# Параметрическое задание пространственной кривой
x = R * np.cos(alpha)
y = alpha ** 0.5
z = R * np.sin(alpha)

# Построение пространственной кривой
ax.plot(x, y, z, label='points by SEA', marker = 'o', ms = 0.5)
edge = 5
ax.set(xlim3d=(-edge, edge), xlabel='X')
ax.set(ylim3d=(0, edge), ylabel='Y')
ax.set(zlim3d=(-edge, edge), zlabel='Z')

ax.legend()
ax.set_title('3D Test')

plt.savefig('Points_arrangement_SEA/curve.png', dpi = 500)