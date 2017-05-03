def iter(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n
def recurs(n, m):
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