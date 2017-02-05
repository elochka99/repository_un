#Gorokhova Olena KNIT 16-A
#вывести значение переменной х, обозначающее некоторую длину
#в единицах р, заменить величиной этой же длины в метрах
k = True
while k:
    from enum import Enum
    class measure(Enum):
        decimetre = 1
        kilometre = 2
        metre = 3
        millimetre = 4
        centimetre = 5
    try:
        x = float(input('length: '))
        p = measure[input('measure: ')]
        if p == measure.centimetre:
            print(x*0.01, "metre")
        elif p == measure.decimetre:
            print(x*0.1, "metre")
        elif p == measure.kilometre:
            print(x*1000, "metre")
        elif p == measure.millimetre:
            print(x*0.001, "metre")
        elif p == measure.metre:
            print(x, "metre")
        else:
            print("введите правильные данные")
    except (ValueError, KeyError):
        print('error')
    while True:
        K = input("хотите продолжить? 1 - да, 2 - нет :")
        if K == "1":
            break
        elif K == "2":
            flag = False
            print("пока\n")



