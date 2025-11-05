x0 = 10 #переменнная определенная глобально

def move(t):
    x = x0 * t
    return x

print(move(3))
#print(x)
a = 'Good'

def my_func():
    a = 'Bad'
    print(a, id(a))
    
my_func()
print(a, id(a))



#у множеств можно искать пересечение a = {1, 2, 3}