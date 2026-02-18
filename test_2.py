import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def cicloida():
    fig, ax = plt.subplots()
    
    
    anim_object, = plt.plot([], [], '-', lw=1)
    plt.axis('equal')
    x, y = [], []
    
    t = np.linspace(0, 8*np.pi, 200)
    R = 0.3
    
    ax.set_xlim(-1, 9) 
    ax.set_ylim(-1, 5) 
    
    
    def update(t):
        r = R
        xapp = r * t - r * np.sin(t)
        yapp = r - r * np.cos(t)
        x.append(xapp)
        y.append(yapp)
        
        
        
        anim_object.set_data(x, y)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval= 20) 
    
    ani.save('cycloida.gif', writer="pillow")
    plt.close()

cicloida()