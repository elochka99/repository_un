# Горохова Елена КНИТ 16-А

import random
while True:
    try:
        b = int(input("Введите количество элементов в файле: "))
        file_f = open('f.txt', 'w')
        h = list()
        for i in range(1, b+1):
            k = str(random.randint(0, 100))
            file_f.write(k +",")
            h.append(k)
        file_f.close()
        file_f = open('f.txt', 'r')
        file_g = open('g.txt', 'w')
        str_file = file_f.readlines()
        h2 = []
        for i in h:
            if i not in h2:
                h2.append(i)
        print(h)
        print(h2)
        h2.reverse()
        file_g.write(str(h2) +",")
        file_g.flush()
        file_g.close()
        file_f.flush()
        file_f.close()
        file_f = open('f.txt', 'r')
        file_g = open('g.txt', 'r')
        print(file_g.read())
        file_g.flush()
        file_f.flush()
        file_f.close()
        file_g.close()
        w = input('\nХотите начать работу с программой заново? [1 - да]: ')
        if w == '1':
            print()
            continue
        else:
            print("пока!")
            break
    except (ValueError, IndexError, MemoryError):
        print("введите корректные данные! ")