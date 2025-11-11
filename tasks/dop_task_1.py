def square(a, n):
    ans = 1
    for _ in range(n):
        ans = ans * a 
    return ans


print(square(2, 0))
print(square(4, 4))
