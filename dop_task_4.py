import numpy as np
import matplotlib.pyplot as plt


def staircase(N):


    x = np.arange(0, N + 1, 0.5)
    y = x // 1
    



    plt.plot(x, y, marker = '', color = 'y')
    plt.title('Staircase')
    plt.axis('equal')
    plt.grid()
    plt.savefig('dop_task_4.png')

staircase(5)


# a = 10
# np.full(10, a)
# заполняет список десетью а

# 0 0
# 0 1
# 1 1
# 1 2
# 2 2
# 2 3
# 3 3