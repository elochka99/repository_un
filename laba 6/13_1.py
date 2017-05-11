# Горохова Елена КНИТ 16-А
while True:
    try:
        b = int(input("Введите количество элементов в файле: "))
        file_f = open('f.txt', 'w')
        for i in range(1, b+1):
            file_f.write(str(i)+"\n")
        file_f.close()
        file_f = open('f.txt', 'r')
        file_g = open('g.txt', 'w')
        str_file = file_f.readlines()
        for j in str_file:
            if int(j) % (int(j)**(1/2)) == 0 :
                file_g.write(str(j))
        file_g.flush()
        file_f.flush()
        file_f.close()
        file_g.close()
        file_g = open('g.txt', 'r')
        print("числа которые являются полными квадратами: ", file_g.read())
        w = input('\nХотите начать работу с программой заново? [1 - да]: ')
        if w == '1':
            print()
            continue
        else:
            print("пока!")
            break
    except (ValueError, IndexError, MemoryError):
        print("введите корректные данные! ")