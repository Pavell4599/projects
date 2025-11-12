import numpy as np


def area(figure: str='', a: int=0, b: int=0, c: int=0):
    if figure == 'circle':
        ans = round(a**2 * np.pi, 3)
    elif figure == 'rectangle':
        ans = a * b
    elif figure == 'triangle':
        p = (a + b + c) / 2
        ans = round(np.sqrt(p * (p - a) * (p - b) * (p - c)), 3)
    else:
        ans = 'I don\'t know what is this figure'
    return ans


print(area(1, 2, 4))
print(area('rectangle',3, 2, 4))
print(area('triangle', 3, 2, 4))
print(area('circle', 3))


def area_2(figure: str='', *arg):
    
    '''
    figure: \n
    \t circle: R \n
    \t rectangle: A, B \n
    \t triangle: L, H \n
    '''
    
    if figure == 'circle':
        area_culc = np.pi * arg[0]**2 
    elif figure == 'rectangle':
        area_culc = arg[0] * arg[1]
    elif figure == 'triangle':
        area_culc = arg[0] * arg[1] * 0.5
    return area_culc

print(area_2('circle', 7))
help(area_2)
area_2()
