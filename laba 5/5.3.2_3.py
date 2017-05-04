znaki = "+-*"
def text(t, p):
    if p == -1:
        return True
    elif t[p] in znaki:
        return t[p-1].isdigit() and text(t, p-1)
    elif t[p].isdigit():
        return t[p - 1] in znaki and text(t, p-1)
    else:
        return False
def text_iter(t, p):
    k = True
    for i in range(p, 1, -1):
        if not (t[p] in znaki and t[p-1].isdigit()):
            k = False
            break
    return k
t = input("Введите знаки букавы: ")
p = len(t)-1
print(text(t, p))
print(text_iter(t, p))