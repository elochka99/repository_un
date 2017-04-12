import numpy as np
def A(d):
    n = len(d)
    while True:
        n = n//2
        for i in range (n, len(d), n):
            k = i
            while k>0 and d[k] < d[k-n]:
                d[k], d[k-n] = d[k-n], d[k]
                k = k - n
        if n ==  1:
            break
    return d
b = int(input("введите количество элeментов в массиве: "))
d = np.zeros(b , dtype = int)
for j in range(b):
    d[j] = int(input("Вводите элементы массива:"))
print("Ваш массив: ", d)
print("Отсортированный массив", A(d))
