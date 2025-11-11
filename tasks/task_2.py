import numpy as np


def multiplyer(numbers):
    return np.prod(numbers)


numbers = np.array((1, 2, 4, 7))
print(multiplyer(numbers))