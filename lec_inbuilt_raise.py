def error_func(a):
    try:
        if a == 3:
            raise Exception('Myexception')
    except Exception as e:
        print('Произошла ошибка:', str(e))
        
error_func(3)




