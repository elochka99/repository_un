#
import numpy as np
while True:
    arr = np.array(input('Введите числа: ').split(","), dtype=int)
    k = len(arr)
    if k == 5:
        print("Ваш массив: ", arr)
        print("сумма массива= ", sum(arr))
        print("среднее арифметическое = ", sum(arr) / k)
    else:
        print("Нужно ввести 5 чисел!")

