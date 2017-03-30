#Горохова Елена КНИТ 16-А
#алгоритм Вагнера-Фишера
import timeit
setup = '''
textpol = input('Введите строку для поиска: ')
textpol = textpol.split(' ')
pattern = input('Введите строку которую найти: ')
k = int(input('Введите точность ввода: '))
b = []
index=[]
slova = []
kol = 0
index_slov = 0
'''
stmt = '''
for i in range(len(textpol)):
    text = textpol[i]
    n = len(text)
    m = len(pattern)
    if n > m:
        text, pattern = pattern, text
        n, m = m, n
    current = range(n+1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous[j] + 1, current[j-1] + 1, previous[j-1]
            if text[j - 1] != pattern[i - 1]:
                change += 1
            current[j] = min(add,delete,change)
    if current[n] <= k:
        index.append(current[n])
        slova.append(text)
        kol += 1
for t in range(kol+1):
    for i in range(kol):
        if index[i] == index_slov:
            print(slova[i])
    index_slov += 1
'''
print('Время поиска', timeit.timeit(stmt=stmt, setup=setup, number=1), 'секунд')
