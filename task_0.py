import time


def timer(func):
    def wrapper_func():
        timerr = time.time()
        result = func()
        timerr = time.time() - timerr
        print(f'Время работы функции {func.__name__}: {timerr}')
        return result
    return wrapper_func


@timer 
def popa():
    a = [x for x in range(0, 1000000)]
    return 999
    

print(popa())
popa() 

