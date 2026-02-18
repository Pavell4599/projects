import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



def circle_zoom():
    fig, ax = plt.subplots()
    
    anim_object, = plt.plot([], [], '-', lw = 2, color = 'pink')
    plt.axis('equal')
    
    x, y = [], []
    
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    rad_start = 0.2 
    rad_stop = 1 # рекомендуем брать не больше, чем размеры поля
    
    r = np.linspace(rad_start, rad_stop, 200)
    
    def update(r):
        alpha = np.arange(-0.1, 2 * np.pi, 0.1)
       
        x = r * np.cos(alpha)
        y = r * np.sin(alpha)
    
        anim_object.set_data(x, y)
        return anim_object
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames = r,
                        interval = 40) # ИНТЕРВАЛ В МИЛЛЕСЕКУНДАХ 40 мс = 0.04 с = 25 кадров / с 
    
    ani.save('circle_zoom.gif')
    plt.close()
    
circle_zoom()
