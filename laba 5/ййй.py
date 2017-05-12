def form_iter(s):
    '''
    Итерационно проверяет формулу
    :param s: текст формулы
    :return: True or False
    '''
    k = True
    c = 0
    if s[len(s)-1:] == '.':
        s = s[:len(s)-1]
        for i in s:
            if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                c = 1
            elif (i == '*' or i == '-' or i == '+') and c == 1:
                c = 0
            else:
                k = False
        if k == True and c == 1:
            return True
        else:
            return False
    else:
        return False
def form_rec(s):
    '''
    Рекурсивно проверяет формулу
    :param s: текст формулы
    :return: True or False
    '''
    c = 0
    k = False
    t = 0
    dok = False
    per = False
    if t == 0:
        t = 1
        if s[len(s) - 1:] == '.':
            dok = True
            q = s[len(s) - 2:len(s) - 1]
            if q == '1' or q == '2' or q == '3' or q == '4' or q == '5' or q == '6' or q == '7' or q == '8' or q == '9':
                per = True
            s = s[:len(s) - 1]


    if len(s) == 0:
        return False
    elif len(s) == 1 and s[0] == '.':
        return False
    else:
        i = s[len(s) - 1:]
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            c = 1
            k = True
        elif (i == '*' or i == '-' or i == '+') and c == 1:
            c = 0
            k = True
        else:
            k = False
        s = s[:len(s) - 1]
        form_rec(s)
    if k == True and c == 1 and dok == True and per == True:
        return True
    else:
        return False


while True:
    s = input('Введите формулу заканчивая точкой: ')
    print("итеративно: ", form_iter(s))
    print("рекурсивно: ", form_rec(s))
