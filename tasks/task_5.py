import numpy as np


def square(figure: str='', a: int=0, b: int=0, c: int=0):
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


print(square(1, 2, 4))
print(square('rectangle',3, 2, 4))
print(square('triangle', 3, 2, 4))
print(square('circle', 3))

