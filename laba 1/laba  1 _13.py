#Gorokhova Olena KNIT 16-A
#по s-названию страны вывести название континента
k = True
while k:
    from enum import Enum
    class country(Enum):
        Germany = 1
        Cuba = 2
        Laos = 3
        Monaco = 4
        Bangladesho = 5
        Ukraine = 6
    class continent(Enum):
        Asia = 1
        America = 2
        Europe = 3
    try:
        s = country[input('country: ')]
        if s == country.Germany:
            print(continent(3))
        elif s == country.Cuba:
            print(continent(2))
        elif s == country.Laos:
            print(continent(1))
        elif s == country.Monaco:
            print(continent(3))
        elif s == country.Bangladesho:
            print(continent(1))
        elif s == country.Ukraine:
            print(continent(3))
        else:
            print("введите корректные данные")
    except (ValueError, KeyError):
        print('wrote value or key')
    while True:
        K = input("хотите продолжить? 1 - да, 2 - нет :")
        if K == "1":
            break
        elif K == "2":
            flag = False
            print("пока\n")
