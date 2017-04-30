import numpy as np
while True:
    arr = np.array(input('vedite').split(","))
    a = arr[::-1]
    for i in a:
        print(i)