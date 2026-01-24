# def divine(a, b):
#     assert b != 0, # делитель не может быть 0
#     return a / b


# print(divine(9, 0))
# print(divine(9, 2))

class Myerr(Exception):
    def __str__(self):
        return 'делитель не может быть 0'
        
def divine(a, b):
    if b == 0:
        raise Myerr
    return a / b

print(divine(9, 0))


