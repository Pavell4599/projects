n=int(input('give me number: '))
first=0
second=0
third=1
for _ in range(n):
    print(third)
    first=second
    second=third
    third=second+first
    
    
    