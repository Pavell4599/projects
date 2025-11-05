def my_func(a, b):
    x = 3 * a - b
    return x

#tmp = my_func()

def my_func(a:int=1, b=0):
    x = 3 * a - b
    return x

print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b = 3))
print(my_func(b = 3, a = 9))

def my_func(a, b = 0):
    x = 3 * a - b
    return x

# Так нельзя
# def my_func(a = 0, b):
#     x = 3 * a - b

def my_func(*args):
    x = (3 * args[0] - args[1]) * len(args)
    return x

print(my_func(2, 4, 5, 6, 7, 8, 3, 8))


def my_func_middle(*args):
    s = 0
    for arg in args:
        s += arg
    return s / len(args)

print(my_func_middle(2, 6, 4, 55, 7))


def my_func(**kwrgs):
    print(kwrgs)
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1 = 2, obj_2 = 1, obj_3 = 4, g = 0))


def my_func(a, b, c = 4, d = 5, *args, **kwrgs):
    print(args)
    print(kwrgs)
    
    
my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, gg = 2, ggga = 'hello')
