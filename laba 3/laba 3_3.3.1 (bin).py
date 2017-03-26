import timeit
setup = '''
import numpy as np
n = int(input('Введите количество элементов массива: '))
a = np.zeros(n)
for j in range(len(a)):
    a[j] = int(input('Вводите элементы массива: '))
x = int(input('Введите значение числа: '))
flag = False
l = 0
r = len(a) - 1
'''
stmt = '''
while l <= r and not flag:
    k = (l + r) // 2
    if a[k] == x:
        flag = True
    elif a[k] < x:
        l = k + 1
    else:
        r = k - 1
if not flag:
    print('элемент не был найден')
else:
    print('элемент', x, 'был найден в положении: ', k)
'''
print('Время поиска', timeit.timeit(stmt = stmt, setup = setup, number = 1), 'секунд')
