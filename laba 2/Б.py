import re
letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}
letters1 = set()
while True:
    seq = input('Введите последовательность слов русского алфавита, разделяйте '
    'запятой, в конце точка: ')
    seq = seq.lower()
    if re.search('[а-я]', seq):
        if re.search(',', seq):
            if seq.endswith('.'):
                seq = seq.replace('.', '')
                seq = seq.split(', ')
                seq = set(seq)
                seq1 = seq.copy()
                n = 0
                for i in seq1:
                    n += 1
                    if n % 2 == 0:
                        seq.remove(i)
                    else:
                        pass
                for j in seq:
                    for c in j:
                        if c in letters:
                            letters1.add(c)
                let = sorted(letters1)
                let1 = ' '.join(let)
                print(let1)

            else:
                print('postav tochku')
        else:
            print('postav komu')
    else:
        print('ruskimi pishi')
    ex = input('Для продолжения нажмите Enter...')
    if ex != '':
        break
