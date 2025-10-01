num=int(input())
summ=0
ans=[]
for g in range(1,num+1):
    for i in range(1,g):
       if g%i==0:
            summ+=i
    if g==summ:
        ans.append(g)
    summ=0
print(ans)
