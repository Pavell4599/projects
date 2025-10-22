a=int(input())
b=int(input())

if b==0:
    print('idi v banu')
elif a % b == 0:
    print('yes')
    print(a % b)
else:
    print('no')
    print(a / b)