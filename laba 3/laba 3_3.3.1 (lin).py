#Горохова Елена КНИТ 16-А
#линейный поиск
import timeit
setup = '''
import numpy as np
#import random as rnd
n = int(input('Количество элементов в массиве: '))
a = np.zeros(n, dtype = np.int_)
for j in range(n):
    a[j] = int(input('Вводите элменти массива: '))
x = float(input('искомый элемент x:  '))
i = 0
'''
stmt = '''
while i < n and a[i] != x:
    i += 1
if i == n:
    print('элемент не найден')
else:
    print('элемент', x, 'находится в позиции', i)
'''
print('время поиска', timeit.timeit(stmt = stmt, setup = setup, number = 1), 'секунд')
