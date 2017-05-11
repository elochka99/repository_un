# Горохова Елена КНИТ 16-А
# Сформировать функцию подсчета количества разных представлений заданного натурального числа в виде
# суммы не менее двух попарно различных натуральных слагаемых

def rec_decompose(c):
    def func(c, id):
        if c == 0 and id == 0:
            return 1
        if c <= 0 or id <= 0:
            return 0
        return func(c - id, id) + func(c - 1, id - 1)
    stack = []
    if c == 0 or c == 1:
        return 0
    for i in range(1, c):
        stack.append(func(c, i))
    return max(stack)
def func_iter(c):
    a = c - 1
    return len(list(enumerate(range(a, c // 2 - (c - a), -1))))

def rec(n, m):
    '''
    Функция рекурсивно считает количество разных представлений числа
    :param n: число
    :param m: число
    :return: число
    '''
    if m == 0:
        if n == 0:
            return 1
        return 0
    if m <= n:
        return rec(n, m-1) + rec(n - m, m)
    return rec(n,n)
def iter(n, m):
    '''
    Функция рекурсивно считает количество разных представлений числа
    :param n: число
    :param m: число
    :return: число
    '''
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
while True:
    try:
        n = m = int(input('N = '))
        if n <= 0 or m <= 0:
            print('Не правильное число')
        else:
            kol = rec(n,m)
            kol1 = iter(n, m)
            print('Количество представлений заданного числа: ',"рекурсивно - ",kol, "итерационно - ", kol1)
            print("количество представлений без 1+1+1... = ", rec_decompose(n) )
        w = input('\nХотите начать работу с программой заново? [1 - да]: ')
        if w == '1':
            print()
            continue
        else:
            print("пока!")
            break
    except (ValueError, RecursionError, MemoryError):
        print("Введите коректные данные!")
