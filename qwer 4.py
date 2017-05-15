import random
import numpy as np
def func(a):
    q = s = (n-1)
    k = m = 0
    h = []
    r = []
    while True:
        for i in a:
            for j in a:
                if i == k and j == q:
                    h.append(a[i,j])
                    k += 1
                    q -= 1
                elif i == s and j == m:
                    r.append(a[i,j])
                    m += 1
                    s -= 1
                else:
                    continue
        for i in r:
            for j in h:
                r[i], h[j] = h[j], r[i]
        k = m = 0
        q = s = (n-1)
        for i in a:
            for j in a:
                if i == k and j == q:
                    for el in h:
                        a[i,j] = h[el]
                        k += 1
                        q -= 1
                elif i == s and j == m:
                    for elem in r:
                        a[i,j] = r[elem]
                        s -= 1
                        m += 1
        return a
while True:

    n = int(input("размерность = "))
    a = np.zeros(n, dtype=int)
    for i in range(n):
        for j in range(n):
            a[i,j] = int(input("vvodi- "))
    print("matrix: ", a)
    print("izm matr: ", func(a))
    w = input("continue - [1]? - ")
    if w == '1':
        continue
    else:
        break
