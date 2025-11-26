import time


M = int(input())
N = int(input())
timer = time.time()
for i in range(M):
    time.sleep(0.5)
    print(i)
    for j in range(N):
        time.sleep(0.25)
        print(f'\t {j}')




print(timer - time.time())

