import numpy as np
import random
while True:
    b = 12
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 10)
        if arr[j] < 0:
            arr[j] = 0
    print(arr)
    break