def Akkerm(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return Akkerm(n-1, m)
    elif n > 0 and m > 0:
        return Akkerm(n-1, Akkerm(n, m-1))
while True:
    n = int(input("n = "))
    m = int(input("m = "))
    print("Значение рекурсивно: ", Akkerm(n, m))

'''def akker_Iter(n,m):
    a = []
    a.append(n)
    a.append(m)
    while a:
        c = a.pop()
        b = a.pop()
        if b == 0:
            a.append(c+1)
        elif b > 0 and c == 0:
            a.append(b-1)
            a.append(1)
        elif n > 0 and m > 0:
            a.append(b-1)
            a.append(b)
            a.append(c-1)
    return a[0]
    '''



