def decorator(func):
    print('Hi girl')
    return func


@decorator 
def decorate_example():
    print('Привет, Вселенная!')
    
decorate_example()

#2 способ
decorate_example = decorator(decorate_example)
decorate_example()