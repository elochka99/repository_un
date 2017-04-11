import numpy as np

n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype=np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив: ", A)
N = len(A)-1

while N>0:
    for k in range(N):
        if (A[k] > A[k + 1]):
            tmp = A[k]
            A[k] = A[k + 1]
            A[k + 1] = tmp
    N-=1
    print(A)
