import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def froktal():
    fig, ax = plt.subplots()
    
    
    anim_object, = plt.plot([], [], '-', lw=1)
    plt.axis('equal')
    x, y = [], []
    
    t = np.arange(200) 
    C = 0.3
    D = 0.3
    x0 = 0.1
    y0 = 0.1
    x_offset = -0.6
    y_offset = -0.3
    x.append(x0)
    y.append(y0)
    
    
    ax.set_xlim(-1, 1) 
    ax.set_ylim(-1, 1) 
    
    
    def update(t):
        x0 = x[t]
        y0 = y[t]
        xapp = x0**2 - y0**2 + C 
        yapp = 2 * x0 * y0 + D 
        x.append(xapp)
        y.append(yapp)
        
        x_off_l = x.copy()
        y_off_l = y.copy()
        for i in range(len(x_off_l)):
            x_off_l[i] += x_offset
        for i in range(len(y_off_l)):
            y_off_l[i] += y_offset
            
        anim_object.set_data(x_off_l, y_off_l)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval=50) 
    
    ani.save('fraktal.gif', writer="pillow")
    plt.close()

froktal()