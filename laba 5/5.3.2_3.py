# Горохова Елена КНИТ 16-А
# Дан некоторый текст,за которым следует точка. Программа определяет является ли текст правильной записью формулы,
# которая записана в сообтветствии с синтаксисом EBNF
znak = "+-*"
r = ['0','1','2','3','4','5','6','7','8','9']
def text(t, p):
    '''
    Проверяет формулу рекурсивно
    :param t: параметр что передает текст формулы
    :param p: параметр что передает длину формулы
    :return: верная или не верная формула
    '''

    if p == 0:
        return True

    elif t[p] in znak:
        return t[p-1].isdigit() and text(t, p-1)
    elif t[p].isdigit():
        return t[p - 1] in znak and text(t, p-1)
    else:
        return False

def text_iter(t, p):
    '''
    Проверяет формулу итерационно
    :param t: параметр что передает текст формулы
    :param p: параметр что передает длину формулы
    :return: верная или не верная формула
    '''
    global r
    k = True
    for i in range(p, 0, -1):
        if t[i] in znak and t[i - 1] not in r:
            k = False
            break
        elif t[i] not in r and t[i] not in znak:
            k = False
            break

    return k
while True:
    try:

        t = input("Введите формулу:  ")
        p = len(t) - 1
        if len(t) == 1 and t[0] not in r:
            raise ValueError()
        elif (t[-1] != "." or t[-2] not in r):
            raise ValueError()


    except ValueError:
        print("Введите коректные данные!")
        continue
    t = t[:len(t) - 1]
    p = len(t) - 1
    print("рекурсивно = ", text(t, p))
    print("Итерационно = ", text_iter(t, p))