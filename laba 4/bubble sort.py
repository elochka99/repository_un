import numpy as np
n = int(input('Количество элементов в массиве: '))
A = np.zeros(n, dtype = np.int_)
for j in range(n):
    A[j] = int(input('Вводите элменты массива: '))
print("ваш массив: ", A)
N = len(A)
i = 0
flag = True
while flag:
   flag = False
   for k in range(N-i-1):
       if (A[k] > A[k+1]):
           tmp = A[k]
           A[k] = A[k+1]
           A[k + 1] = tmp
           flag = True
       print(A)
