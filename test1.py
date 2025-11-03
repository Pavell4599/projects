import random
from sre_constants import RANGE


N = int(input())
M = int(input())
a = []
for i in range(N):
    a.append([])
    for j in range(M):
        a[i].append(random.randint(1, 100))

print(a)