import numpy as np
import random
import time
while True:
    while 1:
        while True:
            try:
                g = int(input('Введите 1, если хотите ввести данные с клавиатуры, 2- сгенерировать автоматически: '))
            except ValueError:
                print('Ошибка')
            else:
                break
        if g<=2 and g>=0:
                break
        else:
                print('Ошибка. Вы ввели неверное значения')
    while 2:
        while True:
            try:
                c=int(input('Ввведите 1 для сортировки по возростанию, 2 для сортировки по убыванию: '))
            except ValueError:
                print('Ошибка')
            else:
                break
        if c<=2 and c>=0:
                break
        else:
                print('Ошибка. Вы ввели неверное значения')
    while 3:
        while True:
            try:
                q=int(input('Введите 1 для coctail sort, 2-Shell sort, 3- heapsort: '))
            except ValueError:
                print('Ошибка')
            else:
                break
        if q<=3 and q>=0:
                break
        else:
            print('Ошибка. Вы ввели неверное значения')
    start1 = time.time()
    def Shell(a):
        count1=0
        count2=0
        t=int(len(a)/2)
        while t>0:
            for i in range(len(a)-t):
                j=i
                if c==1:
                    while j>=0 and a[j]>a[j+t]:
                        count1+=1
                        a[j],a[j+t]=a[j+t],a[j]
                        count2+=1
                        j-=1
                elif c==2:
                    while j>=0 and a[j]<a[j+t]:
                        count1+=1
                        a[j],a[j+t]=a[j+t],a[j]
                        count2+=1
                        j-=1
            t=int(t/2)
        end1 = time.time()
        print('Произведено сравнений:',count1)
        print('Произведено перестановок:',count2)
        print('Время выполнения алгоритма: ',end1 - start1)

    start2 = time.time()
    def cocktail_sort (a):
        count1=0
        count2=0
        for k in range(len(a)-1, 0, -1):
            swapped = False
            if c==1:
                for i in range(k, 0, -1):
                    if a[i]>a[i-1]:
                        count1+=1
                        a[i], a[i-1] = a[i-1], a[i]
                        count2+=1
                        swapped = True

                for i in range(k):
                    if a[i] > a[i+1]:
                        count1+=1
                        a[i], a[i+1] = a[i+1], a[i]
                        count2+=1
                        swapped = True
                if not swapped:
                    return a
            elif c==2:
                for i in range(k, 0, -1):
                    if a[i]<a[i-1]:
                        count1+=1
                        a[i], a[i-1] = a[i-1], a[i]
                        count2+=2
                        swapped = True

                for i in range(k):
                    if a[i] < a[i+1]:
                        count1+=1
                        a[i], a[i+1] = a[i+1], a[i]
                        count2+=2
                        swapped = True
                if not swapped:
                    return a
        end2 = time.time()
        print('Произведено сравнений:',count1)
        print('Произведено перестановок:',count2)
        print('Время выполнения алгоритма: ',end2 - start2)

    start3 = time.time()
    def HeapSort(a):
        count1=0
        count2=0
        def shiftDown(a,i,j):
            nonlocal count1
            nonlocal count2
            while i*2+1<j:
                if c==1:
                    if i*2+1==j-1 or a[i*2+1]>a[i*2+2]:
                        count1+=1
                        maxChild=i*2+1
                    else:
                        maxChild=i*2+2
                    if a[i]<a[maxChild]:
                        a[i],a[maxChild]=a[maxChild],a[i]
                        count2+=1
                        i=maxChild
                    else:break
                if c==2:
                        if i*2+1==j-1 or a[i*2+1]<a[i*2+2]:
                            count1+=1
                            maxChild=i*2+1
                        else:
                            maxChild=i*2+2
                        if a[i]>a[maxChild]:
                            a[i],a[maxChild]=a[maxChild],a[i]
                            count2+=1
                            i=maxChild
                        else:break
        for i in range(int(len(a)/2-1),-1,-1):
            shiftDown(a,i,len(a))
        for i in range(len(a)-1,0,-1):
            a[0],a[i]=a[i],a[0]
            count2+=1
            shiftDown(a,0,i)
        end3 = time.time()
        print('Произведено сравнений:',count1)
        print('Произведено перестановок:',count2)
        print('Время выполнения алгоритма: ',end3 - start3)

    if g==1:
        while 4:
            while True:
                try:
                    s=np.array(input('Введите исходные данные: ').split(','),dtype=int)
                except ValueError:
                    print('Вы ввели неверные данные')
                else:
                    break
            a=list(s)
            if len(a)>30:
                print('Ошибка. Превышен допустимый размер')
            else:
                break
        print('\nИсходный массив:\n',a)
        if q==1:
                cocktail_sort(a)
        elif q==2:
                Shell(a)
        elif q==3:
                HeapSort(a)
        print('\nОтсортированнный массив:\n',a)
    elif g==2:
        a=[random.random() for i in range(10000)]
        if q==1:
           cocktail_sort (a)
        elif q==2:
                Shell(a)
        elif q==3:
                HeapSort(a)
    print("Введите 1, чтобы продолжить или 2, чтобы прекратить выполнения программы")
    p = int(input("Ваш выбор:"))
    if p == 1:
        continue
    elif p == 2:
        break
    break