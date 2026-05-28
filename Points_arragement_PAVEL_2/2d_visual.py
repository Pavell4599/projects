import numpy as np
import matplotlib.pyplot as plt

# Параметры отображения
box_limit = 12
R = 10
N = 70  # Количество зон (уменьшено для наглядности, как на рисунке)

# 1. Расчет широт для поясов (Разбиение Леопарди)
Areg = 4 * np.pi / N
Ocap = 2 * np.arcsin(np.sqrt(1 / N))

# Находим идеальное количество поясов и шаг по широте
Ncol_ideal = np.round((np.pi - 2 * Ocap) / np.sqrt(Areg))
Ocol = (np.pi - 2 * Ocap) / Ncol_ideal
O = np.arange(Ocap, np.pi, Ocol)

# Добавляем полюса в список границ широт
theta_boundaries = np.concatenate(([0], O, [np.pi]))

# Инициализируем график
fig, ax = plt.subplots(figsize=(6, 6))

# Рисуем главный контур сферы (окружность)
phi_circle = np.linspace(0, 2 * np.pi, 300)
ax.plot(R * np.cos(phi_circle), R * np.sin(phi_circle), 'k-', linewidth=1.2)

# Отрезок для центральной оси (пунктир)

# Храним сдвиг долготы для имитации смещения зон (опционально)
phi_shift = 0.0

# 2. Отрисовка границ каждого пояса
for i in range(1, len(theta_boundaries) - 1):
    theta_top = theta_boundaries[i - 1]
    theta_bottom = theta_boundaries[i]
    
    # Расчет количества делений по долготе в текущем поясе
    Ncol = np.round(4 * np.pi * (np.sin(theta_bottom / 2)**2 - np.sin(theta_top / 2)**2) / Areg)
    if Ncol == 0:
        continue
        
    # Горизонтальная линия (граница пояса)
    z_line = R * np.cos(theta_bottom)
    # Ширина горизонтальной линии на проекции
    x_max = R * np.sin(theta_bottom)
    ax.hlines(z_line, -x_max, x_max, colors='k', linewidth=1)
    
    # Сетки долгот внутри текущего пояса
    # Добавим небольшой случайный или фиксированный сдвиг между слоями для реалистичности
    phi_edges = np.linspace(0, 2 * np.pi, int(Ncol) + 1) + phi_shift
    phi_shift += 0.2  # Имитация смещения сетки (как на рисунке)
    
    # Рисуем меридианы (вертикальные дуги) внутри этого пояса
    theta_range = np.linspace(theta_top, theta_bottom, 50)
    for phi in phi_edges:
        # Проверяем, находится ли меридиан на видимой стороне (Y >= 0)
        # В ортографической проекции мы видим только переднюю полусферу
        if np.sin(phi) >= -1e-5: 
            x_arc = R * np.sin(theta_range) * np.cos(phi)
            z_arc = R * np.cos(theta_range)
            ax.plot(x_arc, z_arc, 'k-', linewidth=1)

# 3. Оформление графика в стиле рисунка (d)
ax.set_xlim(-box_limit, box_limit)
ax.set_ylim(-box_limit, box_limit)
ax.set_aspect('equal')
ax.axis('off')  # Скрываем оси координат для чистоты рисунка

# Добавим подпись угла \phi_0 для центральной зоны (пример наглядности)
# Находим центральный пояс
mid_idx = len(theta_boundaries) // 2
theta_mid_top = theta_boundaries[mid_idx - 1]
theta_mid_bottom = theta_boundaries[mid_idx]
z_text = R * np.cos((theta_mid_top + theta_mid_bottom) / 2)


plt.tight_layout()
plt.savefig('images/Star_PAVEL_2_projection_slice.png', dpi=400)

