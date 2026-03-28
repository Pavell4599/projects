import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



box_limit = 12
point_size = 24
filename = 'Star_PAVEL_2'
N = 500
R = 10


#points
x = np.array([])
y = np.array([])
z = np.array([])

Areg = 4 * np.pi / N
Acap = Areg
Ocap = 2 * np.arcsin(np.sqrt(1 / N))
Ncol = np.round((np.pi - 2 * Ocap) / np.sqrt(Areg))
Ocol = (np.pi - 2 * Ocap) / Ncol

f = [0]
O = np.arange(Ocap, np.pi, Ocol)
print(np.degrees(O))
for i in range(1, len(O)):
    Ncol = np.round(4 * np.pi * (np.sin(O[i] / 2)**2 - np.sin(O[i - 1] / 2)**2) / Areg)
    O_i = O[i - 1] + (O[i] - O[i - 1]) / 2
    f_i_1 = f 
    f = np.linspace(0, 2 * np.pi, int(Ncol)) + np.random.choice(f_i_1)
    #print(np.degrees(O_i))
    x = np.concatenate((x, R * np.cos(f) * np.sin(O_i)))
    y = np.concatenate((y, R * np.sin(f) * np.sin(O_i)))
    z = np.concatenate((z, np.full(int(Ncol), R * np.cos(O_i))))

x = np.concatenate((x, np.array([0, 0])))
y = np.concatenate((y, np.array([0, 0])))
z = np.concatenate((z, np.array([-R, R])))
h = np.sqrt(Areg / np.pi)   
print(h)
h = np.sqrt((R**2 * 4 * np.pi) / (len(x) * np.pi))
print(h)
# print(np.degrees(Ocap))
# print(np.degrees(Ocol))
# print(Ncol)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(x, y, z, s=point_size, edgecolors='none', color = 'blue', alpha=1, marker='.')


def draw_poles():
    phi = np.linspace(0, 2 * np.pi, 15)
    alpha = np.linspace(0, np.pi, 10)
    phi, alpha = np.meshgrid(phi, alpha)
    poles_x = []
    poles_y = []
    poles_z = []
    for i in range(len(x)):
        poles_x = h * np.sin(alpha) * np.cos(phi) + x[i]
        poles_y = h * np.sin(alpha) * np.sin(phi) + y[i]
        poles_z = h * np.cos(alpha) + z[i]
        sc = ax.plot_surface(poles_x, poles_y, poles_z, 
                    color='blue', 
                    alpha=0.5,    
                    linewidth=0,        
                    edgecolor='none') 

draw_poles()

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-box_limit, box_limit)
plt.ylim(-box_limit, box_limit)
plt.axis('equal')
plt.savefig('images/' + filename + '.png', dpi = 800)
# plt.show()