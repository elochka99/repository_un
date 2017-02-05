#Gorokhova Olena KNIT 16-A
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из
# пяти 12-летних подциклов. Подциклы обозначались названиями цвета: зелёный,
# красный, желтый, белый и черный. Внутри каждого подцикла, годы носили
# названия животных: крысы, коровы, тигра, зайца, драковна, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) --
# начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.
k = True
while k:
    import random
    from enum import Enum
    class color(Enum):
        Green = 1
        Red = 2
        Yellow = 3
        White = 4
        Black = 5
    class animal(Enum):
        Rat = 1984
        Cow = 1985
        Tiger = 1986
        Rabbit = 1987
        Dragon = 1988
        Snake = 1989
        Hourse = 1990
        Sheep = 1991
        Monkey = 1992
        Chicken = 1993
        Dog = 1994
        Pig = 1995
    i = int(input("введите год:"))
    n = i
    h = n
    b = range(1984, 1996)
    if i < 1984:
        while i not in b:
            i += 12
    elif i > 1996:
        while i not in b:
            i -= 12
    if n in range(1984,1996):
        n = "Green"
    elif n in range(1996,2008):
        n = "Red"
    elif n in range(2008,2020):
        n = "Yellow"
    elif n in range(2020,2032):
        n = "White"
    elif n in range(2032,2044):
        n = "Black"
    else:
        print("error")
    print(h,'-',n, animal(i).name)
