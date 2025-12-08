import matplotlib.pyplot as plt
import numpy as np



def log_spiral(b = 0.5):
    
    fi = np.arange(0, 8 * np.pi, 0.01)
    r = np.exp(b * fi)
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    
    plt.plot(x, y)
    #plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_4_log_spiral.png')
    plt.close()
    
    
def arc_spiral(k = 0.9):
    
    fi = np.arange(0.01, 8 * np.pi, 0.01)
    r = fi * k
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    
    plt.plot(x, y)
    #plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_4_arc_spiral.png')
    plt.close() #ДЛЯ НЕСКОЛЬКИХ ФУНКЦИЙ В 1 ФАЙЛЕ
    

def gezl_spiral(k = 0.02):
    
    fi = np.arange(0.01, 9 * np.pi, 0.01)
    r = k / np.sqrt(fi)
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    
    plt.plot(x, y)
    #plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_4_gezl_spiral.png')
    plt.close() #ДЛЯ НЕСКОЛЬКИХ ФУНКЦИЙ В 1 ФАЙЛЕ
    
    
def rose(k = 6.32):
    
    fi = np.arange(0.01, 8 * np.pi, 0.01)
    r = np.sin(fi * k)
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    
    plt.plot(x, y)
    #plt.title('Base')
    # plt.grid()
    plt.axis('equal')
    plt.savefig('task_4_rose.png')
    plt.close() #ДЛЯ НЕСКОЛЬКИХ ФУНКЦИЙ В 1 ФАЙЛЕ
    
    

if __name__ == '__main__':
    log_spiral()
    arc_spiral()
    gezl_spiral()
    rose()
