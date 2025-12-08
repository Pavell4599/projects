import matplotlib.pyplot as plt
import numpy as np



def lissau_curves(A = 1, B = 1, a = 2.25, b = 6,  q = np.pi / 2):
    t = np.linspace(0, 13, 1000)
    
    x = A * np.sin(a * t + q)
    y = B * np.sin(b * t)
    
    plt.plot(x, y)
    plt.title('Lissau curve')
   
    plt.axis('equal')
    plt.savefig('dop_task_1.png')


lissau_curves()



    