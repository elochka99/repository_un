import numpy as np

a = input('Введите элементы для сортировки: ').split(', ')
mass = np.array(a, dtype=int)

n = 1
while n < len(mass):
    for i in range(len(mass) - n):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    n += 1
    print(a)


