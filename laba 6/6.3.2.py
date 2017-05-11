# Горохова Елена КНИТ 16-А
import numpy as np
def Dijkstra(N, S, matrix):
    valid = [True]*N
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight
while True:
    try:
        N = int(input("Введите количество городов: "))
        matrix = np.ones((N, N), dtype=int)
        matrix = matrix * (-1)
        a = []
        for i in range(N):
            a.append(input("Введите название города:  "))
        for i in range(N):
            for j in range(N):
                if i != j:
                    if matrix[i][j] == -1 and matrix[j][i] == -1:
                        matrix[i][j] = matrix[j][i] = int(
                            input("укажите длинну пути между городами " + a[i] + " и " + a[j] + ": "))
                else:
                    matrix[i][j] = 0
        print(Dijkstra(N, 0, matrix))
        w = input('\nХотите начать работу с программой заново? [1 - да]: ')
        if w == '1':
            print()
            continue
        else:
            print("пока!")
            break
    except (ValueError, IndexError):
        print("введите корректные данные! ")

