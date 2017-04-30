import numpy as np
while True:
    arr = np.array(input('Введите: ').split(","), dtype=str)
    k = len(arr)
    if k == 5:
        b = input("введите букву: ")
        for i in arr:
            if i[0] == b:
                print(i)
    else:
        print("Нужно ввести 5 фамилий!")