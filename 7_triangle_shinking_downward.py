def triDownwards(a):
    setTri = []
    n = len(a)
    for i in range(0, n):
        # s = '*'*i + a[i:n]
        s = ''
        for _ in range(i):
            s += '*'
        s += a[i:n]
        setTri.append(s)
    return setTri

a = input('write something:\n')
z = triDownwards(a)
for i in z:
    print(i)
