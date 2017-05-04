def rec(n, m):
    if m == 0:
        if n == 0:
            return 1
        return 0
    if m <= n:
        return rec(n, m-1) + rec(n - m, m)
    return rec(n,n)
def iter(n, m):
    s = 0
    a = []
    a.append((n, m))
    while a:
        r = a.pop()
        b = r[0]
        c = r[1]
        if c == 0:
            if b == 0:
                s += 1
        elif c > b:
            a.append((b, b))
        elif c <= b:
            a.append((b, c - 1))
            a.append((b - c, c))
    return s
z = 1
while z == 1:
    try:
        n = m = int(input('N = '))
        if n <= 0 or m <= 0:
            print('Не правильное число')
        else:
            kol = rec(n,m)
            kol1 = iter(n, m)
            print('Количество представлений заданного числа: ',"рекурсивно - ",kol, "итерационно - ", kol1)
        print('Для продолжения нажмите - 1\nДля завершения любую другую кнопку')
        z = int(input())
    except ValueError:
        print("Введите коректные данные!")
