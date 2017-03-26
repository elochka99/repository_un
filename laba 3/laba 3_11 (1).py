#Горохова Е. КНИТ 16-А
#Повернуть матрицу на 90 градусов по часовой стрелке
import numpy as np
z = 'да'
while z == 'да':
    try:
        n = int(input('Введите размерность матрицы '))
        a = np.ones((n, n), dtype = np.int_)
        for i in range(n):
            for j in range(n):
                print('a[',i,'][',j,']: ', end = '')
                a[i][j] = int(input())
        i = 0
        n -= 1
        print('Начальная матрица: \n',a)
        for j in range(n):
            a[i+j][n], a[n][n-j], a[n-j][i], a[i][j]= a[i][j], a[i+j][n],a[n][n-j],a[n-j][i]
        print('Перевернутая матрица: \n',a)
    except:
        print('Введена ошибка')
    print()
    print('Для продолжения работы с программой введите "да", чтобы вийти - нажмите любой символ')
    z = input()
    print()