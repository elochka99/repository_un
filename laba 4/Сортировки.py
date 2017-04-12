import numpy as np
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


