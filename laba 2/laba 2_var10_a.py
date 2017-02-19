k=True
while k:
    v=set()
    print("введите 30 чисел :")
    while len(v)<30:
        try:
            v.add(int(input()))
            pass
        except ValueError:
            print("последовательность должна состоять из чисел")
    print("ваша последовательность :",v)
    #u=v
    m=min(v)
    M=max(v)
    print ("минимальное число=",m,"максимальное число=",M)
    print("числа которые не входят в последовательность:")
    for i in range(m,M):
        if i not in v:
            print(i,end=",")
        else:
            continue
    print()
    a = input('Хотите продолжить? [y/n]: ')
    if a == 'y':
        continue
    else:
        break
