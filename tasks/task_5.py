import numpy as np 


N = 5
M = 6
trigonometry_array = np.ndarray((N, M))

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.round(np.sin(N * i + M * j + 1), 3)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

print(trigonometry_array)

first_column = 3
second_column = 4
for i in range(N):
    trigonometry_array[i, first_column], trigonometry_array[i, second_column] = trigonometry_array[i, second_column], trigonometry_array[i, first_column]

print(trigonometry_array)
