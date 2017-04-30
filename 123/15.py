import numpy as np
import random
while True:
    b = 20

    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.uniform(100, 200)
    k = 0
    for i in arr:
        if i % 2 == 0:
            k += i
    print("массив: ", arr)

    print("Сумма элементов массива: ", k)
    break
