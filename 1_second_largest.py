def sec_largest(arr, n):
    arr.sort()
    for i in range(n):
        if arr[-1]/arr[n-1-i] > 1:
            return arr[n-1-i]
    return -1

arr = [2, 3, 4, 55, 55, 4]
num = sec_largest(arr, len(arr))
print(num)
