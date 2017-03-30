#Горохова Елена КНИТ 16-А
#алгоритм Бойера-Мура-Хорспула
import timeit
setup = '''
text = list(map(str, input('Введите строку для поиска: ').split()))
pattern = input('Введите строчку которую найти: ')
text.sort()
text = str(text)
n = len(text)
m = len(pattern)
d = [m] * (ord(max(max(text), max(pattern))) + 1)
for i in range(m - 1):
    d[ord(pattern[i])] = m - i - 1
pos = -1
i = 0
'''
stmt = '''
while n - i >= m and pos == -1:
    j = m - 1
    while text[i + j] == pattern[j]:
        if j == 0:
            pos = i
            break
        j -= 1
    i += d[ord(text[i + m - 1])]
if pos != -1:
    print('Подстрока найдена в позиции: ', pos)
else:
    print('Элемент не найден.')
'''
print('Время поиска', timeit.timeit(stmt=stmt, setup=setup, number=1), 'секунд')
