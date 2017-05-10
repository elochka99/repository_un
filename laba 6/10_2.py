a = int(input("Введите количество цифр кратное 100: "))
'''while True:'''
    if a % 100 == 0:
        file_f = open('f.txt', 'w')
        for i in range(1, a+1):
            file_f.write(str(i)+"\n")
        file_f.close()
        file_f = open('f.txt', 'r')
        file_g = open('g.txt', 'w')
        str_file_read = file_f.readlines()
        print("числа: ",str_file_read)
        file_f.close()
        p = str_file_read[1:100]
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
        flag = False
    else:
        print("Число должно быть кратным 100!")
        continue
        '''k = []
        for i in str_file_read:
            for j in range(1, 100):
                k.append(j)
            break
        z = max(k)
        file_g.write(str(z))
        file_g.close()
        file_g = open('g.txt', 'r')

        str_file_read_g = file_g.read()

        print("kkk: ",str_file_read_g)
        print()

        file_g.flush()

        file_g.close()

    else:
        print("Число должно быть кратным 100!")
        continue'''