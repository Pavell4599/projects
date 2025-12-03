import matplotlib.pyplot as plt
import numpy as np



def elips(x0, x1, y0, y1, step, a = 0.74, b = 0.4):
    
    x = np.arange(x0, x1, step)
    y = np.arange(y0, y1, step)
    X, Y = np.meshgrid(x, y)
    fxy = X**2 / a**2 + Y**2 / b**2 - 1
    
    plt.contour(X, Y, fxy, levels = [0])

    
    
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_3.png')


if __name__ == '__main__':
    elips(-1, 1, -2, 2, 0.01)
