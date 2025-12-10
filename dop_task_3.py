import numpy as np
import matplotlib.pyplot as plt


def abx(a: int, b: int, steps: int):


    
    y = np.linspace(-5, 15, steps)
    for i in range(len(y)):
        if y[i] < a:
            y[i] = a**2

        elif y[i] > b:
            y[i] = b**2

        else:
            y[i] = y[i]**2

    x = np.linspace(-5, 10, steps)



    plt.plot(x, y, marker = '', color = 'y')
    plt.title('abx')
    plt.axis('equal')
    plt.grid()
    plt.savefig('dop_task_3.png')

    print(x)
    print(y)

abx(1, 4, 120)