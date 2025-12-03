import matplotlib.pyplot as plt
import numpy as np



def circle_plotter(R = 3):
    
    alpha = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
   
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
   
    plt.plot(x, y, ls = '--', lw = 3)

    
    
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Base')
    # plt.grid()
    plt.axis('equal')
     
    plt.savefig('parametric_plot.png')


if __name__ == '__main__':
    circle_plotter()

