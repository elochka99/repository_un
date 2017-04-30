import numpy as np
import random
while True:
    b = 10
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 15)
    print("Температуры: ", arr)
    k = int(sum(arr)/len(arr))
    n = 0
    for i in arr:
        if i > k:
            n += 1
    print("средняя температура = ", k)
    print("Температура выше средней была ", n, "раз")
    break