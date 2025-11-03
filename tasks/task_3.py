import numpy as np
from task_1_constants import g



x0 = 5
y0 = 7
v0x = 4
v0y = 3


txy = ' [   t     x     y ]'
ans = np.ndarray((6, 3))
for i in range(6):
    t = i
    x = x0 + v0x * t
    y = y0 + v0y * t - g * t ** 2 / 2
    ans[i, :3:] = np.array([t, x, y])



print(txy)
print(ans)

