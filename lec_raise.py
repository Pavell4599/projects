def element_1(obj, i):
    if len(obj) == 3:
        raise ValueError
    return obj[i]

x = [0, 1, 2]
element_1(x, 1)