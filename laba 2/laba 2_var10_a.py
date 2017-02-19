k=True
while k:
    v=set()
    while len(v)<30:
        try:
            v.add(int(input()))
            pass
        except ValueError:
            print("последовательность должна состоять из чисел")
    print("ваша последовательность :",v)
    u=v
    m=min(u)
    M=max(u)
    print ("минимальное число=",m,"максимальное число=",M)
    for i in range(m,M):
        if i not in v:
            print(i)
        else:
            continue
