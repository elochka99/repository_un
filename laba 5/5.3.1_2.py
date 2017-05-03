from random import random
import numpy as np

def summa(a, n):
    for i in a:
        for j in i:
            n += j
    return n
def summa_rek(a):
   if len(a) == 1:
        return a[0]
   else:
        return a[0] + summa_rek(a[1:])

def proiz(a, n):
    for i in a:
        for j in i:
            n *= j
    return n
def proiz_rek(a):
   if len(a) == 1:
        return a[0]
   else:
        return a[0] * proiz_rek(a[1:])
def seach(a,k):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == k:
                return i+1, j+1
def seach_rek(a,k):
    if len(a) == 1:
        return a[0]
    else:
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] == k:
                    return i + 1, j + 1

while True:
    n = 0
    b = int(input("какая размерность матрицы? - "))
    a = np.zeros((b, b), dtype=int)
    for i in range(b):
        for j in range(b):
            a[i][j] = int(random() * 10)
    print(a)
    print("итерационно сумма = ", summa(a, n))
    suma = sum(summa_rek(a))
    print("рекурсивно сумма = ", suma)
    print("итерационно произведение = ", proiz(a, n+1))
    proi = proiz_rek(a)
    p = 1
    for i in proi:
        p *= i
    print("рекурсивно произведение = ", p)
    k = int(input("введи число для поиска - "))
    print("итерационно число на месте - ", seach(a,k))
    print("рекурсивно число на месте - ", seach_rek(a, k))