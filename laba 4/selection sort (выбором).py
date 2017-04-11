import numpy as np
n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype = np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив: ", A)
N = len(A)
for i in range(N-1):
    min = i
    for j in range(i+1, N):
        if A[j] < A[min]:
            min = j
    tmp = A[i]
    A[i] = A[min]
    A[min] = tmp
print(A)