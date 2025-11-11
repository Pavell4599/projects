from task_3_constants import g


def tme(m: int, v: int, h: int):
    E = m * v**2 / 2 + m * g * h
    return E

print(tme(6, 100, 200), 'Дж')