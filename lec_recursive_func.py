def fib(i):
    if i <= 1:
        return i
    else:
        return (fib(i - 1) + fib(i - 2))
    
print(fib(99))