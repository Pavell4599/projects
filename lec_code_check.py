try:
    x = int(input('Введите 1 число : '))
    y = int(input('Введите 2 число : '))
    
    if x < 0 and y < 0:
        raise ValueError('Числа должны быть неотрицатеьными')
        
    result = x / y
    
    print('Результат:', result)
    
    
except ValueError as e:
    print('Ошибка', e)
    
except ZeroDivisionError as e:
    print('Ошибка деления на 0')
    
except Exception as e:
    print('Непредвиденная ошибка', e)