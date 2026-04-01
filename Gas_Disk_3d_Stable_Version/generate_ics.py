import shapely.geometry as geom
import numpy as np
import random
import h5py
import yaml
import sys
from scipy.spatial import cKDTree
from typing import Union

float_type = np.float64
int_type = np.int32

AU = 1.49e11  # Астрономическая единица, м
G = 6.67e-11  # Гравитационная постоянная, м^3/(кг*с^2)
M_SUN = 1.998e+30  # Масса Солнца, кг
GAMMA = 5.0 / 3.0  # Постоянная адиабаты
m_H = 2 * 1.6735575e-27  # Масса молекулы водорода, кг
n_H = 2e+12  # Характерная концентрация газа, частиц/м^3
MU_H = 0.002  # Молярная масса водорода, кг/моль
R = 8.3144598  # Газовая постоянная, Дж/(моль*К)
N_a = 6.0221409e+23  # Число Авогадро 
k = 1.38064852e-23  # Больцманская постоянная
ETA = 1.2348  # Коэффициент среднего расстояния между частицами SPH

num_part = 20000
box_size = 20 * AU
radius_interior = AU * 0.6
radius_exterior = AU * 1.2
thickness = AU * 0.05
temperature = 100


# ============================================================================
# ФУНКЦИЯ РАСЧЁТА H ЧЕРЕЗ БЛИЖАЙШИХ СОСЕДЕЙ (KD-TREE)
# ============================================================================
def calculate_smoothing_lengths(
    coordinates: np.ndarray,
    boxsize: Union[float, np.ndarray, None] = None,
    n_neighbors: int = 32,
    kernel_gamma: float = 1.4,
    speedup_fac: int = 2,
    dimension: int = 3,
    use_periodic: bool = False
) -> np.ndarray:
    """
    Рассчитать радиус сглаживания h для каждой частицы по методу ближайших соседей.
    
    Параметры
    ---------
    coordinates : np.ndarray
        Массив координат формы (N, 3).
    boxsize : float | np.ndarray | None
        Размер периодической коробки.
    n_neighbors : int
        Целевое число соседей внутри радиуса сглаживания.
    kernel_gamma : float
        Параметр ядра СПФ (1.4 для M4 в 3D).
    speedup_fac : int
        Фактор ускорения поиска.
    dimension : int
        Размерность задачи.
    use_periodic : bool
        Использовать ли периодические границы в поиске соседей.
    
    Возвращает
    ----------
    np.ndarray
        Массив радиусов сглаживания h формы (N,).
    """
    coordinates = np.asarray(coordinates, dtype=np.float64)
    if coordinates.ndim != 2 or coordinates.shape[1] != 3:
        raise ValueError("coordinates должен быть массивом формы (N, 3)")
    
    n_particles = len(coordinates)
    if n_particles == 0:
        return np.array([], dtype=np.float64)
    
    # Построение KD-дерева
    if use_periodic and boxsize is not None:
        if np.isscalar(boxsize):
            boxsize = np.full(3, float(boxsize), dtype=np.float64)
        else:
            boxsize = np.asarray(boxsize, dtype=np.float64).reshape(3)
        tree = cKDTree(coordinates, boxsize=boxsize)
    else:
        tree = cKDTree(coordinates)  # Без периодичности!
    
    k_search = max(1, n_neighbors // speedup_fac)
    correction_factor = (speedup_fac ** (1.0 / dimension)) / kernel_gamma
    
    # Обработка блоками для экономии памяти
    block_size = 65536
    h_lengths = np.empty(n_particles, dtype=np.float64)
    
    for start in range(0, n_particles, block_size):
        end = min(start + block_size, n_particles)
        distances, _ = tree.query(coordinates[start:end], k=k_search, workers=-1)
        
        if k_search == 1:
            r_n = distances
        else:
            r_n = distances[:, -1]
        
        h_lengths[start:end] = r_n * correction_factor
    
    return h_lengths


def _vel_calc(x, y, z):
    alpha = np.atan2(y, x)
    r = np.sqrt(x**2 + y**2 + z**2)
    v_x = -np.sqrt(G * M_SUN / r) * np.sin(alpha)
    v_y = np.sqrt(G * M_SUN / r) * np.cos(alpha)
    v_z = 0
    return v_x, v_y, v_z


def create_regular_dist_model(temperature,
                              radius_interior,
                              radius_exterior,
                              thickness,
                              box_size
                              ):
    ########################## PAVEL ###############################################
    pos_xyz = []
    vel_xyz = []
    V = (radius_exterior**2 * np.pi - radius_interior**2 * np.pi) * thickness
    num_part = 50000
    h = (((V / num_part) * 3) / (4 * np.pi))**(1 / 3)
    x = []
    y = []
    z = []
    x_0 = -radius_exterior
    y_0 = -radius_exterior
    z_0 = -thickness / 2
    x_1 = radius_exterior 
    y_1 = radius_exterior 
    z_1 = thickness / 2
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
    x_0 = (-radius_exterior + h)
    x_1 = (radius_exterior + h)
    y_0 = (-radius_exterior + (h / np.sqrt(3)))
    y_1 = (radius_exterior + (h / np.sqrt(3)))
    z_0 = (-thickness / 2 + z_step / 2)
    z_1 = (thickness / 2 + z_step / 2)
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

    for i in range(len(x)):
        x_now = x[i]
        y_now = y[i]
        z_now = z[i]
        if (x_now**2 + y_now**2)**0.5 <= radius_exterior and (x_now**2 + y_now**2)**0.5 >= radius_interior:
            pos_xyz.append([x_now + box_size / 2, y_now + box_size / 2, z_now + box_size / 2])
            v_x, v_y, v_z = _vel_calc(x_now, y_now, z_now)
            vel_xyz.append([v_x, v_y, v_z])
    ##############################################################################

    ########################## MATVIY ###############################################
    num_part = len(pos_xyz)
    pos = np.array(pos_xyz)
    vel = np.array(vel_xyz)

    T = np.full(num_part, temperature)
    rho = np.full(num_part, n_H * m_H)
    P = R / MU_H * rho * T
    u = 3 * k * T / m_H / 2

    # === РАСЧЁТ ДЛИНЫ СГЛАЖИВАНИЯ ЧЕРЕЗ KD-TREE ===
    N_ngb = 32
    kernel_gamma = 1.4
    speedup_fac = 2
    
    smth_lnght = calculate_smoothing_lengths(
        coordinates=pos,
        boxsize=box_size,
        n_neighbors=N_ngb,
        kernel_gamma=kernel_gamma,
        speedup_fac=speedup_fac,
        dimension=3,
        use_periodic=False  # ← ОТКЛЮЧАЕМ для тонкого диска!
    )
    
    # === ОТЛАДКА: статистика h ===
    print(f"\n[DEBUG] Smoothing lengths:")
    print(f"  min: {np.min(smth_lnght):.3e} м")
    print(f"  max: {np.max(smth_lnght):.3e} м")
    print(f"  mean: {np.mean(smth_lnght):.3e} м")
    print(f"  median: {np.median(smth_lnght):.3e} м")
    print(f"  std: {np.std(smth_lnght):.3e} м")
    print(f"  h/box_mean: {np.mean(smth_lnght) / box_size:.2e}")
    print(f"  h/thickness: {np.mean(smth_lnght) / thickness:.2f}")
    print(f"  any NaN: {np.any(np.isnan(smth_lnght))}")
    print(f"  any inf: {np.any(np.isinf(smth_lnght))}")
    print(f"  any <= 0: {np.any(smth_lnght <= 0)}\n")
    
    # === ПРОВЕРКИ ===
    assert np.all(np.isfinite(smth_lnght)), "NaN/inf в h!"
    assert np.all(smth_lnght > 0), "Отрицательные h!"
    assert np.all(smth_lnght < box_size * 0.1), "h слишком велик!"
    assert np.all(smth_lnght < thickness * 3), "h > 3*толщины диска — проверь!"

    masses = V / num_part * rho

    pos_star = np.array([[box_size / 2, box_size / 2, box_size / 2]])
    vel_star = np.array([[0, 0, 0]])
    mass_star = np.array([M_SUN])
    return ((pos, vel, masses, u, P, T, rho, smth_lnght),
            (pos, vel, masses, pos_star, vel_star, mass_star))
    ##############################################################################


def output_gas_data(pos, vel, masses, u, P, T, rho, smth_lnght):
    return {
            ("PartType0", "particle_position_x"): pos[:, 0],
            ("PartType0", "particle_position_y"): pos[:, 1],
            ("PartType0", "particle_position_z"): pos[:, 2],
            ("PartType0", "particle_velocity_x"): vel[:, 0],
            ("PartType0", "particle_velocity_y"): vel[:, 1],
            ("PartType0", "particle_velocity_z"): vel[:, 2],
            ("PartType0", "particle_mass"): masses,
            ("PartType0", "internal_energy"): u,
            ("PartType0", "pressure"): P,
            ("PartType0", "temperature"): T,
            ("PartType0", "smoothing_length"): smth_lnght,
            ("PartType0", "density"): rho
        }


# ============================================================================
# ОСНОВНОЙ БЛОК
# ============================================================================
if __name__ == "__main__":
    gas_data, material_parts_data = create_regular_dist_model(
        temperature, radius_interior, radius_exterior, thickness, box_size)

    data = output_gas_data(*gas_data)

    def part_filter(parts_type):
        parts_data = {}
        for key, value in data.items():
            if parts_type in key:
                parts_data[key[1]] = value
        return parts_data

    gas_parts = part_filter('PartType0')
    num_gas_part = len(gas_parts['density'])
    gas_parts_coords = np.array(tuple(zip(
                        gas_parts['particle_position_x'], 
                        gas_parts['particle_position_y'], 
                        gas_parts['particle_position_z'])))
    gas_parts_vel = np.array(tuple(zip(
                    gas_parts['particle_velocity_x'], 
                    gas_parts['particle_velocity_y'], 
                    gas_parts['particle_velocity_z'])))
                        
    sun_mass = np.array([M_SUN])
    sun_coords = np.array([box_size/2, box_size/2, box_size/2])
    sun_vel = np.array([0, 0, 0])

    # === ВАЛИДАЦИЯ ДАННЫХ ПЕРЕД ЗАПИСЬЮ ===
    print("\n=== Проверка данных перед записью ===")
    print(f"Координаты: min={np.min(gas_parts_coords):.3e}, max={np.max(gas_parts_coords):.3e}")
    print(f"Скорости: min={np.min(gas_parts_vel):.3e}, max={np.max(gas_parts_vel):.3e}")
    print(f"Массы: min={np.min(gas_parts['particle_mass']):.3e}, max={np.max(gas_parts['particle_mass']):.3e}")
    print(f"Длина сглаживания (h): min={np.min(gas_parts['smoothing_length']):.3e}, "
          f"max={np.max(gas_parts['smoothing_length']):.3e}, "
          f"mean={np.mean(gas_parts['smoothing_length']):.3e}")

    assert np.all(np.isfinite(gas_parts['smoothing_length'])), "ОШИБКА: В smoothing_length есть NaN или inf!"
    assert np.all(gas_parts['smoothing_length'] > 0), "ОШИБКА: В smoothing_length есть отрицательные значения!"
    assert np.all(gas_parts['smoothing_length'] < box_size * 0.01), "ОШИБКА: h слишком велика (>1% от бокса)!"

    h_mean = np.mean(gas_parts['smoothing_length'])
    print(f"Отношение h_mean / box_size: {h_mean / box_size:.6f} (должно быть ~0.001-0.01)")
    print("===================================\n")

    # === ЗАПИСЬ В HDF5 ===
    IC = h5py.File('./IC.hdf5', 'w')

    grp = IC.create_group("/Header")
    grp.attrs["BoxSize"] = np.array([box_size, box_size, box_size], dtype=np.float64)
    grp.attrs["NumPart_Total"] = np.array([len(gas_parts['particle_mass']), 1, 0, 0, 0, 0], dtype=np.int32)
    grp.attrs["NumPart_Total_HighWord"] = np.array([0, 0, 0, 0, 0, 0], dtype=np.int32)
    grp.attrs["NumPart_ThisFile"] = np.array([len(gas_parts['particle_mass']), 1, 0, 0, 0, 0], dtype=np.int32)
    grp.attrs["Time"] = 0.0
    grp.attrs["NumFileOutputsPerSnapshot"] = 1
    grp.attrs["MassTable"] = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float64)
    grp.attrs["Flag_Entropy_ICs"] = np.array([0, 0, 0, 0, 0, 0], dtype=np.int32)
    grp.attrs["Dimension"] = 3

    grp = IC.create_group("/Units")
    grp.attrs["Unit length in cgs (U_L)"] = 100.0
    grp.attrs["Unit mass in cgs (U_M)"] = 1000.0
    grp.attrs["Unit time in cgs (U_t)"] = 1.0
    grp.attrs["Unit current in cgs (U_I)"] = 1.0
    grp.attrs["Unit temperature in cgs (U_T)"] = 1.0

    # PartType0 - Газ
    grp = IC.create_group("/PartType0")
    grp.create_dataset("Coordinates", data=gas_parts_coords.astype(np.float64))
    grp.create_dataset("Velocities", data=gas_parts_vel.astype(np.float64))
    grp.create_dataset("Masses", data=gas_parts['particle_mass'].astype(np.float64))
    grp.create_dataset("SmoothingLength", data=gas_parts['smoothing_length'].astype(np.float64))
    grp.create_dataset("InternalEnergy", data=gas_parts['internal_energy'].astype(np.float64))
    grp.create_dataset("ParticleIDs", data=np.arange(0, len(gas_parts['particle_mass']), dtype=np.int64))
    grp.create_dataset("Density", data=gas_parts['density'].astype(np.float64))

    # PartType1 - Звезда
    grp = IC.create_group("/PartType1")
    grp.create_dataset("Coordinates", data=sun_coords.astype(np.float64))
    grp.create_dataset("Velocities", data=sun_vel.astype(np.float64))
    grp.create_dataset("Masses", data=sun_mass.astype(np.float64))
    grp.create_dataset("ParticleIDs", data=np.array([len(gas_parts['particle_mass'])], dtype=np.int64))

    IC.close()

    # === ПРОВЕРКА ЗАПИСАННОГО ФАЙЛА ===
    print("\n=== Проверка записанного файла ===")
    with h5py.File('./IC.hdf5', 'r') as f:
        h_check = f['/PartType0/SmoothingLength'][:]
        print(f"Прочитано h: min={np.min(h_check):.3e}, max={np.max(h_check):.3e}")
        if np.any(~np.isfinite(h_check)):
            print("!!! ВНИМАНИЕ: В файле есть NaN или inf в SmoothingLength !!!")
    print("Файл IC.hdf5 создан успешно.\n")