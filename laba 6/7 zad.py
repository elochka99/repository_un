import os
flag = True
while flag:
    os.chdir('D:/NewFolder/')
    os.chdir('D:/NewFolder/My')
    print('Мы находимся в следующуей директории:', os.getcwd())
    print('Заполните анкету')
    while True:
        name = input('Как Вас зовут ?\n'
                     '>>>')
        if not (name.isalpha() and name.istitle()):
            print('введите имя c большой буквы!')
            flag = False
        else:
            try:
                year = input('Сколько Вам лет?\n'
                             '>>>')
                if int(year) not in range(10, 101):
                    print('Вы допустили ошибку!')
                    flag = False
                else:
                    email = input('Ваш электронный адрес?\n'
                                  '>>>')
                    if not ('@' and '.') in email:
                        print('Вы допустили ошибку!')
                        flag = False
                    else:
                        with open('MyAnket.txt', 'w') as g:
                            g.write('Имя: ' + name + '\n')
                            g.write('Возраст: ' + year + '\n')
                            g.write('Электроннный адрес: ' + email + '\n')
                        with open('MyAnket.txt', 'r') as f:
                            line = f.readlines()
                        for i in line:
                            print(i, sep='')
                    w = input('\nХотите начать работу с программой заново? [1 - да]: ')
                    if w == '1':
                        print()
                        continue
                    else:
                        print("пока!")
                        break
            except (ValueError, IndexError, MemoryError):
                print("введите корректные данные!")

