import numpy as np
import math
while True:
    arr = np.array(input('vedite').split(","), dtype=int)
    for i in arr:
        n = i**2
        m = math.sqrt(i)
        print(n, m)