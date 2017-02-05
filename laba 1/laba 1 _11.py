# Gorokhova Olena KNIT 16-A
#по дате d,m,y определить дату следующего дня
N = True
while N:
    days = range(1, 32)
    mounths = range(1,13)
    years = range(1901, 2016)
    d, m, y = int(input('day: ')),\
    int(input('mounth: ')),\
    int(input('year: '))
    if d in days and m in mounths and y in years:
        if d == 31 and m == 12:
            d = 1
            m = 1
            y += 1
        else:
            d+=1
        print('next date:', d , '.', m , '.', y)
    else:
        print("error")
    while True:
        K = input("хотите продолжить? 1 - да, 2 - нет :")
        if K == "1":
            break
        else:
            flag = False
            print("пока\n")
