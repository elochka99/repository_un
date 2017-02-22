import re
letters={'к','п','т','с','ф','х','ц','ч','ш'}
while True:
    seq = input('Введите последовательность слов русского '
                'алфавита, разделяйте запятой, в конце точка: ')
    t=seq()
    w = []
    if seq != '':
        if seq.__getitem__(-1) == '.':
            seq = seq.replace(seq.__getitem__(-1), '')
            words = seq.split(', ')
            if len(words) != 0:
                for i in words:
                    if re.search("[а-я]", i):
                        if i.isalpha():
                            w.append(i)
                            print(i, end=' ')
                        else:
                            print("введите слова из букв через запятую")

                    else:
                        print('Слова должны состоять из строчых русских букв, которые разделены запятой')
                        break
            else:
                print('Слова должны быть разделены запятыми.')
        else:
            print('Точка нужна.')
    else:
        print('Последовательность должна быть непустой.')

    print()
    ex = input('Для продолжения нажмите Enter...')
    if ex != '':
        break
