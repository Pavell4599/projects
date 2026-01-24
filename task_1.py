import numpy as np
import matplotlib.pyplot as plt


def cycloid():
    r = 
    R = 1
   
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
   
    plt.plot(x, y, ls = '--', lw = 3)

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
    
    alpha = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
   
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
   
    plt.plot(x, y, ls = '--', lw = 3)
    
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
