def fst_num(num1):
    def decorator(func):
        def wrapper_func(num2):
            print(f'сумма num1 и num2 равна {num1 + func(num2)}')
           
        return wrapper_func
    return decorator



@fst_num(9)
def summer(num2):
    return num2

summer(9)
    