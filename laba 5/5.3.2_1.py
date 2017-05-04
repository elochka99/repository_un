
def Akkerm_rec(m,n):
    if m == 0:
        return ( n + 1 )
    if m > 0 and n == 0:
        return Akkerm_rec(m-1, 1)
    if m > 0 and n > 0:
        return Akkerm_rec(m-1, Akkerm_rec(m, n-1))

def Akk_iter(m,  n):
   assert isinstance(m, int) and m >= 0
   assert isinstance(n, int) and n >= 0
   s = []
   while True:
      if not m:
         if not s:
            return n+1
         m, n = s.pop(), n+1
      elif not n:
         n = 1
         m = m-1
      else:
         s.append(m-1)
         n-=1


while True:
    try:
        n = int(input("n = "))
        m = int(input("m = "))
        print("Значение рекурсивно: ", Akkerm_rec(m, n))
        print("Значение итерационно: ", Akk_iter(m, n))
    except (ValueError, MemoryError, RecursionError):
        print("всaдите корекные данные!")
        continue


