# Горохова Елена, КНИТ16-А
# Дана непустая последовательность слов из строчных руссских букв; между соседними словами -
# - запятая, за последним словом - точка. Вывести на экран в алфавитном порядке все глухие
# согласные буквы, которые входят в каждое нечетное слово и не входят хотя бы в одно четное слово.
import re

letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}
while True:
    p = input("введите слова через запятую и в конце точка :")
    p = p.lower()
    if re.search('[а-я]', p):
        if re.search(',', p):
            if p.endswith('.'):
                print(p)
            else:
                print('нужна точка в конце')
        else:
            print('нужно писать через запятую')
    else:
        print('нужно писать русские буквы')

    temp = p
    c = 0
    res = set()
    for i in temp:
        if i == ',':
            t = p.index(',')
            p = p[:t] + str(c) + p[t+1:]
            c += 1
        if i == '.':
            t = p.index('.')
            p = p[:t] + str(c) + p[t+1:]

    p = set(p.split(' '))
    for i in letters:
        flag1 = None
        flag2 = None
        for j in p:
            if int(j[-1]) % 2 == 0:
                if i not in set(j):
                    flag1 = True
            else:
                if i in set(j):
                    flag2 = True
                else:
                    flag2 = False
                    break
        if flag1 and flag2:
            res.add(i)

    print(res)
    ex = input('Для продолжения нажмите Enter...')
    if ex != '':
        break
