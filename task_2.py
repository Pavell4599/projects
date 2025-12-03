import matplotlib.pyplot as plt
import numpy as np



def hyperbola(x0, x1, step, a = 1, b = 1):
    
    x = np.arange(x0, x1, step)
    y = a / x + b

    plt.plot(x, y, color = 'b', 
             label = 'Graf 1', 
             marker = '>', ms = 3)
    
    
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_2.png')


if __name__ == '__main__':
    hyperbola(0.1, 5, 0.01)
