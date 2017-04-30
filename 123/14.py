import numpy as np
import random
while True:
    def bubble_sort(A):
        N = len(A)
        i = 0
        flag = True
        while flag:
            flag = False
            for j in range(N - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    flag = True
            i += 1
        return A

    b = 15
    arr = np.zeros(b, dtype=float)
    for j in range(b):
        arr[j] = random.uniform(1, 100)
    h = bubble_sort(arr)
    print("массив: ", h)

    break