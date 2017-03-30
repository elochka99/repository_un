from enum import Enum

while True:
    class Marka(Enum):
        BMW = 1
        Volkswagen = 2
        Toyota = 3
        Ford = 4
        Skoda = 5
        Renault = 6
        Kia = 7
        Nissan = 8


    print("Здравствуйте, вы находитесь в программе, которая отображает сведения об автомобилях вашего города.")
    try:
        while True:
            a = int(input("Вы можете 1 - Зарегистрировать новое авто; \n"
                          " 2 - вывести данные об уже зарегестрированных автомобилях. \n"
                          "Выберите что вы хотите сделать в программе: "))
            if a == 1:
                nomers = []
                names = []
                datas = []
                markas = []
                b = input("вы выбрали функцию регистрации авто. Если это так тогда введите - [+] , \n"
                          " если вы ошиблись введите любой символ. \n"
                          "Вводите: ")
                if b == "+":
                    c = int(input("Какое количество автомобилей вы хотите зарегистрировать? Ответ: "))
                    print("Вам нужно заполнить бланк регистрации авто: ")
                    for i in range(c):
                        while True:
                            try:
                                marka_ = int(input("[ BMW = 1,  Volkswagen = 2,  Toyota = 3,  Ford = 4,   \n"
                                                   "Skoda = 5, Renault = 6, Kia = 7,  Nissan = 8 ] \n"
                                                   "(если в предложенном списке нету вашей марки - вам нужна другая программа) \n"
                                                   "Введите номер марки вашего авто из списка: "))

                                if marka_ in range(9):
                                    marka = Marka(marka_).name
                                    markas.append(marka)
                                    break
                                else:
                                    print("вы должны выбрать марку из списка")
                                    continue
                            except ValueError:
                                print("вы должны указать марку цифрой из списка")
                        while True:
                            try:
                                namee = input("Введите фамилию владельца: ")
                                if namee.isalpha:
                                    names.append(namee)
                                    break
                                else:
                                    print("Фамилия должна состоять из букв!")
                                    continue
                            except ValueError:
                                print("вы должны указать фамилию бувами")
                        while True:
                            try:
                                nomer = int(input("Введите номер автомобиля состоящий из 4 цифр: "))
                                nomer = str(nomer)
                                if len(nomer) == 4:
                                    nomers.append(nomer)
                                    break
                                else:
                                    print("номер должен быть четырехзначным")
                                    continue
                            except ValueError:
                                print("вводите цифры!")
                        while True:
                            data = input("Введите дату регистрации в формате (31.12.2017): ").split(".")

                            if int(data[0], base=10) <= 31 and len(data[0]) == 2:
                                if int(data[1], base=10) <= 12 and len(data[0]) == 2:
                                    if int(data[2], base=10) <= 2017 and len(data[2]) == 4:
                                        datas.append(data)
                                        break
                            else:
                                print("введите верные данные!")
                                continue


                    print("просмотр зарегестрированных авто: ")
                    for j in range(c):
                        print("марка ", markas[j])
                        print("фамилия ", names[j])
                        print("номер ", nomers[j])
                        print("дата ", datas[j])
                else:
                    break
            elif a == 2:
                imena = ["Александров", "Шестакова", "Мишина", "Григорян", "Шитов", "Козлов", "Воробьев"]
                nom = ["1456", "0954", "1459", "1235", "9054", "7895", "2232"]
                mar = ["BMW", "Volkswagen", "Toyota", "Ford", "Ford", "BMW", "Nissan"]
                dat = ["12.12.12", "13.11.12", "24.12.11", "15.08.13", "27.03.11", "01.09.13", "22.04.12"]
                n = int(input("Ваш выбор - просмотр данных базы. Выберите сортировку для владельцев марки: \n "
                              "1- фамилии в алфавитном порядке \n"
                              "2- номера по возрастанию"))
                if n == 1:
                    m = int(input("[ BMW = 1,  Volkswagen = 2,  Toyota = 3,  Ford = 4,   \n"
                                  "Skoda = 5, Renault = 6, Kia = 7,  Nissan = 8 ] \n"
                                  "(если в предложенном списке нету вашей марки - вам нужна другая программа) \n"
                                  "Введите номер марки авто из списка: "))
                    ma = Marka(m).name
                    if m in range(9):
                        if ma in mar:
                            for i in range(len(mar)):
                                if mar[i] == ma:
                                    h = []
                                    h.append((mar[i], imena[i], nom[i], dat[i]))
                                    print(h)

                        else:
                            print("Владельцев автомобилей такой марки еще нет в базе!")
                    else:
                        print("вы должны выбрать марку из списка")
                elif n == 2:
                    m = int(input("[ BMW = 1,  Volkswagen = 2,  Toyota = 3,  Ford = 4,   \n"
                                  "Skoda = 5, Renault = 6, Kia = 7,  Nissan = 8 ] \n"
                                  "(если в предложенном списке нету вашей марки - вам нужна другая программа) \n"
                                  "Введите номер марки авто из списка: "))
                    ma = Marka(m).name
                    if m in range(9):
                        if ma in mar:
                            for i in range(len(mar)):
                                if mar[i] == ma:
                                    h = []
                                    h.append((nom[i], imena[i], dat[i]))
                                    print(h)
                        else:
                            print("Владельцев автомобилей такой марки еще нет в базе!")
                    else:
                        print("вы должны выбрать марку из списка")


    except (ValueError, IndexError):
        print("Слишком много ошибок, начните лучше сначала ")
    f = input('Хотите вернуться к началу программы (у) или выйти ? : ')
    if f == 'y':
        continue
    else:
        break