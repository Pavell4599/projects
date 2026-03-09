import numpy as np
from scipy.spatial import Delaunay, ConvexHull

# 1. Ваши координаты стенок (границы фигуры)
wall_x = np.array([0, 10, 10, 0, 0, 10, 10, 0])
wall_y = np.array([0, 0, 10, 10, 0, 0, 10, 10])
wall_z = np.array([0, 0, 0, 0, 10, 10, 10, 10])

wall_points = np.stack([wall_x, wall_y, wall_z], axis=1)

# 2. Создаем структуру для проверки (триангуляция Делоне)
# Это превращает набор точек стенок в "твердое тело"
hull = Delaunay(wall_points)

# 3. Ваши точки, которые нужно проверить
px = np.array([5, 15])
py = np.array([5, 15])
pz = np.array([5, 15])
test_points = np.stack([px, py, pz], axis=1)

# 4. Проверка: результат < 0 означает, что точка внутри
is_inside = hull.find_simplex(test_points) >= 0

print(f"Результат проверки: {is_inside}") 
# [True, False] -> первая точка внутри куба, вторая — нет

