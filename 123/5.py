import numpy as np
import random
while True:
    arr = np.zeros(7, dtype = int)
    for i in range(0,7):
        arr[i] = random.randint(1,20)
    print("ваш массив: ", arr)
    print("Массив в квадрате: ", arr**2)
    break
