def first_element(a, n, k):
    newdict = {}
    for i in a:
        if i not in newdict:
            newdict[i] = 1
        else:
            newdict[i] += 1
        if i in newdict:
            if newdict[i] == k:
                return i
    return -1



a = [1, 3, 5, 2, 4, 2, 4, 4, 4, 2, 2]
n = len(a)
k = int(input('no. of times: '))
print(first_element(a, n, k))