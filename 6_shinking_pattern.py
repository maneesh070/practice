def triDownwards(x):
    setTri = []
    n = len(a)
    for i in range(n):
        setTri.append(a[0:(n-i)])
    return setTri
a = input('write something:\n')
z = triDownwards(a)
print(z)
