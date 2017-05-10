import random
import numpy as np
a = int(input("Введите количество цифр кратное 100: "))

if a % 100 == 0:
    file_f = open('f.txt', 'w')
    for j in range(1, a+1):
        file_f.write(str(random.randint(-100, 100))+ " ")
    file_f.flush()
    file_f.close()
    file_f = open('f.txt')
    k = file_f.readline()
    h = list()
    print(max(k))
    for i in k:
        print(i)
        h.append(i)
    print(h)
    '''h.append(i)
    print(h)'''


    file_f.flush()
    file_f.close()


























    '''file_f.close()
    file_f = open('f.txt', 'r')
    file_g = open('g.txt', 'w')
    str_file_read = file_f.readlines()
    print("числа: ", str_file_read)
    file_f.close()
    p = str_file_read[0:101]
    print(p)
    k = max(p)
    print(k)
    file_g.write(str(k))
    file_g = open('g.txt', 'r')

    str_file_read_g = file_g.read()

    print("kkk: ", str_file_read_g)
    print()

    file_g.flush()

    file_g.close()
    flag = False'''
else:
    print("Число должно быть кратным 100!")