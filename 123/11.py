import numpy as np
import random
while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(5, 35)
    print("Температуры: ", arr)
    n = 0
    for i in arr:
        if i > 18:
            n += 1
    print("Дней для купания было ", n)
    break