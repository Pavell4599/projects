import numpy as np


N = 6
M = 7
numbers = np.array([[46, 42, 68, 31, 46, 2, 26],
                    [68, 20, 65, 37, 7, 25, 4],
                    [69, 54, 7, 71, 68, 98, 73],
                    [80, 65, 8, 75, 64, 72, 62],
                    [27, 21, 16, 69, 54, 63, 31],
                    [88, 61, 59, 90, 13, 45, 84]])
maximum = np.ones(M)

for i in range(M):
    maximum[i] = max(numbers[::, i])

print(numbers)
print(' ', str(list(map(int, maximum))).replace(',', ''), sep = '')

    