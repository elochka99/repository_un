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
        Asia = country.Bangladesho, country.Laos
        America = country.Cuba
        Europe = country.Germany, country.Monaco
        s = country[input('country: ')]
    except (ValueError, KeyError):
        print('wrote value or key')
    for i in Asia:
        if i == s:
            print(continent.Asia.name)
    for i in Europe:
        if i == s:
           print(continent.Europe.name)
    if America == s:
        print(continent.America.name)
    while True:
        L = input("хотите продолжить? 1 - да, 2 - нет :")
        if L == "1":
            break
        elif L == "2":
            flag = False
            print("пока\n")
