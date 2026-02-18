import numpy as np
import matplotlib.pyplot as plt


def cycloid():
    
    t = np.arange(0, np.pi * 3, 0.1)
    R = 1
   
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
   
    plt.plot(x, y, ls = '-', lw = 3)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('cycloid')
    plt.grid()
    plt.axis('equal')
    plt.savefig('cycloid.png')
    plt.close()

def astroid():
    
    t = np.arange(0, np.pi * 2, 0.1)
    R = 1
   
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
   
    plt.plot(x, y, ls = '-', lw = 3)
    
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('astroid')
    plt.axis('equal')
    plt.savefig('astroid.png')
    plt.close()


if __name__ == '__main__':
    cycloid()
    astroid()
