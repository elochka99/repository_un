#Горохова Е. КНИТ 16-А
import numpy as np
z = 'да'
while z == 'да':
    try:
        h = int(input("Выберите действие:\n"
                "1- поворот массива на 90 градусов по часовой стрелке;  \n"
                "2- циклический сдвиг линейного массива на К позиций влево;  \n"
                "3- произведение двух квадратных матриц, учитывая размерность;  \n"
                "4- вычисление определителя квадратной матрицы;  \n"
                "Ваш выбор: "))
        if h == 1: #поворот на 90 градусов
            n = int(input('Введите размерность матрицы '))
            a = np.ones((n, n), dtype=np.int_)
            for i in range(n):
                for j in range(n):
                    print('a[', i, '][', j, ']: ', end='')
                    a[i][j] = int(input())
            i = 0
            n -= 1
            print('Начальная матрица: \n', a)
            for j in range(n):
                a[i + j][n], a[n][n - j], a[n - j][i], a[i][j] = a[i][j], a[i + j][n], a[n][n - j], a[n - j][i]
            print('Перевернутая матрица: \n', a)
        elif h == 2: # сдвиг на К позиций влево
            n = int(input('Ввведите количество элементов массива: '))
            a = np.zeros(n, dtype=np.int_)
            for i in range(n):
                print('a[', i, ']: ', end='')
                a[i] = int(input())
            k = int(input('Укажите на какое количество элементов сдвинуть: '))
            if k > n:
                k = k % n
            i = 0
            t = a[i]
            for j in range(n):
                i -= k
                if i < 0:
                    i += n
                t, a[i] = a[i], t
            print('Сдвинутая матрица: ', a)
        elif h == 3:  #произведение двух квадратных матриц
            n = int(input('Введите размерность первой и второй квадратной матрицы: '))
            m = n
            a = np.ones((n, m), dtype=np.int_)
            b = np.zeros((n, m), dtype=np.int_)
            c = np.zeros((n, m), dtype=np.int_)
            for i in range(n):
                for j in range(m):
                    print('a[', i, '][', j, ']: ', end='')
                    a[i][j] = int(input())
            for i in range(n):
                for j in range(m):
                    print('b[', i, '][', j, ']: ', end='')
                    b[i][j] = int(input())
            for i in range(n):
                for j in range(n):
                    s = 0
                    p = 0
                    for k in range(n):
                        c[i][j] += a[i][k] * b[k][j]
            print('Произведение матриц: \n', c)
        elif h == 4: #Определитель матрицы
            n = int(input('Введите размерность квадратной матрицы: '))
            a = np.zeros((n, n), dtype=np.int)
            for i in range(n):
                for j in range(n):
                    print('a[', i, '][', j, ']: ', end='')
                    a[i][j] = int(input())  # Заполняем массив
            r = 0
            op = 1
            while r != n - 1:
                gd = a[r, r]
                op *= gd  # Сохраняем произведение главной диагонали
                for i in range(r + 1, n):
                    vit = a[i][r] / gd  # Находим значение которое нужно вычесть
                    for j in range(n):
                        a[i, j] -= vit * a[r][j]  # Вычетаем значение от строки
                r += 1
            print('Определитель матрицы = ', '%.0f' % (op * a[r][r]))
        else:
            print("Выберите действие из предложенных")
    except:
        print('Введена ошибка')
    print()
    print('Для продолжения работы с программой введите "да", чтобы вийти - нажмите любой символ')
    z = input()
    print()
