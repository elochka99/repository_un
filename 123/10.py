import numpy as np
import random
while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 15)
    print("Температуры: ", arr)
    n = 0
    for i in arr:
        if i < -10:
            n += 1
    print("Температура ниже -10 была ", n, "раз")
    break