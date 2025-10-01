a=int(input())
b=a
lenn=0
ans=0
numb=0
while b>0:
    b//=10
    lenn+=1
counter=lenn-1
for i in range(lenn):
    numb=(a//(10*counter))%10
    ans+=numb
    counter-=1
    
print(ans)