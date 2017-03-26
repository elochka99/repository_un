import timeit

setup = '''
text = input('Введите текст, в котором искать: ')
stroka = input('Введите строку которую искать: ')
a = len(text)
b = len(stroka)
i = j = 0
'''
stmt = '''
while i <= a - b and j < b:
    if text[i + j] == stroka[j]:
        j += 1
    else:
        i += 1
        j = 0
if j == b:
    print('Искомая строка найдена в позиции ', i+1)
else:
    print('такой строки в тексте нет!')
'''
print('Час пошуку', timeit.timeit(stmt=stmt, setup=setup, number=1), 'секунд')