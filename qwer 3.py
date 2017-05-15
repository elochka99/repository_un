# программа что определяет является ли введенное слово идентификатором (англ буквы, цифры, дочеркивание...
# начинается с буквы или подчеркивания.
while True:
    try:
        x = input("Введи слово: ")
        if x[0] == '_' or x[0].isalpha():
            for i in x:
                if i.isalpha() or i.isdigit() or i == '_':
                    print("True")
                else:
                    print("False")
        else:
            print("не идентификатор")
        y = input("continue - [1]? - ")
        if y == '1':
            continue
        else:
            break
    except (ValueError, IndexError, KeyError):
        print("введите коректные данные")