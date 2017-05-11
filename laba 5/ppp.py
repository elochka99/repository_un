# Горохова Елена КНИТ 16-А
# Сформировать функцию подсчета количества разных представлений заданного натурального числа в виде
# суммы не менее двух попарно различных натуральных слагаемых
import numpy as np
def rec_decompose(c):
    def func(c, id):
        if c == 0 and id == 0:
            return 1
        if c <= 0 or id <= 0:
            return 0
        return func(c - id, id) + func(c - 1, id - 1)
    stack = []
    if c == 0 or c == 1:
        return 0
    for i in range(1, c):
        stack.append(func(c, i))
    return max(stack)
def number_decompose_iter(n):
    """ Функция подсчета количества различных представлений заданого числа.
     Итерационно

    :param n: заданное натуральное число 
    :return: количество различных представлений числа n 
    """
    a = 0
    n1 = n
    c = 0  # количество представлений числа n
    while n1 >= 0:
        a += 1
        n1 -= a
    mas = np.zeros(a - 1, dtype=int)
    for i in range(0, a - 1):
        mas[i] = i + 1
    if n1 != 0:
        mas[a - 2] = mas[a - 3] + a + 1 + n1
    a -= 1
    for i in range(0, a):
        pass
    c += 1
    while a > 1:
        for j in range(a - 2, -1, -1):
            temp1 = mas[j]
            temp2 = mas[a - 1]
            while mas[j] + 1 < mas[a - 1] - 1:
                mas[j] += 1
                mas[a - 1] -= 1
                n1 = 0
                for i in range(0, a - 1):
                    for i1 in range(i + 1, a):
                        if mas[i] == mas[i1]:
                            n1 = 1
                if n1 == 0:
                    for i in range(0, a):
                        pass
                    c += 1
            mas[j] = temp1
            mas[a - 1] = temp2
        mas[a - 2] += mas[a - 1]
        a -= 1
    if n > 5:
        return c + 1
    else:
        return c

def rec(n, m):
    '''
    Функция рекурсивно считает количество разных представлений числа
    :param n: число
    :param m: число
    :return: число
    '''
    if m == 0:
        if n == 0:
            return 1
        return 0
    if m <= n:
        return rec(n, m-1) + rec(n - m, m)
    return rec(n,n)
def iter(n, m):
    '''
    Функция рекурсивно считает количество разных представлений числа
    :param n: число
    :param m: число
    :return: число
    '''
    s = 0
    a = []
    a.append((n, m))
    while a:
        r = a.pop()
        b = r[0]
        c = r[1]
        if c == 0:
            if b == 0:
                s += 1
        elif c > b:
            a.append((b, b))
        elif c <= b:
            a.append((b, c - 1))
            a.append((b - c, c))
    return s
while True:
    try:
        n = m = int(input('N = '))
        if n <= 0 or m <= 0:
            print('Не правильное число')
        else:
            kol = rec(n,m)
            kol1 = iter(n, m)
            print('Количество представлений заданного числа: ',"\nрекурсивно - ",kol, "\nитерационно - ", kol1)
            print("без 1+1+1... рекурсивно = ", rec_decompose(n) )
            print("без 1+1+1... итерационно = ", number_decompose_iter(n))
        w = input('\nХотите начать работу с программой заново? [1 - да]: ')
        if w == '1':
            print()
            continue
        else:
            print("пока!")
            break
    except (ValueError, RecursionError, MemoryError):
        print("Введите коректные данные!")
