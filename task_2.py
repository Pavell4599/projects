def calculator(func):
    def wrapper_func(num1: int, num2: int, sign: str):
        num1, num2, sign = func(num1, num2, sign)
        try:
            print(f'{num1} {sign} {num2} = {eval(str(num1) + sign + str(num2))}')
        except SyntaxError:
            print('Выбран некорректный математический символ')
    return wrapper_func
  


@calculator
def args_func(num1: int, num2: int, sign: str) -> tuple:
    return num1, num2, sign

args_func(2, 5, '-')
args_func(22, 7, '/')
args_func(66, 7, ';')
    