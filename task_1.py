import numpy as np
import random as rd

n = 9
ar1 = np.array([rd.randint(0, 100) for i in range(n)])
ar2 = np.array([rd.randint(0, 100) for i in range(n)])
ar3 = np.array([rd.randint(0, 100) for i in range(n)])


maxx = max(np.concatenate((ar1, ar2, ar3)))
maxx_alternative = max((max(ar1), max(ar2), max(ar3)))
summ = sum(ar1) + sum(ar2) + sum(ar3)


print(maxx, summ)




rand_uniform_array = np.random.randint(5, 10, 7)
print(f"Array of random ints (5-10): {rand_uniform_array}")