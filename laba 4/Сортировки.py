import numpy as np
import random
def bubble_sort(A):
    N = len(A)
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(N-i-1):
            if (A[j] > A[j+1]):
                tmp = A[j]
                A[j] = A[j+1]
                A[j + 1] = tmp
                flag = True
        i+=1
def selection_sort(A):
    N = len(A)
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if A[j] < A[min]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
def insertion_sort(A)
    N = len(A)
    for i in range(1,N):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
def cocktail(a):
    for i in range(len(a)//2):
        for j in range(1+i, len(a)-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        return a
def shell_sort(d):
    n = len(d)
    while True:
        n = n//2
        for i in range (n, len(d), n):
            k = i
            while k>0 and d[k] < d[k-n]:
                d[k], d[k-n] = d[k-n], d[k]
                k = k - n
        if n ==  1:
            break
    return d
def heap_sort(li):
    def down_Heap(li, k, n):
        new_elem = li[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and li[child] < li[child+1]:
                child += 1
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
        down_Heap(li, 0, i)
    return li
print('\nКак Вы хотите вводить информацию в БД: вручную или рандомно? [1/2]')
    while True:
        try:
            ask_inp = int(input('Выберите цифру → '))
            if ask_inp not in range(1, 3):
                print('Пожалуйста, введите корректные данные ☻\n')
                continue
            break

        except ValueError:
            print('Пожалуйста, введите целое число ☻\n')
            continue

