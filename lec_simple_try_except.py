def element_i(obj, i):
    return obj[i]

x = [0, 1, 2, 3]
print(element_i(x, 3))

# print(element_i(x, 4))

def catcher():
    try:
        element_i(x, 4)
    except IndexError:
        print('Я получил исключение')
    except ValueError:
        print('Ошибка значения')
    print('Сделано, продолжаем')

catcher()