# Горохова Елена, КНИТ16-А
# Дана непустая последовательность слов из строчных руссских букв; между соседними словами -
# - запятая, за последним словом - точка. Вывести на экран в алфавитном порядке все глухие
# согласные буквы, которые входят в каждое нечетное слово и не входят хотя бы в одно четное слово.
import re

letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}
while True:
    inp = input("введите слова через запятую и в конце точка :")
    inp = inp.lower()
    if re.search('[а-я]', inp):
        if re.search(',', inp):
            if inp.endswith('.'):
                print(inp)
            else:
                print('нужна точка в конце')
        else:
            print('нужно писать через запятую')
    else:
        print('нужно писать русские буквы')

    temp = inp
    c = 0
    res = set()
    for i in temp:
        if i == ',':
            t = inp.index(',')
            inp = inp[:t] + str(c) + inp[t+1:]
            c += 1
        if i == '.':
            t = inp.index('.')
            inp = inp[:t] + str(c) + inp[t+1:]

    inp = set(inp.split(' '))
    for i in letters:
        flag1 = None
        flag2 = None
        for j in inp:
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
