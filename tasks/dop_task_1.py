def square(osnovanie, pokazatel):
    ans = 1
    for _ in range(pokazatel):
        ans = ans * osnovanie 
    return ans


print(square(2, 0))
print(square(4, 4))
