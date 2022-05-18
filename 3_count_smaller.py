def countsmaller(a):
    b = []
    for i in a:
        if i <= keynumber:
            b.append(keynumber)
    return len(b)
a = [4, 2, 74, 89, 74, 76]
keynumber = int(input('enter your key number: '))
smaller = countsmaller(a)
print(smaller)