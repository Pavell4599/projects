class Myerr(Exception):
    pass

def stuff(title):
    raise Myerr
    
file = open('data.txt', 'w')

try:
    stuff(file)
finally:
    file.close()
    print('Файл закрыт')