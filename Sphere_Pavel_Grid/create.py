import shapely.geometry as geom
import numpy as np
import random
import h5py
import yaml
import sys


float_type = np.float64
int_type = np.int32

AU = 1.49e11 # Астрономическая единица, м
G = 6.67e-11 # Гравитационная постоянная, м^3/(кг*с^2)
M_SUN = 1.998e+30 # Масса Солнца, кг
GAMMA = 5.0 / 3.0 # Постоянная адиобатты
m_H = 2 * 1.6735575e-27 # Масса молекулы водорода, кг
n_H = 2e+12  # Характерная концентрация газа, частиц/м^3
MU_H = 0.002  # Молярная масса водорода, кг/моль
R = 8.3144598  # Газовая постоянная, Дж/(моль*К)
N_a = 6.0221409e+23 # Число Авогадро 
k = 1.38064852e-23 # Больцманская постоянная
ETA = 1.2348 # Коэффициент среднего расстояния между частицами SPH
h = 1000000000 * 5  # Радиус сглаживания

num_part = 50000
box_size = 20 * AU
radius_interior = AU * 0.6
radius_exterior = AU * 1.2
thickness = AU * 0.2
temperature = 100

def coords_generator(r, N):
    phi = np.linspace(0, 2 * np.pi, N)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return np.array(list(zip(x, y)))


def _vel_calc(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    if r == 0:
        return 0.0, 0.0, 0.0  # Защита от деления на ноль в центре

    v_mag = np.sqrt(G * M_SUN / r)  # Кеплеровская скорость

    # Нормализованный радиус-вектор
    x_n = x / r
    y_n = y / r
    z_n = z / r

    # Выбор вспомогательной оси для векторного произведения
    if abs(z_n) < 0.9:
        # Векторное произведение с осью Z: v_dir = r_norm × (0, 0, 1)
        v_x = y_n
        v_y = -x_n
        v_z = 0.0
    else:
        # Вблизи полюсов используем ось X: v_dir = r_norm × (1, 0, 0)
        v_x = 0.0
        v_y = z_n
        v_z = -y_n

    # Нормализация направления скорости
    v_dir_norm = np.sqrt(v_x**2 + v_y**2 + v_z**2)
    if v_dir_norm > 0:
        v_x = v_mag * v_x / v_dir_norm
        v_y = v_mag * v_y / v_dir_norm
        v_z = v_mag * v_z / v_dir_norm

    return v_x, v_y, v_z


def create_regular_dist_model(temperature, # Температура, К
                              radius_interior, # Внутренний радиус газового диска
                              radius_exterior, # Внешний радиус газового диска
                              thickness, # Толщина газового диска
                              box_size
                              ):
########################## PAVEL ###############################################


    pos_xyz = []
    vel_xyz = []

    fig_center_x = box_size / 2
    fig_center_y = box_size / 2
    fig_center_z = box_size / 2
    fig_r = radius_exterior

    x = []
    y = []
    z = []
    x_0 = fig_center_x - fig_r
    y_0 = fig_center_y - fig_r
    z_0 = fig_center_z - fig_r
    x_1 = fig_center_x + fig_r
    y_1 = fig_center_y + fig_r
    z_1 = fig_center_z + fig_r
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

    x_0 = (fig_center_x - fig_r + h)
    x_1 = (fig_center_x + fig_r + h)
    y_0 = (fig_center_y - fig_r + (h / np.sqrt(3)))
    y_1 = (fig_center_y + fig_r + (h / np.sqrt(3)))
    z_0 = (fig_center_z - fig_r + z_step / 2)
    z_1 = (fig_center_z + fig_r + z_step / 2)

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
        x_now = x[i] - box_size / 2
        y_now = y[i] - box_size / 2
        z_now = z[i] - box_size / 2
        r_now = np.sqrt(x_now**2 + y_now**2 + z_now**2)
        if r_now <= radius_exterior and r_now >= radius_interior:
            pos_xyz.append([x_now + box_size / 2, y_now + box_size / 2, z_now + box_size / 2])

            v_x, v_y, v_z = _vel_calc(x_now, y_now, z_now)
            vel_xyz.append([v_x, v_y, v_z])
##############################################################################


########################## MATVIY ###############################################
    num_part = len(pos_xyz)
    print(num_part)
    pos = np.array(pos_xyz)
    vel = np.array(vel_xyz)

    T = np.full(num_part, temperature)
    rho = np.full(num_part, n_H * m_H)
    P = R / MU_H * rho * T
    u = 3  * k * T / m_H / 2
    V_disk = (4/3) * np.pi * (radius_exterior**3 - radius_interior**3)


    smth_lnght = np.full(num_part, h)
    masses = V_disk / num_part * rho


    return ((pos, vel, masses, u, P, T, rho, smth_lnght))

##############################################################################


def output_gas_data(pos, vel, masses, u, P, T, rho, smth_lnght):
    return {
            ("gas", "particle_position_x"): pos[:, 0],
            ("gas", "particle_position_y"): pos[:, 1],
            ("gas", "particle_position_z"): pos[:, 2],
            ("gas", "particle_velocity_x"): vel[:, 0],
            ("gas", "particle_velocity_y"): vel[:, 1],
            ("gas", "particle_velocity_z"): vel[:, 2],
            ("gas", "particle_mass"): masses,
            ("gas", "internal_energy"): u,
            ("gas", "pressure"): P,
            ("gas", "temperature"): T,
            ("gas", "smoothing_length"): smth_lnght,
            ("gas", "density"): rho
        }

gas_data = create_regular_dist_model(temperature, radius_interior, radius_exterior, thickness, box_size)

data = output_gas_data(*gas_data)

def part_filter(parts_type):
    parts_data = {}

    for key, value in data.items():
        if parts_type in key:
            parts_data[key[1]] = value
    
    return parts_data

gas_parts = part_filter('gas')
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

IC = h5py.File('./IC.hdf5', 'w')
grp = IC.create_group("/Header")
grp.attrs["BoxSize"] = [box_size, box_size, box_size]
grp.attrs["NumPart_Total"] = [len(gas_parts['particle_mass']), 1, 0, 0, 0, 0]
grp.attrs["NumPart_Total_HighWord"] = [0, 0, 0, 0, 0, 0]
grp.attrs["NumPart_ThisFile"] = [len(gas_parts['particle_mass']), 1, 0, 0, 0, 0]
grp.attrs["Time"] = 0.0
grp.attrs["NumFileOutputsPerSnapshot"] = 1
grp.attrs["MassTable"] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
grp.attrs["Flag_Entropy_ICs"] = [0, 0, 0, 0, 0, 0]
grp.attrs["Dimension"] = 3

grp = IC.create_group("/Units")
grp.attrs["Unit length in cgs (U_L)"] = 100
grp.attrs["Unit mass in cgs (U_M)"] = 1000
grp.attrs["Unit time in cgs (U_t)"] = 1.0
grp.attrs["Unit current in cgs (U_I)"] = 1.0
grp.attrs["Unit temperature in cgs (U_T)"] = 1.0

grp = IC.create_group("/PartType0")
grp.create_dataset("Coordinates", data=gas_parts_coords, dtype="f")
grp.create_dataset("Velocities", data=gas_parts_vel, dtype="f")
grp.create_dataset("Masses", data=gas_parts['particle_mass'], dtype="f")
grp.create_dataset("SmoothingLength", data=gas_parts['smoothing_length'], dtype="f")
grp.create_dataset("InternalEnergy", data=gas_parts['internal_energy'], dtype="f")
grp.create_dataset("ParticleIDs", data=np.arange(0, len(gas_parts['particle_mass'])))
grp.create_dataset("Density", data=gas_parts['density'], dtype="f")


grp = IC.create_group("/PartType1")
grp.create_dataset("Coordinates",  data=sun_coords, dtype="f")
grp.create_dataset("Velocities", data=sun_vel, dtype="f")
grp.create_dataset("Masses", data=sun_mass, dtype="f")
grp.create_dataset("ParticleIDs", data=np.arange(len(gas_parts['particle_mass']), len(gas_parts['particle_mass'])+int(1)))




