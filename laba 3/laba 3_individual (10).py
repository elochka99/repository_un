from enum import Enum
qq = True
while qq:
    class Marka(Enum):
        BMW = 1
        Volkswagen = 2
        Toyota = 3
        Ford = 4
        Skoda = 5
        Renault = 6
        Kia = 7
        Nissan = 8
        Hyundai = 9
        Mercedes_Benz = 10

    print("Здравствуйте, вы находитесь в программе, которая отображает сведения об автомобилях вашего города.")
    try:
        a = int(input( "Вы можете 1 - Зарегистрировать новое авто; \n"
                       " 2 - вывести данные об уже зарегестрированных автомобилях. \n"
                       "Выберите что вы хотите сделать в программе: "))
        if a == 1:
            nomers = []
            names = []
            datas = []
            markas = []
            b = input("вы выбрали функцию регистрации авто. Если это так тогда введите - да , \n"
                  " если вы ошиблись введите - ошибка. \n"
                      "Вводите: ")
            if b == "да":
                c = int(input("Какое количество автомобилей вы хотите зарегистрировать? Ответ: "))
                print("Вам нужно заполнить бланк регистрации авто: ")
                for i in range(c):
                    marka_ = int(input("[ BMW = 1,  Volkswagen = 2,  Toyota = 3,  Ford = 4,  Skoda = 5, \n"
                               "Renault = 6, Kia = 7,  Nissan = 8,  Hyundai = 9,  Mercedes_Benz = 10 ] \n"
                                 "(если в предложенном списке нету вашей марки - вам нужна другая программа) \n"
                                 "Введите номер марки вашего авто из списка: "))
                    if marka_ in range(10):
                        marka = Marka(marka_).name
                        markas.append(marka)
                    else:
                        print("вы должны выбрать марку из списка")
                        continue

                    namee = input("Введите фамилию владельца: ")
                    names.append(namee)

                    nomer = int(input("Введите номер автомобиля состоящий из 4 цифр: "))
                    nomer = str(nomer)
                    if len(nomer) == 4:
                        nomers.append(nomer)
                    else:
                        print("номер должен быть четырехзначным")
                        break

                    data = (input("Введите дату регистрации в формате (31.12.17): ").split("."))
                    datas.append(data)
                    for j in range(c):
                        print("марка ",  (markas[j]))
                        print("фамилия ", (names[j]))
                        print("номер ", (nomers[j]))
                        print("дата ",  (datas[j]))
            else:
                continue



    except ValueError:
        print("Введите коректные данные")
