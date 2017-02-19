k=True
while k:
    v=set()
    while len(v)<7:
        try:
            print("вам нужно ввести 30 чисел")
            v.add(int(input()))
            pass
        except ValueError:
            print("последовательность должна состоять из чисел")
    print("ваша последовательность :",v)
    #u=v
    m=min(v)
    M=max(v)
    print ("минимальное число=",m,"максимальное число=",M)
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
