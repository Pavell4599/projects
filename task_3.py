import time


M = int(input())
N = int(input())
timer = time.time()
for i in range(M):
    time.sleep(1)
    print(i)
    for j in range(N):
        time.sleep(1)
        print(f'\t {j}')

timer = time.time()-timer


print(timer)

