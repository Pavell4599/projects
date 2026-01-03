def decorator(func):
    def new_func():
        print('Go play me')
    return new_func 

@decorator 
def decorate_example():
    print('Best')
    
decorate_example()
print(decorate_example.__class__)
print(decorate_example.__name__)