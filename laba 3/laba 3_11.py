#Горохова Е. КНИТ 16-А
#Повернуть матрицу на 90 градусов по часовой стрелке
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
        if h == 1:
            n = int(input('Введите размерность матрицы '))
            a = np.ones((n, n), dtype = np.int_)
            for i in range(n):
                for j in range(n):
                    print('a[',i,'][',j,']: ', end = '')
                    a[i][j] = int(input())
            print('Начальная матрица: \n',a)
            print('Перевернутая матрица: \n',np.rot90(a,-1))
        elif h == 2:
            n = int(input('Ввведите количество элементов массива: '))
            a = np.zeros(n, dtype=np.int_)
            for i in range(n):
                print('a[', i, ']: ', end='')
                a[i] = int(input())
            M = int(input('Укажите на какое количество элементов нужно сдвинуть: '))
            b = np.roll(a,-M)
            print('сдвинутая матрица: ', b)
        elif h == 3:
            n = int(input('введите размерность квадратных матриц: '))
            m = n
            a = np.zeros((n, m), dtype=np.int)
            b = np.zeros((n, m), dtype=np.int)
            for i in range(n):
                for j in range(m):
                    print('a[', i, '][', j, ']: ', end='')
                    a[i][j] = int(input())
            for i in range(n):
                for j in range(m):
                    print('b[', i, '][', j, ']: ', end='')
                    b[i][j] = int(input())
            k = np.dot(a,b)
            print('Произведение матриц: \n',k )
        elif h == 4:
            n = int(input('Введите размерность квадратной матрицы: '))
            a = np.zeros((n, n), dtype=np.int)
            for i in range(n):
                for j in range(n):
                    print('a[', i, '][', j, ']: ', end='')
                    a[i][j] = int(input())  # Заполняем массив
            b = int(np.linalg.det(a))
            print('Определитель матрицы = ',b)
        else:
            print("Выберите действие из предложенных")
    except:
        print('Введена ошибка')
    print()
    print('Для продолжения работы с программой введите "да", чтобы вийти - нажмите любой символ')
    z = input()
    print()
