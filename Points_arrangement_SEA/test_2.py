import matplotlib.pyplot as plt
import numpy as np

# 1. Создаем данные
alpha = np.arange(0, 8 * np.pi, 0.01)
R = 2

# Параметрическое задание пространственной кривой
x = R * np.cos(alpha)
y = alpha ** 0.5
z = R * np.sin(alpha)

# 2. Создаем фигуру и 3D оси
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 3. Строим точки
# s - размер, c - цвет (можно передать массив значений для раскраски)
sc = ax.scatter(x, y, z, c=z, cmap='viridis', s=20)

# 4. Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(sc, ax=ax) # добавление шкалы цветов

plt.savefig('Points_arrangement_SEA/curve.png', dpi = 500)
