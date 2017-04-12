import numpy as np
def cocktail(a):
    for i in range(len(a)//2):
        for j in range(1+i, len(a)-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        return a
n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype = np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив: ", A)
print(cocktail(A))

