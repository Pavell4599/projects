import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def cicloida():
    fig, ax = plt.subplots()
    
    
    anim_object, = plt.plot([], [], '-', lw=1)
    plt.axis('equal')
    x, y = [], []

    t = np.linspace(0, 2*np.pi, 120)
    R = 1
    
    ax.set_xlim(-2, 9) 
    ax.set_ylim(-2, 9) 
    
    
    def update(t, r = R):
        xapp = r * t - r * np.sin(t)
        yapp = r - r * np.cos(t)
        x.append(xapp)
        y.append(yapp)
        
        
        
        anim_object.set_data(x, y)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval=50) 
    
    ani.save('cicloida.gif', writer="pillow")
    plt.close()

cicloida()