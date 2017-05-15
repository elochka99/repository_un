import io
k = []
try:
    f = open('f.txt', 'w')
    n = input("text = ")
    f.write(n)
    f.flush()
    f.close()
    f = open('f.txt', 'r')
    m = list(f.read())
    for i in m:
        if i is i.upercase():
            i = i.lowercase
            k.append(i)
        else:
            k.append(i)
    g = open('g.txt', 'w')
    g.write(k)
    f.flush(), f.close(), g.flush(), g.close()
    open('g.txt','r')
    print(g.read())
except ValueError:
    print("error")

