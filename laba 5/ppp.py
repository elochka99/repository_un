import time
import numpy as np
import random


def vivod(arr):
    arr2 = list(arr)
    t = time.clock()
    arres = (piramid_sort(arr2, True))
    print("Массив пирамида: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()
    arr2 = list(arr)
    t = time.clock()
    arres = (koktel_sort(arr2, True))
    print("Массив коктель: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()
    arr2 = list(arr)
    t = time.clock()
    arres = (viborka(arr2, True))
    print("Массив выборка: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()
    arr2 = list(arr)
    t = time.clock()
    arres = (vstavka(arr2, True))
    print("Массив вставка: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()
    arr2 = list(arr)
    t = time.clock()
    arres = (hell(arr2, True))
    print("Массив шелл: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()
    arr2 = list(arr)
    t = time.clock()
    arres = (puzir(arr2, True))
    print("Массив пузырь: ", arres[0])
    print("Кол во сравнений: ", arres[1])
    print("Кол во перестановок: ", arres[2])
    print(str(time.clock() - t))
    print()


def piramid_sort(arr, revers):
    """
   Пирамидальная сортировка
   Пирамидальная сортировка — алгоритм сортировки, работающий в худшем,
   в среднем и в лучшем случае (то есть гарантированно) за О(n log n) операций при сортировке n элементов.
   Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1)).

   :param li: Принимает массив.
   :param r: выбор направления сортировки
   :return: возвращает отсортированный массив, сравнения и сумму обменов.
   """


ks = 0
kp = 0
arr2 = arr


def downHeap(arr2, k, n):
    """
   Функция создает бинарное сортировочное дерево
   :param li: начальный элемент
   :param k: конечный элемент
   :param n: сам массив
   :return: возвращает сортированное дерево
   """


nonlocal ks
nonlocal kp
new_elem = arr2[k]
if revers:
    while 2 * k + 1 < n:
        child = 2 * k + 1
        ks += 1
        if child + 1 < n and arr2[child] < arr2[child + 1]:
            child += 1
            kp += 1
        if new_elem >= arr2[child]:
            break
        arr2[k] = arr2[child]
        k = child
    arr2[k] = new_elem
else:
    while 2 * k + 1 < n:
        child = 2 * k + 1
        ks += 1
        if child + 1 < n and arr2[child] > arr2[child + 1]:
            child += 1
            kp += 1
        if new_elem <= arr2[child]:
            break
        arr2[k] = arr2[child]
        k = child
    arr2[k] = new_elem
size = len(arr2)
for i in range(size // 2 - 1, -1, -1):
    downHeap(arr2, i, size)
for i in range(size - 1, 0, -1):
    temp = arr2[i]
    arr2[i] = arr2[0]
    arr2[0] = temp
    kp += 1
    downHeap(arr2, 0, i)
return arr2, ks, kp


def koktel_sort(arr, revers):
    """
    Сортировка перемешиванием.

    Сортировка перемешиванием, или двунаправленная — разновидность пузырьковой сортировки.
    Лучший случай для этой сортировки — отсортированный массив O(n), худший — отсортированный в обратном
    порядке O(n**2)

    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    left = 0
    arr2 = arr
    right = len(arr2) - 1
    ks = 0
    kp = 0
    if revers:
        while left <= right:
            for i in range(left, right, +1):
                ks += 1
                if arr2[i] > arr2[i + 1]:
                    arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]
                    kp += 1

            right -= 1
            for i in range(right, left, -1):
                ks += 1
                if arr2[i - 1] > arr2[i]:
                    arr2[i], arr2[i - 1] = arr2[i - 1], arr2[i]
                    kp += 1

            left += 1
    else:
        while left <= right:
            for i in range(left, right, +1):
                if arr2[i] < arr2[i + 1]:
                    arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]
                    kp += 1
            ks += 1
            right -= 1
            for i in range(right, left, -1):
                if arr2[i - 1] < arr2[i]:
                    arr2[i], arr2[i - 1] = arr2[i - 1], arr2[i]
                    kp += 1
            ks += 1
            left += 1
    return arr2, ks, kp


def viborka(arr, revers):
    """
    Сортировка выбором

    Это алгоритм сортировки, в частности сортировка выбором на месте. 
    На массиве из n элементов имеет время выполнения в худшем, среднем и лучшем случае O(n**2).

    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    a = arr
    ks = 0
    kp = 0
    if revers:
        for i in range(b):
            Min = i
            for j in range(i + 1, b):
                ks += 1
                if a[j] < a[Min]:
                    Min = j
            a[i], a[Min] = a[Min], a[i]
            kp += 1
    else:
        for i in range(b):
            Min = i
            for j in range(i + 1, b):
                ks += 1
                if a[j] > a[Min]:
                    Min = j
            a[i], a[Min] = a[Min], a[i]
            kp += 1

    return a, ks, kp


def vstavka(arr, revers):
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
    a = arr
    ks = 0
    kp = 0
    if revers:
        for i in range(1, b):
            k = i
            ks += 1
            while a[k - 1] > a[k] and k > 0:
                a[k], a[k - 1] = a[k - 1], a[k]
                k -= 1
                kp += 1
    else:
        for i in range(1, b):
            k = i
            ks += 1
            while a[k - 1] < a[k] and k > 0:
                a[k], a[k - 1] = a[k - 1], a[k]
                k -= 1
                kp += 1
    return a, ks, kp


def hell(arr, revers):
    """
    Сортировка Шелла.

    алгоритм сортировки, являющийся усовершенствованным вариантом сортировки вставками. 
    Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом, но и на
    определённом расстоянии друг от друга.

    :param A: Принимает массив.
    :param r: выбор направления сортировки
    :return: возвращает отсортированный массив, сравнения и сумму обменов.
    """
    n = len(arr)
    kp = 0
    ks = 0
    arr2 = arr
    if revers:
        while True:
            n = n // 2
            for i in range(n, len(arr2), n):
                k = i
                ks += 1
                while k > 0 and arr2[k] < arr2[k - n]:
                    arr2[k], arr2[k - n] = arr2[k - n], arr2[k]
                    k -= n
                    kp += 1
            if n == 1:
                break
    else:
        while True:
            n = n // 2
            for i in range(n, len(arr2), n):
                k = i
                ks += 1
                while k > 0 and arr2[k] > arr2[k - n]:
                    arr2[k], arr2[k - n] = arr2[k - n], arr2[k]
                    k -= n
                    kp += 1
            if n == 1:
                break
    return arr2, ks, kp


def puzir(arr, revers):
    """
   Сортировка пузырьком
    Это алгоритм сортировки, который многократно перебирает список, чтобы
    отсортировать, сравнивает каждую пару смежных элементов и меняет их, 
    если они находятся в неправильном порядке. Сложность алгоритма: O(n**2).

   :param A: Принимает массив.
   :param r: выбор направления сортировки
   :return: возвращает отсортированный массив, сравнения и сумму обменов.
   """


m = len(arr) - 1
ks = 0
kp = 0
arr2 = arr
while m > 0:
    for i in range(m):
        ks += 1
        if revers == True:
            if arr2[i] > arr2[i + 1]:
                kp += 1
                x = arr2[i]
                arr2[i] = arr2[i + 1]
                arr2[i + 1] = x

        else:
            if arr2[i] < arr2[i + 1]:
                x = arr2[i]
                arr2[i] = arr2[i + 1]
                arr2[i + 1] = x
                kp += 1
    m -= 1
return arr2, ks, kp
while True:
    try:
        vopross_o_proge = input("Оценка производительности(2) или такая прога(1)?")
    except ValueError:
        continue
    if vopross_o_proge == "1":
        try:
            b = int(input("введите кол во элиментов в массиве"))
        except ValueError:
            print("Вы ввели данные не верно повторите воод")
            continue
        if b > 400000:
            print("Вы ввели слишком большое число ваш комп згорит повторите ввод")
            continue
        arr = np.zeros(b, dtype=int)
        opshin = int(input("как хотите заполнить массив 1-рандом 2-собой"))
        if opshin == 2:
            for j in range(b):
                try:
                    arr[j] = int(input("Заполните матрицу"))
                except ValueError:
                    print("Повторите ввод")
                    continue
        elif opshin == 1:
            for j in range(b):
                arr[j] = random.randint(1, 10000)
        else:
            print("Повторите попытку")
            continue
        try:
            vopross = input("1 - пирамидальная сортировка\n"
                            "2 - коктельная сортировка\n"
                            "3 - выборка\n"
                            "4 - вставка\n"
                            "5 - шелл\n"
                            "6 - пузырьком\n")
        except ValueError:
            continue
        if vopross == "1":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(piramid_sort(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(piramid_sort(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        elif vopross == "2":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(koktel_sort(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(koktel_sort(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        elif vopross == "3":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(viborka(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(viborka(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        elif vopross == "4":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(vstavka(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(vstavka(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        elif vopross == "5":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(hell(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(hell(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        elif vopross == "6":
            vopross = input("1 - в возростании\n"
                            "2 - в порядке убывания\n")
            t = time.clock()
            if vopross == "1":
                arres = str(puzir(arr, True)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            elif vopross == "2":
                arres = str(puzir(arr, False)).split()
                print("Массив: ", arres[1:-2])
                print("Кол во сравнений: ", arres[-2])
                print("Кол во перестановок: ", arres[-1])
            else:
                print("Ввод не правильный")
                continue
            print(str(time.clock() - t))
        break
    elif vopross_o_proge == "2":
        while True:
            b = 100
            arr = np.zeros(b, dtype=int)
            for j in range(b):
                arr[j] = random.randint(1, 10000)
            print(vivod(arr))
            print("А ТЕПЕРЬ МЫ ПУСТИМ ОТСОРТИРОВАНЫЙ МАСИВ ЧЕРЕЗ СОРТИРОВКИ ЕЩЁ РАЗ!!!!")
            arr = sorted(arr)
            print(arr)
            print()
            print(vivod(arr))
            print("А ТЕПЕРЬ МЫ ПУСТИМ ОТСОРТИРОВАНЫЙ МАСИВ ЧЕРЕЗ СОРТИРОВКИ ЕЩЁ РАЗ НО В ОБРАТНОМ ПОРЯДКЕ!!!!")
            arr = sorted(arr, reverse=True)
            print(arr)
            print()
            print(vivod(arr))
            break
