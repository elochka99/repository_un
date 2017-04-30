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
                if A[j] < A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    flag = True
            i += 1
        return A


    b = 13
    arr = np.zeros(b, dtype=int)
    for j in range(b):
        arr[j] = random.randint(-20, 20)
    #print("Ваш массив: ", arr)

    m = bubble_sort(arr)
    print("Отсортированный массив: ", m)
    n = 8
    for i in m:
        if i > 0:
            n += 1
        else:
            break
    print("Отрицательна температура зафиксирована в ", n, "часов")
    '''h = []
    for i in m:
        if i < 0:
            h.append(i)
    u = max(h)
    k = 0
    for i in m:
        if i != u:
            k += 1
        else:
            break

    print(h)'''

    #print("Отрицательна температура зафиксирована в ", k+8, "часов")
    break
