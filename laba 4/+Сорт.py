# Горохова Елена КНИТ 16-А
import numpy as np
import random
import time

def bubble_sort(A):
    """

    :param A:
    :return:
    """
    '''Сортировка пузырьком.

               В качестве аргумента нужно задать массив, который необходимо отсортировать.

               Сортировка простыми обменами, сортировка пузырьком — простой алгоритм сортировки.
               Для понимания и реализации этот алгоритм — простейший, но эффективен он лишь для небольших массивов.
               Сложность алгоритма: O(n**2).'''
    count1 = 0
    count2 = 0
    N = len(A)
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(N-i-1):
            count1 += 1
            if A[j] > A[j+1]:
                tmp = A[j]
                A[j] = A[j+1]
                A[j + 1] = tmp
                count2 += 1
                flag = True
        i += 1
    print('Произведено сравнений:', count1)
    print('Произведено перестановок:', count2)
    return A

def selection_sort(A):
    '''Сортировка выбором

                В качестве аргумента нужно задать массив, который необходимо отсортировать.

                Сортировка выбором — алгоритм сортировки. Может быть как устойчивый, так и неустойчивый.
                На массиве из n элементов имеет время выполнения в худшем, среднем и лучшем случае O(n**2), предполагая
                 что
                сравнения делаются за постоянное время.'''
    count1 = 0
    count2 = 0
    N = len(A)
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            count1 += 1
            if A[j] < A[min]:
                min = j
        count2 += 1
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
    print('Произведено сравнений:', count1)
    print('Произведено перестановок:', count2)
    return A

def insertion_sort(A):
    '''Сортировка вставками.

                В качестве аргумента нужно задать массив, который необходимо отсортировать.

                Сортировка вставками — алгоритм сортировки, в котором элементы входной
                последовательности просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее
                место среди ранее упорядоченных элементов.
                Вычислительная сложность — O(n**2)'''
    count1 = 0
    count2 = 0
    N = len(A)
    for i in range(1, N):
        j = i - 1
        key = A[i]
        count1 += 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            count2 += 1
            j -= 1
        A[j+1] = key
    print('Произведено сравнений:', count1)
    print('Произведено перестановок:', count2)
    return A

def cocktail_sort(A):
    '''Сортировка перемешиванием.

                В качестве аргумента нужно задать массив, который необходимо отсортировать.

               Сортировка перемешиванием, или двунаправленная — разновидность пузырьковой сортировки.
               Лучший случай для этой сортировки — отсортированный массив O(n), худший — отсортированный в обратном
                порядке O(n**2).'''
    count1 = 0
    count2 = 0
    N = range(len(A) - 1)
    while True:
        for j in (N, reversed(N)):
            flag = False
            for i in j:
                count1 += 1
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    count2 += 1
                    flag = True
            if not flag:
                print('Произведено сравнений:', count1)
                print('Произведено перестановок:', count2)
                return A

def shell_sort(A):
    '''Сортировка Шелла.

                   В качестве аргумента нужно задать массив, который необходимо отсортировать.

                   Сортировка Шелла  — алгоритм сортировки, являющийся усовершенствованным вариантом сортировки
                   вставками. Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом, но и на
                   определённом
                   расстоянии друг от друга. Иными словами — это сортировка вставками с предварительными "грубыми"
                   проходами.'''
    count1 = 0
    count2 = 0
    n = len(A)
    while True:
        n = n//2
        for i in range (n, len(A), n):
            j = i
            count1 += 1
            while j>0 and A[j] < A[j-n]:
                A[j], A[j-n] = A[j-n], A[j]
                count2 += 1
                j = j - n
        if n ==  1:
            break
    print('Произведено сравнений:', count1)
    print('Произведено перестановок:', count2)
    return A

def heap_sort(li):
    '''Пирамидальная сортировка

                В качестве аргумента нужно задать массив, который необходимо отсортировать.

                Пирамидальная сортировка — алгоритм сортировки, работающий в худшем,
                в среднем и в лучшем случае (то есть гарантированно) за О(n log n) операций при сортировке n элементов.
                Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1)).'''
    count1 = 0
    count2 = 0
    def down_Heap(li, k, n):
        '''
        Функция создает бинарное сортировочное дерево

        где li - начальный элемент, k - конечный элемент, n - сам массив
        '''
        nonlocal count1
        nonlocal count2
        new_elem = li[k]
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

    size = len(li)
    for i in range(size//2-1,-1,-1):
        down_Heap(li, i, size)
    for i in range(size-1,0,-1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        count2 += 1
        down_Heap(li, 0, i)
    end6 = time.time()
    print('Произведено сравнений:', count1)
    print('Произведено перестановок:', count2)
    print('Время выполнения алгоритма: ', end6 - start6)
    return li

while True:
    print('Как Вы хотите вводить информацию в БД: вручную или рандомно? [1/2]')
    while True:
        try:
            ask_inp = int(input('Выберите цифру → '))
            n = int(input("Введите кол во элeментов в массиве: "))
            A = np.zeros(n, dtype=int)
            if ask_inp == 1:
                for j in range(n):
                    A[j] = int(input("Заполните матрицу: "))
            elif ask_inp == 2:
                for j in range(n):
                    A[j] = random.randint(0, 100000)
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
            print("колчество элементов: ", n)
            print("Ваша последовательность чисел: ", A )
            break
        except ValueError:
            print('Пожалуйста, введите целое число ☻\n')
            continue
    print('Каким методом сортировать? \n[1 - bubble / 2 - selection / 3 - insertion / 4 - cocktail / 5 - shell / 6 - heapsort ]')
    while True:
        try:
            ask = int(input('Выберите цифру → '))
            if ask == 1:
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                t = time.clock()
                if order == "1":
                    print("Отсортированная последовательность bubble_sort по возрастанию: ", bubble_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность bubble_sort по убыванию: ", bubble_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            elif ask == 2:
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                t = time.clock()
                if order == "1":
                    print("Отсортированная последовательность selection_sort по возрастанию: ", selection_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность selection_sort по убыванию: ", selection_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            elif ask == 3:
                t = time.clock()
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                if order == "1":
                    print("Отсортированная последовательность insertion_sort по возрастанию: ", insertion_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность insertion_sort по убыванию: ", insertion_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            elif ask == 4:
                t = time.clock()
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                if order == "1":
                    print("Отсортированная последовательность cocktail_sort по возрастанию: ", cocktail_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность cocktail_sort по убыванию: ", cocktail_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            elif ask == 5:
                t = time.clock()
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                if order == "1":
                    print("Отсортированная последовательность shell_sort по возрастанию: ", shell_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность shell_sort по убыванию: ", shell_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            elif ask == 6:
                t = time.clock()
                order = input("1 - по возростанию \ 2 - в порядке убывания :")
                if order == "1":
                    print("Отсортированная последовательность heap_sort по возрастанию: ", heap_sort(A))
                elif order == "2":
                    print("Отсортированная последовательность heap_sort по убыванию: ", heap_sort(-A) * -1)
                else:
                    print('Пожалуйста, введите корректные данные ☻\n')
                    continue
                print(str(time.clock() - t))
            else:
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
            #print(str(time.clock() - t))
            s = input('\nХотите сортировать еще раз другим алгоритмом? [1 - да]: ')
            if s == '1':
                print()
                continue
            else:
                break
        except ValueError:
            print('Пожалуйста, введите целое число ☻\n')
            continue

    r = input('\nХотите начать работу с программой заново? [1 - да]: ')
    if r == '1':
        print()
        continue
    else:
        break
