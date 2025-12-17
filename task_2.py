import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)


    x = np.arange(-2 * radius, 2 * radius, 0.1)
    y = np.arange(-2 * radius, 2 * radius, 0.1)
    
    X, Y = np.meshgrid(x, y)
   
    fxy = X**2 + Y**2 #- radius**2


def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, 
                    update, 
                    frames = np.arange(0,2 * np.pi, 0.1),
                    interval = 40) # ИНТЕРВАЛ В МИЛЛЕСЕКУНДАХ 40 мс = 0.04 с = 25 кадров / с 

ani.save('circle_zoom.gif')