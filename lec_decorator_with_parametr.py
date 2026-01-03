def logger(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            f = open(filename, 'w')
            f.write(str(result))
            return result
        return wrapper 
    return decorator

@logger('file_log.txt')
def summator(list_of_num):
    return(sum(list_of_num))

print(summator([1, 2, 3, 4]))