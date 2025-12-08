import numpy as np
import matplotlib.pyplot as plt


def ellipse(a = 2, b = 1):
    p = b**2 / a
    fi = np.linspace(0, 2 * np.pi, 1000)
    e = -0.9
    r = p / (1 + e * np.cos(fi))
    

    x = r * np.cos(fi)
    y = r * np.sin(fi)


    plt.plot(x, y, color = 'violet')
    plt.title('Ellipse')
    plt.axis('equal')
    plt.grid()
    plt.savefig('dop_task_2.png')


ellipse()