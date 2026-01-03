def logger(func):
    def wrapper_func(list_of_num):
        result = func(list_of_num)
        f = open('demofile.txt', 'w')
        f.write(str(result))
        f.close()
        return result
    return wrapper_func

@logger 
def summator(list_of_num):
    return(sum(list_of_num))

print(summator([1, 2, 3, 4]))