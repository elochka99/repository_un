import re
letters={'к','п','т','с','ф','х','ц','ч','ш'}

while True:
    a = input("Введите последовательность слов из русских букв через запятую \n"
              "без пробелов и с точкой в конце: ")
    if a != "":
        if a.__getitem__(-1) == ".":
            a = a.replace(a.__getitem__(-1), "")
            b = frozenset(a.split(","))
            p=set()
            for i in b:
                if re.search("[а-яА-Я]", i):
                    if i.isalpha():
                        print(i.lower())
                    else:
                        print("!Не должны присутствовать пробелы и небуквы")
                        break
                else:
                    print("!Слова должны состоять из русских букв")
                    break


        else:
            print("!Отсутствует точка в конце")
    else:
        print("!Последовательность должна быть непустая")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break