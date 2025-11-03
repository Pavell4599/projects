import numpy as np


lisst = list(map(int, input().split()))
numbers = np.array(lisst)

print(numbers)

value = int(input())
position = int(input())
copy_of_numbers = lisst

for i in range(position + 1, len(numbers)):
    numbers[i] = copy_of_numbers[i - 1]
numbers[position] = value

print(numbers)




