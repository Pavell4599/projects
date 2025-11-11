def fib(n):
    x1 = 0 
    x2 = 1 
    for _ in range(n - 1):
        x3 = x1 + x2
        x1, x2 = x2, x3
    return x1


print(fib(16))
print(fib(5))

        