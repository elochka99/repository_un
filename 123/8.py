import numpy as np
import random
while True:
    b = 15
    n = 0
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-15, 30)
    m = max(arr)
    for i in arr:
        if i != m:
            n += 1
        else:
            break
    print(arr)
    print(m)
    print(n)
    break
