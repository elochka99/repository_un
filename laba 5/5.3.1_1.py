# Горохова Елена КНИТ 16-А
# Даны натуральные числа n,m найти наибольший общий делитель Nod(n,m)
def iter(n, m):
    '''
    
    :param n: значение числа
    :param m: значение числа
    :return: НОД
    '''
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n
def recurs(n, m):
    '''
    
    :param n: значение числа
    :param m: значение числа
    :return: НОД
    '''
    if n < m:
        n, m = m, n
    if 0 < m:
        return recurs(m, n % m)
    else:
        return n
while True:
    try:
        n = int(input("введите N - "))
        if n <= 1000000:
            m = int(input("введите M - "))
            if m <= 1000000:
                print("итерационное нахождение НОД = ", iter(n, m))
                print("рекурсивное нахождение НОД = ", recurs(n, m))
            else:
                print("введите число меньше 1000000!")
                continue
        else:
            print("введите число меньше 1000000!")
            continue
    except ValueError:
        print("введите целое число!")