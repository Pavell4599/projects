num=int(input())
sum=0
ans=[]
for g in range(1,num+1):
    sum=0
    for i in range(1,g):
       
        if g%i==0:
            sum+=i
        if g==sum:
            ans.append(g)
            
print(ans)
