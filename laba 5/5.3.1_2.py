# Горохова Елена КНИТ 16-А
# Программа, которая будет содержать функции вычисления суммы элементов квадратной матрицы,произведения элементов,
# поиска элемента с заданным значением в квадратной матрице
from random import random
import numpy as np
from copy import deepcopy

def summa(a, n):
    '''
    Функция итерационно возвращает сумму всех элементов суммируя их
    
    :param a: массив
    :param n: счетчик
    :return: сумму єлементов
    '''
    for i in a:
        for j in i:
            n += j
    return n
def summa_rek(a):
    '''
    Функция рекурсивно возвращает сумму всех элементов суммируя их 
    
    :param a: массив
    :return:  сумму єлементов
    '''
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + summa_rek(a[1:])

def proiz(a, n):
    '''
    Функция возвращает итерационно произведение єлементов переуманожая их
    :param a: массив
    :param n: счетчик
    :return: произведение єлементов
    '''
    for i in a:
        for j in i:
            n *= j
    return n
def proiz_rek(a):
    '''
    Функция возвращает рекурсивно произведение элементов 
    :param a: массив
    :return: произведение элементов
    '''
    if len(a) == 1:
         return a[0]
    else:
         return a[0] * proiz_rek(a[1:])
def seach(a,k):
    '''
    Функция возвращает итерационно местоположение элемента методом прохода всей матрицы
    :param a: массив
    :param k: искомый элемент
    :return: местоположение k
    '''
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == k:
                return i+1, j+1
def seach_rec(a, k, row, col, visited):
    '''
    Функция работает рекурсивно она рекурсивно ищет элементы сравнивая их с нашим 
    искомым числом на каждой рекурсии смещаясь на одно число в направлении пути матрицы

    :param a: матрица которую мы передаём 
    :param k: искомый элимент 
    :param row: строки
    :param col: столбы
    :param visited: копированый массив для сравнения 
    :return: возвращает координаты расположения числа 
    '''
    if row >= len(a) or col >= len(a[0]) or visited[row][col] or row < 0 or col < 0:
        return False
    visited[row][col] = True
    if a[row][col] == k:
        print(row+1, col+1)
    else:
        seach_rec(a, k,row, col + 1,  visited)
        seach_rec(a, k,row - 1, col,  visited)
        seach_rec(a, k,row + 1, col,  visited)
        seach_rec(a, k,row, col - 1,  visited)
while True:
    n = 0
    try:
        b = int(input("какая размерность матрицы? - "))
        a = np.zeros((b, b), dtype=int)
        visited = deepcopy(a)
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
        print("рекурсивно число на месте - ")
        seach_rec(a, k, 0, 0, visited)
    except ValueError:
        print("Введите корректные данные!")
        continue