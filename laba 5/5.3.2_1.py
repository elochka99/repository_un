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




