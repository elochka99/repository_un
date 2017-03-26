import timeit
setup = '''
text = list(map(str, input('Введіть рядок для пошуку: ').split()))
pattern = input('Введіть рядок який хочете знайти: ')
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
print('Час пошуку', timeit.timeit(stmt=stmt, setup=setup, number=1), 'секунд')
