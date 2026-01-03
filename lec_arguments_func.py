def decorator(func):
    #def wrapper_function(*args, **kwargs):
    def wrapper_function(str):
        #func(*args, **kwargs)
        func(str)
    return wrapper_function 


@decorator 
def greet(name):
    print(f'Привет, {name}!')
    
greet('sweet popka')