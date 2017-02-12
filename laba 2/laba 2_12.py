n= 10
a = [[1,2,3],[4,5,6],[7,8,9]]
s_1={i for i in range(n)}
s_2={i for i in range(n)}
s=0
for i in s_1:
    if i>2:
        break
    for j in s_2:
        if j>2:
            break
        b=a[i]
        c=b[j]
        s+=c
print(s)