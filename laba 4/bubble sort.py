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
    for j in range(N-i-1):
        if (A[j] > A[j+1]):
            tmp = A[j]
            A[j] = A[j+1]
            A[j + 1] = tmp
            flag = True
    i+=1
    print(A)

import numpy as np
b = int(input("введите кол во элиментов в массиве"))
a = np.zeros(b , dtype = int)
for i in range(b):
    a[i] = int(input("Заполните матрицу"))
print (a)
m=len(a)-1
while m>0:
    for i in range(m):
      if (a[i]>a[i+1]):
       a[i], a[i-1] = a[i-1], a[i]
    m -= 1
    print(a)