# Горохова Елена КНИТ 16-А

import numpy as np
import random
import time

def bubble_sort(A, r):
    """
    Сортировка пузырьком
     Это алгоритм сортировки, который многократно перебирает список, чтобы
     отсортировать, сравнивает каждую пару смежных элементов и меняет их, 
     если они находятся в неправильном порядке. Сложность алгоритма: O(n**2).
    
    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    flag = True
    count1 = 0
    count2 = 0
    N = len(A)
    for i in range(1, N):
        if flag:
            flag = False
            for j in range(N - 1, i - 1, -1):
                count1 += 1
                if r == 1:
                    if A[j - 1] > A[j]:
                        A[j], A[j - 1] = A[j - 1], A[j]
                        count2 += 1
                        flag = True
                elif r == 2:
                    if A[j - 1] < A[j]:
                        A[j], A[j - 1] = A[j - 1], A[j]
                        count2 += 1
                        flag = True
        else:
            break
    return A,  count1,  count2

def selection_sort(A, r):
    """
    Сортировка выбором
    
    Это алгоритм сортировки, в частности сортировка выбором на месте. 
    На массиве из n элементов имеет время выполнения в худшем, среднем и лучшем случае O(n**2).
       
    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """

    N = len(A)
    count1 = 0
    count2 = 0
    for i in range(N):
        minim = i
        for j in range(i + 1, N):
            count1 += 1
            if r == 1:
                if A[j] < A[minim]:
                    minim = j
            elif r == 2:
                if A[j] > A[minim]:
                    minim = j
        A[i], A[minim] = A[minim], A[i]
        count2 += 1
    return A, count1, count2

def insertion_sort(A, r):
    """
    Сортировка вставками.
    
    Aлгоритм сортировки, в котором элементы входной последовательности 
    просматриваются по одному, и каждый новый поступивший элемент
    размещается в подходящее место среди ранее упорядоченных элементов.
    Вычислительная сложность — O(n**2)'''
    
    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    count1 = 0
    count2 = 0
    N = len(A)
    for i in range(N):
        j = i
        count1 += 1
        if r == 1:
            while j > 0 and A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                count2 += 1
                j -= 1
        elif r == 2:
            while j > 0 and A[j] > A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                count2 += 1
                j -= 1
    return A, count1, count2

def cocktail_sort(A, r):
    """
    Сортировка перемешиванием.
    
    Сортировка перемешиванием, или двунаправленная — разновидность пузырьковой сортировки.
    Лучший случай для этой сортировки — отсортированный массив O(n), худший — отсортированный в обратном
    порядке O(n**2)
    
    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """

    count1 = 0
    count2 = 0
    N = range(len(A) - 1)
    while True:
        for j in (N, reversed(N)):
            flag = False
            for i in j:
                count1 += 1
                if r == 1:
                    if A[i] > A[i + 1]:
                        A[i], A[i + 1] = A[i + 1], A[i]
                        count2 += 1
                        flag = True
                elif r == 2:
                    if A[i] < A[i + 1]:
                        A[i], A[i + 1] = A[i + 1], A[i]
                        count2 += 1
                        flag = True
            if not flag:
                return A, count1, count2

def shell_sort(A, r):
    """
    Сортировка Шелла.
    
    алгоритм сортировки, являющийся усовершенствованным вариантом сортировки вставками. 
    Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом, но и на
    определённом расстоянии друг от друга.
    
    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    count1 = 0
    count2 = 0
    n = len(A)//2
    while n > 0:
        n = n//2
        for i in range (n, len(A), n):
            j = i
            count1 += 1
            if r == 1:
                while j>0 and A[j] < A[j-n]:
                    A[j], A[j-n] = A[j-n], A[j]
                    count2 += 1
                    j -= n
            if r == 2:
                while j>0 and A[j] > A[j-n]:
                    A[j], A[j-n] = A[j-n], A[j]
                    count2 += 1
                    j -= n

        if n ==  1:
            break
    return A, count1, count2

def heap_sort(li, r):
    """
    Пирамидальная сортировка

    Пирамидальная сортировка — алгоритм сортировки, работающий в худшем,
    в среднем и в лучшем случае (то есть гарантированно) за О(n log n) операций при сортировке n элементов.
    Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1)).
    
    :param li: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    count1 = 0
    count2 = 0
    def down_Heap(li, k, n):
        """
        Функция создает бинарное сортировочное дерево
        :param li: начальный элемент
        :param k: конечный элемент
        :param n: сам массив
        :return: возвращает сортированное дерево
        """
        nonlocal count1
        nonlocal count2
        new_elem = li[k]
        if r == 1:
            while 2*k+1 < n:
                child = 2*k+1
                count1 += 1
                if child+1 < n and li[child] < li[child+1]:
                    child += 1
                    count2 += 1
                if new_elem >= li[child]:
                    break
                li[k] = li[child]
                k = child
            li[k] = new_elem
        elif r == 2:
            while 2 * k + 1 < n:
                child = 2 * k + 1
                count1 += 1
                if child + 1 < n and li[child] > li[child + 1]:
                    child += 1
                    count2 += 1
                if new_elem <= li[child]:
                    break
                li[k] = li[child]
                k = child
            li[k] = new_elem

    size = len(li)
    for i in range(size//2-1,-1,-1):
        down_Heap(li, i, size)
    for i in range(size-1,0,-1):
        li[i], li[0] = li[0], li[i]
        count2 += 1
        down_Heap(li, 0, i)
    return li, count1, count2

def sort(A):
    """
    Функция создана для проверки на эффективность всех алгоритмов сортировки с помощью
     тестового массива в 100000 элементов.
    :param A: массив
    :return: эффективность алгоритмов
    """
    t = time.clock()
    res = str(bubble_sort(A, 1)).split()
    print("Отсортированная последовательность bubble_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(bubble_sort(A, 2)).split()
    print("Отсортированная последовательность bubble_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(selection_sort(A, 1)).split()
    print("Отсортированная последовательность selection_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(selection_sort(A, 2)).split()
    print("Отсортированная последовательность selection_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(insertion_sort(A, 1)).split()
    print("Отсортированная последовательность insertion_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(insertion_sort(A, 2)).split()
    print("Отсортированная последовательность insertion_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(cocktail_sort(A, 1)).split()
    print("Отсортированная последовательность cocktail_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(cocktail_sort(A, 2)).split()
    print("Отсортированная последовательность cocktail_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(shell_sort(A, 1)).split()
    print("Отсортированная последовательность shell_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(shell_sort(A, 2)).split()
    print("Отсортированная последовательность shell_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(heap_sort(A, 1)).split()
    print("Отсортированная последовательность heap_sort по возрастанию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

    t = time.clock()
    res = str(heap_sort(A, 2)).split()
    print("Отсортированная последовательность heap_sort по убыванию: ", res[1:-2])
    print('Произведено сравнений:', res[-2])
    print('Произведено перестановок:', res[-1])
    print("время работы: ", str(time.clock() - t))

while True:
    vop = input(print("Вы хотите отсортировать массив [1] или посмотреть "
                      "эффективности алгоритмов на тестовм массиве [2]? - "))
    while True:
        if vop == "1":
            while True:
                try:
                    n = int(input("Введите количество элeментов в массиве: "))
                    if n <= 500000:
                        A = np.zeros(n, dtype=int)
                        print('Как Вы хотите вводить информацию в БД: вручную или рандомно? [1/2]')
                        ask_inp = int(input('Выберите цифру → '))
                        if ask_inp == 1:
                            if n <= 30:
                                for j in range(n):
                                    A[j] = int(input("Заполните матрицу: "))
                            else:
                                print("Вы можете ввести вручную не больше 30 элементов!")
                                continue
                        elif ask_inp == 2:
                            for j in range(n):
                                A[j] = random.randint(0, 100000)
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue

                        print("колчество элементов: ", n)
                        print("Ваша последовательность чисел: ", A )
                        break
                    else:
                        print("Для нормальной работы программы введите число менее 500 000")
                        continue

                except ValueError:
                    print('Пожалуйста, введите целое число не более 9 символов ☻\n')
                    continue
            print('Каким методом сортировать? \n[1 - bubble / 2 - selection / 3 - insertion / 4 - cocktail / 5 - shell / 6 - heapsort ]')
            while True:
                try:
                    ask = int(input('Выберите цифру → '))
                    if ask == 1:
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        t = time.clock()
                        if order == "1":
                            res = str(bubble_sort(A, 1)).split( )
                            print("Отсортированная последовательность bubble_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(bubble_sort(A, 2)).split()
                            print("Отсортированная последовательность bubble_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str(time.clock() - t))
                    elif ask == 2:
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        t = time.clock()
                        if order == "1":
                            res = str(selection_sort(A, 1)).split()
                            print("Отсортированная последовательность selection_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(selection_sort(A, 2)).split()
                            print("Отсортированная последовательность selection_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str(time.clock() - t))
                    elif ask == 3:
                        t = time.clock()
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        if order == "1":
                            res = str(insertion_sort(A, 1)).split()
                            print("Отсортированная последовательность insertion_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(insertion_sort(A, 2)).split()
                            print("Отсортированная последовательность insertion_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str(time.clock() - t))
                    elif ask == 4:
                        t = time.clock()
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        if order == "1":
                            res = str(cocktail_sort(A, 1)).split()
                            print("Отсортированная последовательность cocktail_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(cocktail_sort(A, 2)).split()
                            print("Отсортированная последовательность cocktail_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str(time.clock() - t))
                    elif ask == 5:
                        t = time.clock()
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        if order == "1":
                            res = str(shell_sort(A, 1)).split()
                            print("Отсортированная последовательность shell_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(shell_sort(A, 2)).split()
                            print("Отсортированная последовательность shell_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str(time.clock() - t))
                    elif ask == 6:
                        t = time.clock()
                        order = input("1 - по возростанию \ 2 - в порядке убывания :")
                        if order == "1":
                            res = str(heap_sort(A, 1)).split()
                            print("Отсортированная последовательность heap_sort по возрастанию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        elif order == "2":
                            res = str(heap_sort(A, 2)).split()
                            print("Отсортированная последовательность heap_sort по убыванию: ", res[1:-2])
                            print('Произведено сравнений:', res[-2])
                            print('Произведено перестановок:', res[-1])
                        else:
                            print('Пожалуйста, введите корректные данные ☻\n')
                            continue
                        print("время работы: ", str( time.clock() - t))
                    else:
                        print('Пожалуйста, введите корректные данные ☻\n')
                        continue
                    s = input('\nХотите сортировать еще раз другим алгоритмом? [1 - да]: ')
                    if s == '1':
                        print()
                        continue
                    else:
                        break
                except ValueError:
                    print('Пожалуйста, введите корректные данные (число) ☻\n')
                    continue
        elif vop == "2":
            n = 1000
            A = np.zeros(n, dtype=int)
            for j in range(n):
                A[j] = random.randint(0, 100000)
            qwer = input(print("Вывести\n [1] - эффективность для сгенерированной псевдослучайной последовательности \n "
                               "[2] - эффективность для отсортированной последовательности в порядке неубывания \n"
                               "[3] - эффективность для отсортированной последовательности в порядке невозрастания\n"
                               "Ваш ответ - "))

            if qwer == "1":
                print("количество элементов в массиве: ", n)
                print("сгенерированный массив: \n", A)
                print(sort(A))
            elif qwer == "2":
                B = sorted(A)
                print("количество элементов в массиве: ", n)
                print("отсортированный массив в порядке неубывания: \n", B)
                print(sort(B))
            elif qwer == "3":
                C = sorted(A, reverse = True)
                print("количество элементов в массиве: ", n)
                print("отсортированный массив в порядке невозрастания: \n", C)
                print(sort(C))
            else:
                print("введите коректные данные!")
                continue
        else:
            print("введите коректные данные!")
            continue
        y = input('\nХотите поработать еще с этим? [1 - да]: ')
        if y == '1':
            print()
            continue
        else:
            break

    w = input('\nХотите начать работу с программой заново? [1 - да]: ')
    if w == '1':
        print()
        continue
    else:
        print("пока!")
        break
