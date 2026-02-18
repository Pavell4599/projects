import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def butterfly():
    fig, ax = plt.subplots()
    
    
    anim_object, = plt.plot([], [], '-', lw=2)
    
    x, y = [], []
    
    t = np.linspace(0, 12*np.pi, 500) 
    
    
    ax.set_xlim(-6, 6) 
    ax.set_ylim(-6, 6) 
    
    
    def update(t):
        x.append(np.sin(t) * (np.e**np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)) 
        y.append(np.cos(t) * (np.e**np.cos(t) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)) 
        
        
        anim_object.set_data(x, y)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval=50) 
    
    ani.save('butterfly.gif', writer="pillow")
    plt.close()

def heard():
    fig, ax = plt.subplots()
    
    
    anim_object, = plt.plot([], [], '-', lw=2)
    plt.axis('equal')
    x, y = [], []
    
    t = np.linspace(0, 2*np.pi, 500) 
    
    
    ax.set_xlim(-20, 20) 
    ax.set_ylim(-20, 20) 
    
    
    def update(t):
        x.append(16 * np.sin(t)**3) 
        y.append(13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(t * 3) - np.cos(t * 4)) 
        
        
        anim_object.set_data(x, y)
    
        return anim_object
    
    
    ani = FuncAnimation(fig, 
                        update, 
                        frames=t, 
                        interval=50) 
    
    ani.save('heard.gif', writer="pillow")
    plt.close()



butterfly()
heard()