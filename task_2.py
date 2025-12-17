import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

anim_object, = plt.plot([], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)


r = np.arange(1, 3.9, 0.1)

   


def update(radius):
    x = np.arange(-2 * radius, 2 * radius, 0.1)
    y = np.arange(-2 * radius, 2 * radius, 0.1)
    
    X, Y = np.meshgrid(x, y)
   
    fxy = X**2 + Y**2
    anim_object.set_data(fxy)
    return anim_object,

ani = FuncAnimation(fig, 
                    update, 
                    frames = r,
                    interval = 40) # ИНТЕРВАЛ В МИЛЛЕСЕКУНДАХ 40 мс = 0.04 с = 25 кадров / с 

ani.save('circle_zoom.gif')