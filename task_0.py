import time


def timer(func):
    def wrapper_func():
        timer = time.time()
        print(func())
        timer = time.time() - timer
        print(f'Время работы функции: {timer}')
    return wrapper_func


@timer 
def popa():
    a = [x for x in range(0, 10000)]
    return 999
    

print(popa())    

