import timeit
setup = '''
text = input('Введіть рядок для пошуку: ')
pattern = input('Введіть рядок який хочете знайти: ')
d = [0] * len(pattern)
j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
        j = d[j-i]
    if pattern[i] == pattern[j]:
        j += 1
    d[i] = j
'''
stmt = '''
j = 0
for i in range(0, len(text)):
    while j > 0 and pattern[j] != text[i]:
        j = d[j-1]
    if pattern[j] == text[i]:
        j += 1
    if j == len(pattern):
        print('Подстрока найдена в позиции: ', i-j+1)
        j = d[j-1]
    '''
print('Час пошуку', timeit.timeit(stmt=stmt, setup=setup, number=1), 'секунд')
