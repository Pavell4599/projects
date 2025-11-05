import numpy as np


# строк 5
# столбцев 4
first_array = np.array([[35, 10, 48, 88], [16, 64, 20, 94], [19, 36, 92, 3], [28, 98, 28, 76], [23, 20, 37, 54]])
second_array = np.array([[80, 76, 67, 65], [20, 48, 69, 14], [41, 91, 65, 77], [69, 42, 70, 28], [73, 17, 63, 59]])
third_array = np.ndarray((len(first_array), len(second_array[0])))

for i in range(len(first_array)):
    for j in range(len(second_array[0])):
        if first_array[i, j] > second_array[i, j]:
            third_array[i, j] = first_array[i, j]
        elif first_array[i, j] <= second_array[i, j]:
            third_array[i, j] = second_array[i, j]

print(first_array)
print(second_array)
print(third_array)




