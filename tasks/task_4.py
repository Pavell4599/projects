import numpy as np 


N = 6
M = 5
trigonometry_array = np.ndarray((N, M))

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.round(np.sin(N * i + M * j + 1), 3)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

print(trigonometry_array)
