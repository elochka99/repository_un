import numpy as np
def cocktail_sort(A):
    for k in range(len(A) - 1, 0, -1):

        for i in range(k, 0, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]


        for i in range(k):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

        return A
n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype = np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив:  ", A)
print(cocktail_sort(A))
