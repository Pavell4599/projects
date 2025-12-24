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
    D = 0.33
    x0 = 0.1
    y0 = 0.1
    x.append(x0)
    y.append(y0)
    
    
    ax.set_xlim(0, 1) 
    ax.set_ylim(0, 1) 
    
    
    def update(t):
        x0 = x[t]
        y0 = y[t]
        xapp = x0**2 - y0**2 + C
        yapp = 2 * x0 * y0 + D
        x.append(xapp)
        y.append(yapp)
        
        
        
        anim_object.set_data(x, y)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval=50) 
    
    ani.save('fraktal.gif', writer="pillow")
    plt.close()

froktal()